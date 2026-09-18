import os
import shutil

# 1. Define the target directory to clean up
# '.' means the current directory where the script is running
TARGET_DIR = '.' 

# 2. Map file extensions to their new folder names
EXTENSION_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Executables': ['.exe', '.dmg', '.pkg'],
    'Code': ['.py', '.html', '.css', '.js', '.java']
}

def organize_files():
    # Loop through every item in the target directory
    for filename in os.listdir(TARGET_DIR):
        file_path = os.path.join(TARGET_DIR, filename)

        # Skip if it's a directory (we only want to move files)
        if os.path.isdir(file_path):
            continue

        # Extract the file extension (e.g., '.jpg')
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Find which category folder this extension belongs to
        for folder_name, extensions in EXTENSION_MAP.items():
            if extension in extensions:
                # Create the category folder if it doesn't exist yet
                folder_path = os.path.join(TARGET_DIR, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                
                # Move the file to its new home
                destination_path = os.path.join(folder_path, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved: {filename} -> {folder_name}/")
                break # Stop searching categories once a match is found

if __name__ == "__main__":
    print("Starting file organization...")
    organize_files()
    print("Cleanup complete!")
