__author__ = "Karun Sandhu"

import argparse


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
