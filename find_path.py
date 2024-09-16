import os

def find_file(root_folder, filename):
    matches = []
    for dirpath, dirnames, filenames in os.walk(root_folder):
        if filename in filenames:
            matches.append(os.path.join(dirpath, filename))
    
    if matches:
        print(f"Found {len(matches)} match(es):")
        for match in matches:
            print(match)
    else:
        print(f"No matches found for '{filename}'.")

# You can either prompt for filename and use a fixed root folder (Cibus)
root_folder = input("Enter the directory you're looking in: ")  # Search in the 'Cibus' directory by default
filename = input("Enter the file name you're looking for: ")

find_file(root_folder, filename)
