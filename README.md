# Python File Organizer

This script sorts files into folders based on their file extensions. It only
organizes files directly inside the directory you specify; it does not recurse
into subdirectories.

## Usage

```bash
python organizer.py /path/to/folder
```

Files are moved into lowercase extension folders (for example, `photo.JPG` is
moved into `jpg/`). Files without an extension are moved into `no_extension/`.
If a file with the same name already exists in the destination folder, a
numbered suffix is added to the moved file's name.
