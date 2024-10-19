from sys import argv
import os

# config:
PATH = "/mnt/data/music" # enter a full path to your existing music folder

class Mp3ipe:
    def __init__(self, path) -> None:
         # check if path is correct
        if not path and not os.path.exists(path):
            print("Invalid path to music directory!")
            exit()

        # init arguments
        self.args = ' '.join(argv[1:])

        if not self.args == "": # play sound
            music_file = self.choose(self.find(self.args, path)) # find a music file/folder
            # play music file with mpv
            os.system(f'mpv "{music_file}" --display-tags=icy-title --no-audio-display --no-video')
        else: # show directory contents
            os.system(f"ls -uxN {path}")

    def find(self, name, path):
        final_file, final_dir = [], [] # init variables holding found music
        
        # walk thru entire music directory 
        for root, dirs, files in os.walk(path):
            # directory
            for dir_name in dirs:
                if name.lower() in dir_name.lower():
                    final_dir.append(os.path.join(root, dir_name))
            # file
            for file_name in files:
                if name.lower() in file_name.lower():
                    final_file.append(os.path.join(root, file_name))
        return final_dir + final_file # return path to a file/folder

    def choose(self, options):
        # if the song was found at all
        if not options:
            print("No results have been found...")
            exit()

        # if only one song is matching
        if len(options) == 1:
            print(f"Playing: {options[0].removeprefix(PATH)}...")
            return options[0]

        # if there is more than one song matching
        print("Found multiple results:")
        for i, option in enumerate(options, 1):
            # display matching songs in a order
            print(f"{i}. {option.removeprefix(PATH)}")
        
        while True:
            try:
                # let the user choose a song they want
                choice = int(input(f"Pick a number (1-{len(options)}): "))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                else: # if user picked a wrong number
                    print(f"Invalid choice! Pick a number between 1 and {len(options)}.")
            except ValueError: # if user picked invalid character
                print("Please enter a valid number!")
            except KeyboardInterrupt: # if user forced quit
                print(" (interrupted)")
                break

if __name__ == "__main__":
    Mp3ipe(PATH)