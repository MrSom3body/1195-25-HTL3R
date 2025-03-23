__author__ = "Karun Sandhu"

import argparse
import os
import sys

from UE05_kasiski.kasiski import Kasiski
from UE05_kasiski.caesar import Caesar


class CVcrackNamespace(argparse.Namespace):
    infile: str = ""
    cipher: str = ""
    verbose: bool = False
    quiet: bool = False


def parse_arguments() -> CVcrackNamespace:
    """
    Parses command-line arguments.

    :return: Parsed arguments as a CVcrackNamespace object.
    """
    parser = argparse.ArgumentParser(
        description="CVcrack - Caesar & Vigenere cracker"
    )
    _ = parser.add_argument("infile", type=str, help="File to be encrypted")
    _ = parser.add_argument(
        "-c",
        "--cipher",
        choices=["caesar", "c", "vigenere", "v"],
        required=True,
        help="Cipher to use",
    )
    _ = parser.add_argument(
        "-v", "--verbose", action="store_true", help="More output"
    )
    _ = parser.add_argument(
        "-q", "--quiet", action="store_true", help="No output"
    )

    return parser.parse_args(namespace=CVcrackNamespace())


def process_file(args: CVcrackNamespace) -> None:
    """
    Processes the input file by cracking a file encrypted with the Vigenere or
    the Caesar cipher.

    :param args: Parsed command-line arguments containing file paths and cipher settings.
    """
    if not os.path.isfile(args.infile):
        print(f"{args.infile}: No such file or directory", file=sys.stderr)
        sys.exit(1)

    with open(args.infile, "r", encoding="utf-8") as f:
        text = f.read()

    if args.cipher in ["caesar", "c"]:
        cipher_name = "Caesar"
        cipher = Caesar()
        key = cipher.crack(text, 1)[0]
    else:
        cipher_name = "Vigenere"
        cipher = Kasiski(text)
        key = cipher.crack_key(6)

    if args.verbose:
        print(
            f"Cracking {cipher_name}-encrypted file {args.infile}: key = {key}"
        )
    else:
        print(key)


if __name__ == "__main__":
    args = parse_arguments()
    process_file(args)
