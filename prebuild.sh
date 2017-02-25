# Hack as OLA does not support v3 protobuf yet
pacman -R python2-protobuf
pacman -R protobuf

# Download and install v2 version of protobuf
wget https://archive.archlinux.org/packages/p/protobuf/protobuf-2.6.1-2-x86_64.pkg.tar.xz
sudo pacman -U protobuf-2.6.1-2-x86_64.pkg.tar.xz
wget https://archive.archlinux.org/packages/p/python2-protobuf/python2-protobuf-2.6.1-2-x86_64.pkg.tar.xz
sudo pacman -U python2-protobuf-2.6.1-2-x86_64.pkg.tar.xz

