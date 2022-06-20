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
- Change the variables in obs-ws.py to your setup
* Filepath has to be with / and not \\, can be done in python but this is just a dirty script to get going.
* The timestamp is the Danish Timestamp format, can be changed to your liking. Look into datetime documentation.
* OBSIP, OBSPORT, OBSPASSWORD and OBSScene (OBSScene is the scene in your OBS you would like to take a picture of.
- Make +x on run.sh (due to Octolapse not being able to execute Python directly (i couldnt get it working atleast).
- Test it locally before putting Octolapse into the mix (./run.sh)
- Make Octolapse run run.sh (for example /home/pi/run.sh) in "External Camera Setup - Script" under the default camera.

# This would not have been possible without:
- simpleobsws - https://github.com/IRLToolkit/simpleobsws
- OBSWebsocket - https://github.com/obsproject/obs-websocket/
- OBS Studio - https://github.com/obsproject/obs-studio

# Created by:

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
