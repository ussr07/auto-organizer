# Auto-Organizer 🧹

A lightweight, zero-dependency Python CLI tool that instantly declutters directories by sorting files into categorized subfolders based on their extensions.

## Features
- **Zero Dependencies:** Uses only Python's built-in `os` and `shutil` libraries.
- **Smart Categorization:** Automatically routes images, documents, archives, and code files to designated directories.
- **Safe Execution:** Ignores existing directories to prevent recursive loops and skips files without extensions.

## Usage

1. Clone the repository or download `organizer.py`.
2. Place the script in the directory you wish to clean (e.g., your `Downloads` folder).
3. Run the script from your terminal:

```bash
python organizer.py
