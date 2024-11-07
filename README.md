# Mp3ipe

Basic python music player made for not demanding folks, that just want to listen to their music :3

## Requirements

To fully use Mp3ipe you will need to install some of those dependencies on your operating system!

**1. python:**

Debian:
```bash
sudo apt-get -y install python3-fabulous
```

Arch:
```bash
sudo pacman -S python-fabulous
```

Fedora/Red Hat:
```bash
yum install python-fabulous
```

Compiling it from source:
```bash
wget https://github.com/jart/fabulous/releases/download/0.4.0/fabulous-0.4.0.tar.gz
tar -xvzf fabulous-0.4.0.tar.gz
cd fabulous-0.4.0
sudo python setup.py install
```

**2. mpv:**

Debian:
```bash
sudo apt-get -y install mpv
```

Arch:
```bash
sudo pacman -S mpv
```

Fedora/Red Hat:
```bash
yum install mpv
```

Compiling it from source:
```bash
git clone https://github.com/mpv-player/mpv-build.git && cd mpv-build
./rebuild -j4
sudo ./instal
```

## Manual

**1. Configure:** You can achive this by editing main.py and modifying CONFIG variable.

**2. Use:** You will need to execute this file so go in terminal and add execution permission to it:
```bash
chmod +x main
```
without parameters it will just display the contents of your music library that you defined in CONFIG variable. 

Otherwise if you would like to use parameters, so in this example:
```bash
./main There, there
```
Mp3ipe will find the music file you were searching for and play it for you!
![](https://i.ibb.co/tbC7RBD/image.png)

**3. Fork:** You can make your own fork of Mp3ipe if you want to implement your own features, and I'd love it!

## FAQ

### Will there be a support for MS Windows?
No, I am not interested in developing software compatible with this operating system, at least not for this project.
