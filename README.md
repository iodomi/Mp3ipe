# Mp3ipe

Basic python music player made for not demanding folks, that just want to listen to their music :3

## Requirements

To fully use Mp3ipe you will need to install some of those dependencies on your operating system!

**1. python:**

Debian:
`sudo apt-get -y install python3-fabulous`

Arch:
`sudo pacman -S python-fabulous`

Fedora/Red Hat:
`yum install python-fabulous`

Compiling it from source:
`wget https://github.com/jart/fabulous/releases/download/0.4.0/fabulous-0.4.0.tar.gz`

`tar -xvzf fabulous-0.4.0.tar.gz`

`cd fabulous-0.4.0`

`sudo python setup.py install`

**2. mpv:**

Debian:
`sudo apt-get -y install mpv`

Arch:
`sudo pacman -S mpv`

Fedora/Red Hat:
`yum install mpv`

Compiling it from source:
`git clone https://github.com/mpv-player/mpv-build.git && cd mpv-build`

`./rebuild -j4`

`sudo ./install`

## Manual

**1. Configure:** You can achive this by editing main.py and modifying CONFIG variable.

**2. Use:** You will need to execute this file so go in terminal and type: `python main.py`, without parameters it will just display the contents of your music library that you defined in CONFIG variable. Otherwise if you use parameters, so: `python main.py Paranoid Android` (this is an example) Mp3ipe will find your song and play it!

**3. Fork:** You can make your own fork of Mp3ipe if you want to implement your own features, and I'd love it!

## FAQ

### Will there be a support for MS Windows?
No, I am not interested in developing software compatible with this operating system, at least not for this project.
