__author__ = "Karun Sandhu"

import argparse
import pandas as pd
import re


class GradeNamespace(argparse.Namespace):
    n: str = ""
    s: str = ""
    m: str = "Nummer"
    f: list[str] = []
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
        "-f",
        type=lambda s: [item.strip() for item in s.split(",")],
        help="name of the subjects to filter (seperated by a comma)",
    )
    _ = parser.add_argument(
        "-v", "--verbose", action="store_true", help="more output"
    )
    _ = parser.add_argument(
        "-q", "--quiet", action="store_true", help="no output"
    )

    return parser.parse_args(namespace=GradeNamespace())


def read_xml(filename: str) -> pd.DataFrame:
    """
    Read a file into a pandas DataFrame with the help of regular expressions.

    :param filename: The file to read.
    :return: A DataFrame containing the data of the XML file.
    """
    with open(filename) as f:
        content = f.read()

    xml = re.sub(r">\s+<", "><", content)

    students_pattern = re.compile(r"<Schueler>(.*?)</Schueler>", re.DOTALL)
    student_blocks: list[str] = students_pattern.findall(xml)

    tag_value_pattern = re.compile(
        r"<(Nummer|Anrede|Vorname|Nachname|Geburtsdatum)>(.*?)</\1>"
    )

    records: list[dict[str, str]] = []
    for block in student_blocks:
        fields = dict(tag_value_pattern.findall(block))
        records.append(fields)

    df = pd.DataFrame(records)
    return df


if __name__ == "__main__":
    args = parse_arguments()
    student_data = read_xml(args.s)
    grade_data = pd.read_csv(args.n, sep=";", dtype=str)
    if args.f:
        grade_data = grade_data.filter(items=[args.m, *args.f])

    student_grade_data = pd.merge(student_data, grade_data)
