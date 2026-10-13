import argparse
import shutil
from pathlib import Path


def organize_files(directory: str | Path) -> list[Path]:
    """Move files in a directory into folders named after their extensions."""
    source = Path(directory)
    if not source.is_dir():
        raise NotADirectoryError(f"Not a directory: {source}")

    moved_files = []
    for file_path in source.iterdir():
        if not file_path.is_file():
            continue

        folder_name = file_path.suffix[1:].lower() or "no_extension"
        destination_folder = source / folder_name
        destination_folder.mkdir(exist_ok=True)
        destination = destination_folder / file_path.name

        counter = 1
        while destination.exists():
            destination = destination_folder / (
                f"{file_path.stem} ({counter}){file_path.suffix}"
            )
            counter += 1

        shutil.move(str(file_path), str(destination))
        moved_files.append(destination)

    return moved_files


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sort files into folders named after their extensions."
    )
    parser.add_argument("directory", type=Path, help="Directory containing files to organize")
    args = parser.parse_args()

    try:
        moved_files = organize_files(args.directory)
    except NotADirectoryError as error:
        parser.error(str(error))

    print(f"Organized {len(moved_files)} file(s) in {args.directory}.")


if __name__ == "__main__":
    main()
