__author__ = "Karun Sandhu"

import argparse


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


if __name__ == "__main__":
    args = parse_arguments()
