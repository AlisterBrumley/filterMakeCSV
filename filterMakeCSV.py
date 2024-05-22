from pathlib import Path
import typer


def main(file_location: str):
    file_path = Path(file_location)
    csv_path = file_path.with_suffix(".csv")

    with file_path.open() as f:
        word_list = [
            word
            for line in f
            for word in line.replace(" • ", ",").replace("\n", ",").split()
        ]

    string = "".join(word_list)
    csv_path.write_text(string)


if __name__ == "__main__":
    typer.run(main)
