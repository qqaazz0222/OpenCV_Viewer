# OpenCV_Viewer
Displays the work history of opencv running in a server environment (no display) where commands such as imshow cannot be used in real time.

# Install

## Install Gstreamer
```
sudo apt-get install libgstreamer1.0-0
sudo apt-get install gstreamer1.0-plugins-base gstreamer1.0-plugins-good
sudo apt-get install gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
sudo apt-get install gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools
```
## Install Gstreamer Python Patch
```
sudo apt-get install python-gst-1.0 python3-gst-1.0
```
## Install Dev-Packages
```
sudo apt-get install libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
sudo apt-get install libfontconfig1-dev libfreetype6-dev libpng-dev
sudo apt-get install libcairo2-dev libjpeg-dev libgif-dev
sudo apt-get install libgstreamer-plugins-base1.0-dev
```
## Update
```
sudo apt update
sudo apt upgrade
```
## Install RTSP Server
```
sudo apt-get install gir1.2-gst-rtsp-server-1.0
```