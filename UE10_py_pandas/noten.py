__author__ = "Karun Sandhu"

import argparse


class GradeNamespace(argparse.Namespace):
    n: str = ""
    s: str = ""
    m: str = "Nummer"
    f: str = ""
    verbose: bool = False
    quiet: bool = False


def parse_arguments() -> GradeNamespace:
    """
    Parses command-line arguments.

    :return: Parsed arguments as a CVcrackNamespace object.
    """
    parser = argparse.ArgumentParser(description="noten.py by Karun Sandhu")
    _ = parser.add_argument("outfile", type=str, help="output file (csv)")
    _ = parser.add_argument(
        "-n", type=str, help="csv file with grades", required=True
    )
    _ = parser.add_argument(
        "-s", type=str, help="xml file with student data", required=True
    )
    _ = parser.add_argument(
        "-m",
        type=str,
        # default="Nummer", # not needed as it is already set in GradeNamespace
        help="name of column to link to (default: 'Nummer')",
    )
    _ = parser.add_argument(
        "-f", type=str, help="name of the subject to filter"
    )
    _ = parser.add_argument(
        "-v", "--verbose", action="store_true", help="more output"
    )
    _ = parser.add_argument(
        "-q", "--quiet", action="store_true", help="no output"
    )

    return parser.parse_args(namespace=GradeNamespace())


if __name__ == "__main__":
    args = parse_arguments()
