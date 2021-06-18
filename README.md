# PyQt5-DHT22
Author: Valentinooo  
Copyright © 2021 EvoLab  
This system using Raspberry Pi read temperature and humidity from DHT22 sensor then display it on GUI

## Graphic User Interface:
## System Diagram:
## Hardware Diagram:
<img src="https://github.com/valentinooodev/PyQt5-DHT22/blob/main/Diagram.png" alt="drawing" width="300"/>  

## Build PyQt5 for Raspberry Pi:

1. Uncomment source line in sources-list:
```bash
sudo nano /etc/apt/sources.list
```

2. Update system:
```bash
sudo apt update
```
```bash
sudo apt full-upgrade
```
```bash
sudo reboot now
```

3. Install Depedencies
```bash
sudo apt-get build-dep qt5-default
```
```bash
sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
```
```bash
sudo apt-get install flex bison gperf libicu-dev libxslt-dev ruby nodejs make git
```
```bash
sudo apt-get install libxcursor-dev libxcomposite-dev libxdamage-dev libxrandr-dev libxtst-dev libxss-dev libdbus-1-dev libevent-dev libfontconfig1-dev libcap-dev libpulse-dev libudev-dev libpci-dev libnss3-dev libasound2-dev libegl1-mesa-dev
```
```bash
sudo apt-get install libasound2-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev
```
```bash
sudo apt-get install freeglut3-dev
```
```bash
sudo apt install libclang-6.0-dev llvm-6.0
```

4. Build Sip
```bash
wget https://www.riverbankcomputing.com/static/Downloads/sip/4.19.24/sip-4.19.24.tar.gz
```
```bash
tar -xzvf sip-4.19.24.tar.gz
```
```bash
cd sip-4.19.24
```
```bash
python configure.py
```
```bash
make
```
```bash
sudo make install
```

5. Build PyQt5:
```bash
cd ..
```
```bash
wget https://www.riverbankcomputing.com/static/Downloads/PyQt5/PyQt5-5.15.1.dev2008081558.tar.gz
```
```bash
tar -xzvf PyQt5-5.15.1.dev2008081558.tar.gz
```
```bash
cd PyQt5-5.15.1.dev2008081558
```
```bash
python configure.py
```
```bash
make
```
```bash
sudo make install
```

## Clone App and run on Raspberry Pi:
```bash
git clone https://github.com/valentinooodev/PyQt5-DHT22.git
```
```bash
cd PtQt5-DHT22
```
```bash
python app.py
```
