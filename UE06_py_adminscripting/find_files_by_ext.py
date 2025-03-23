__author__ = "Karun Sandhu"

import pathlib

directory = pathlib.Path(input("Enter the path to search: "))
ext = input("Enter the extension to search: ")

for path in sorted(directory.rglob(f"*.{ext}")):
    print(f"{path.absolute().resolve()}")
