import os

def get_path():
    config = ""

    if os.path.exists('path.txt'):
        try:
            with open('path.txt', 'r') as f:
                config = f.read()
        except Exception:
            print("Config file was not found!")

    return config

def file_search(name, directory):
    results = []
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
        print(f"Playing: {options[0].removeprefix(base_dir)}...")
        return options[0]

    print("Found multiple results:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option.removeprefix(base_dir)}")
    
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
        os.system(f'vlc "{path}"')
    else:
        print(f"File was not found ({path})...")

inp: str = input("Which song/album do you want to play?: ")  

base_dir = get_path()
if base_dir and os.path.exists(base_dir):
    dir_results = dir_search(inp, base_dir)
    file_results = file_search(inp, base_dir)

    results = dir_results + file_results

    choice = choose(results)
    if choice:
        play(choice)
else:
    print("Invalid directory path!")
