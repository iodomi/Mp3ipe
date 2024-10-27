from sys import argv
import os

CONFIG = {
    "path": "/mnt/data/music", # enter a full path to your music library
    "cover": True, # enable if you want to display album covers
    "cover_size": 64 # size of album cover in pixels
}

class Mp3ipe:
    def __init__(self, config) -> None:
        try:
            # variables
            self.path = config.get("path")
            self.args = ' '.join(argv[1:])

            # check if path is correct
            if not self.path and not os.path.exists(self.path):
                print("Invalid path to music directory!")
                exit()

            if self.args == "": # show directory contents
                os.system(f"ls -uxN {self.path}")
            else: # play sound

                # find a music file/folder
                self.music_file = self.choose(self.find(self.args, self.path))
                
                if config.get("cover"): # check if cover is enabled
                    # fetch and display album cover
                    self.extract_cover(self.music_file, config.get("cover_size"))

                # play music file with mpv
                os.system(f'mpv {self.music_file.replace(" ", "\\ ")} --display-tags=icy-title --no-audio-display --no-video')
                
        except KeyboardInterrupt:
            print(" (interrupted)")

    def extract_cover(self, music_file, cover_size):
        if os.path.isdir(music_file):
            music_file = music_file + "/" + os.listdir(music_file)[0]

        cover_file = "cover.jpg"

        # extract image using ffmpeg
        os.system(f"ffmpeg -i {music_file.replace(" ", "\\ ")} -an -vcodec copy {cover_file}")

        if os.path.exists(cover_file):
            os.system(f"clear && tiv -w {cover_size} -h {cover_size} {cover_file}") # display cover
            os.remove(cover_file) # remove temporary cover file

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
            return options[0]

        # if there is more than one song matching
        print("Found multiple results:")
        for i, option in enumerate(options, 1):
            # display matching songs in a order
            print(f"{i}. {option.removeprefix(self.path)}")
        
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
    Mp3ipe(CONFIG)