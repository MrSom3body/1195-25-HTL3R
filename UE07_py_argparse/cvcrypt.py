__author__ = "Karun Sandhu"

import argparse
import sys
from UE05_kasiski.caesar import Caesar
from UE05_kasiski.vigenere import Vigenere
import os


class CVcryptNamespace(argparse.Namespace):
    infile: str = ""
    outfile: str = ""
    cipher: str = ""
    key: str = ""
    encrypt: bool = False
    decrypt: bool = False
    verbose: bool = False
    quiet: bool = False


def parse_arguments() -> CVcryptNamespace:
    """
    Parses command-line arguments.

    :return: Parsed arguments as a CVcryptNamespace object.
    """
    parser = argparse.ArgumentParser(
        description="CVcrypt - Caesar & Vigenere encrypter"
    )
    _ = parser.add_argument("infile", type=str, help="File to be encrypted")
    _ = parser.add_argument("outfile", type=str, help="Target file")
    _ = parser.add_argument(
        "-c",
        "--cipher",
        choices=["caesar", "c", "vigenere", "v"],
        required=True,
        help="Cipher to use",
    )
    _ = parser.add_argument(
        "-k", "--key", type=str, help="Encryption key", required=True
    )
    _ = parser.add_argument(
        "-e", "--encrypt", action="store_true", help="Encrypt"
    )
    _ = parser.add_argument(
        "-d", "--decrypt", action="store_true", help="Decrypt"
    )
    _ = parser.add_argument(
        "-v", "--verbose", action="store_true", help="More output"
    )
    _ = parser.add_argument(
        "-q", "--quiet", action="store_true", help="No output"
    )

    args = parser.parse_args(namespace=CVcryptNamespace())

    if not args.encrypt and not args.decrypt:
        parser.error("One of --encrypt or --decrypt must be specified.")

    return args


def process_file(args: CVcryptNamespace) -> None:
    """
    Processes the input file by encrypting or decrypting it and writes the
    result to the output file.

    :param args: Parsed command-line arguments containing file paths and cipher settings.
    """
    if not os.path.isfile(args.infile):
        print(f"{args.infile}: No such file or directory", file=sys.stderr)
        sys.exit(1)

    with open(args.infile, "r", encoding="utf-8") as f:
        text = f.read()

    if args.cipher in ["caesar", "c"]:
        cipher = Caesar(args.key)
    else:
        cipher = Vigenere(args.key)

    if args.encrypt:
        result = cipher.encrypt(text)
        action = "Encrypting"
    else:
        result = cipher.decrypt(text)
        action = "Decrypting"

    with open(args.outfile, "w") as f:
        _ = f.write(result)

    if args.verbose:
        print(
            f"{action} {args.cipher} with key = {args.key} from file {args.infile} into file {args.outfile}"
        )


if __name__ == "__main__":
    args = parse_arguments()
    process_file(args)
