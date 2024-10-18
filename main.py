import os
import sys

PATH = "/mnt/data/music"

def file_search(name, directory):
    results = []
    print(f"Searching for {name}...")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if name.lower() in file.lower():
                results.append(os.path.join(root, file))
    return results

def dir_search(name, directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            if name.lower() in dir_name.lower():
                results.append(os.path.join(root, dir_name))
    return results

def choose(options):
    if not options:
        print("No results found...")
        return None

    if len(options) == 1:
        print(f"Now Playing: {options[0].removeprefix(PATH)}")
        return options[0]

    print("Found multiple results:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option.removeprefix(PATH)}")
    
    while True:
        try:
            choice = int(input(f"Pick a number (1-{len(options)}): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"Invalid choice. Please select a number between 1 and {len(options)}.")
        except ValueError:
            print("Please enter a valid number.")

def play(path):
    if os.path.exists(path):
        os.system(f'mpv "{path}"')
    else:
        print(f"File was not found ({path})...")

if PATH and os.path.exists(PATH):
    dir_results = dir_search(' '.join(sys.argv[1:]), PATH)
    file_results = file_search(' '.join(sys.argv[1:]), PATH)

    results = dir_results + file_results

    choice = choose(results)
    if choice:
        play(choice)
else:
    print("Invalid directory path!")
