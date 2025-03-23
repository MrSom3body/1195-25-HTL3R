__author__ = "Karun Sandhu"

from datetime import datetime as dt
from pathlib import Path
import shutil

source = input("Source: ")
destination = input("Destination: ")

for file in Path(source).glob(f"{'[0-9]' * 8}*.jpg"):
    date = dt.fromisoformat(file.stem[:8])
    Path(f"{destination}/{date.year}/{date.month}/{date.day}").mkdir(
        parents=True, exist_ok=True
    )
    shutil.copy(
        file, f"{destination}/{date.year}/{date.month}/{date.day}/{file.name}"
    )
