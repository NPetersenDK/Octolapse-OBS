# Octolapse-OBS
Octolapse plugin for OctoPrint with communication to OBS.

## Requirements:

### OBS Requirements:
- Camera connected to OBS
- OBS Websocket 5.x (https://github.com/obsproject/obs-websocket/releases) as of writing this README, its in beta.
- Remember to open port in local Windows Firewall

### Python3 packages needed:
- simpleobsws (pip3 install simpleobsws)

# Disclaimer
The scripts and programs are released without any support and if stuff breaks I'm not responsible. Although you're more than happy to contact me, and I might help.

# License
Released under the MIT LICENSE - check the LICENSE file

# How to:
- Download obs-ws.py and run.sh
- Make +x on run.sh (due to Octolapse not being able to execute Python directly (i couldnt get it working atleast).
- Test it locally before putting Octolapse into the mix (./run.sh)
- Make Octolapse run run.sh (for example /home/pi/run.sh) in "External Camera Setup - Script" under the default camera.

```
 ____  _____ _____ _____ ____  ____  _____ _   _
|  _ \| ____|_   _| ____|  _ \/ ___|| ____| \ | |
| |_) |  _|   | | |  _| | |_) \___ \|  _| |  \| |
|  __/| |___  | | | |___|  _ < ___) | |___| |\  |
|_|   |_____| |_| |_____|_| \_|____/|_____|_| \_|

    Nikolaj Petersen / NPetersenDK
    gist.github.com/NPetersenDK
    https://nipetersen.dk
```
