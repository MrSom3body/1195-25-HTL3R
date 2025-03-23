__author__ = "Karun Sandhu"

import pathlib

path = pathlib.Path(input("Enter the absolute path to a file: "))

print(f"Name: {path.name}")
print(f"Stem: {path.stem}")
print(f"Suffix: {path.suffix}")
print(f"Anchor: {path.anchor}")
print(
    f"Parent: {path.parent if path.parent.exists() else 'Parent directory does not exist!'}"
)
