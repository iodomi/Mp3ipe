from sys import argv
import os

# configuration:

PATH = "/mnt/data/music"

class Mp3ipe:
    def __init__(self, path) -> None:
        if not path and not os.path.exists(path):
            print("Invalid path to music directory!")
            exit()

        self.args = ' '.join(argv[1:])

        if not self.args == "":
            music_file = self.choose(self.dir_search(self.args, path) + self.file_search(self.args, path))
            os.system(f'mpv "{music_file}" --display-tags=icy-title --no-audio-display --no-video')
        else:
            os.system(f"ls -uxN {path}")

    def file_search(self, name, path):
        results = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if name.lower() in file.lower():
                    results.append(os.path.join(root, file))
        return results

    def dir_search(self, name, path):
        results = []
        for root, dirs, files in os.walk(path):
            for dir_name in dirs:
                if name.lower() in dir_name.lower():
                    results.append(os.path.join(root, dir_name))
        return results

    def choose(self, options):
        if not options:
            print("No results found...")
            exit()

        if len(options) == 1:
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
                    print(f"Invalid choice! Select a number between 1 and {len(options)}.")
            except ValueError:
                print("Please enter a valid number!")
            except KeyboardInterrupt:
                print(" (interrupted)")
                break

if __name__ == "__main__":
    Mp3ipe(PATH)