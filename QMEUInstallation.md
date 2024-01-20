# Check System Architecture
arch

# Download Ubuntu server ISO image
https://releases.ubuntu.com/focal/ubuntu-20.04.6-live-server-amd64.iso

# Install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install QEMU
brew install qemu

# Check QEMU Version
qemu-system-x86_64 --version

# Create QEMU Image 
sudo qemu-img create ubuntu.img 10G -f qcow2

# Given the image, install the VM (which takes the iso file as a “cdrom” 
# and the qemu image as a “hard disk”):

sudo qemu-system-x86_64 -hda ubuntu.img -boot d -cdrom ./ubuntu-20.04.6-live-server-amd64.iso -m 2046 -boot strict=on

# Run
qemu-system-x86_64 [machine opts] \
                [cpu opts] \
                [accelerator opts] \
                [device opts] \
                [backend opts] \
                [interface opts] \
                [boot opts]