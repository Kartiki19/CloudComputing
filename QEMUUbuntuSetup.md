# Check System Architecture
```arch``` <br> OR <br> ```uname -m```

<img width="330" alt="image" src="https://github.com/Kartiki19/CloudComputing/assets/120880459/f101cbde-ed3f-48cb-9411-3db8b42c81eb">

# Check whether ROSETTA terminal is running
```sysctl -n sysctl.proc_translated```  <br><br>
if output = 0, then ROSETTA terminal is not running

![image](https://github.com/Kartiki19/CloudComputing/assets/120880459/ae73fd4f-bbe6-4f10-b2d4-66693ef276cd)

# Download Ubuntu server ISO image for Apple MAC with M2 chip
https://cdimage.ubuntu.com/releases/20.04/release/ubuntu-20.04.5-live-server-arm64.iso

# Install homebrew
```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```

# Install QEMU
```brew install qemu```

<img width="784" alt="image" src="https://github.com/Kartiki19/CloudComputing/assets/120880459/59e25af9-208f-4861-89c9-345be4bbb528">

# Check QEMU Version
```qemu-system-aarch64 --version```

<img width="461" alt="image" src="https://github.com/Kartiki19/CloudComputing/assets/120880459/0b2ae8e7-22a6-410f-8668-3432452c2f5b">

# Check available QEMU packages
```ls /opt/homebrew/bin/qemu-*```

<img width="579" alt="image" src="https://github.com/Kartiki19/CloudComputing/assets/120880459/f6b0a785-8f22-42ea-a6b0-2350730e615d">

# Create QEMU Raw format Image 
```sudo qemu-img create -f raw ubuntuimg.raw 40G```

<img width="522" alt="image" src="https://github.com/Kartiki19/CloudComputing/assets/120880459/4c93d993-f995-4e1c-b877-00a8eef0f48c">

# Running Options
qemu-system-aarch64 [machine opts] \
                [cpu opts] \
                [accelerator opts] \
                [device opts] \
                [backend opts] \
                [interface opts] \
                [boot opts]

# Demo

![image](https://github.com/Kartiki19/CloudComputing/assets/120880459/325b9f36-e1dc-4988-b5ab-2e49e5b02719)

```
sudo qemu-system-aarch64 \
-nodefaults -accel hvf -cpu cortex-a57 -M virt,highmem=off -m 2048 -smp 2 \
-drive file=/opt/homebrew/Cellar/qemu/8.2.0/share/qemu/edk2-aarch64-code.fd,if=pflash,format=raw,readonly=on \
-drive if=none,file=ubuntulatest.img,format=raw,id=hd0 \
-device virtio-blk-device,drive=hd0,serial="dummyserial" \
-device virtio-net-device,netdev=net0 \
-netdev user,id=net0 \
-vga none -device ramfb \
-cdrom ubuntu-20.04.5-live-server-arm64.iso \
-device usb-ehci -device usb-kbd -device usb-mouse -usb ```


                
