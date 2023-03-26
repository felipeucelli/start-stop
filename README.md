# start-stop
A simple script that turns Windows machines off and on automatically
 
## Description
The script was built to run inside a linux machine for shutdown and wake up Windows machines on the local network.

## Installation
start-stop requires an installation of Python3 or greater. And run on a linux machine with some packages installed

Installing packages with apt
```bash
$ sudo apt install samba-common wakeonlan python3
```

## Windows configuration
* You must have a username with a password.
* Open regedit and go to: `\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`.
* create the file DWORD (32 bits): `LocalAccountTokenFilterPolicy` and set its value to `1`.
* Configure your motherboard to wake up with magic packages.

## Configuration file

Change **start-stop.conf** parameters as needed.

You can create more than one machines session.

```text
[LOG]
path=/var/log/start-stop.log

[PC1]
ip=192.168.0.2
username=user
password=pass
mac=00:00:00:00:00:00
time_shutdown=21:00:00
time_wake=07:30:00
day_shutdown=0,1,2,3,4,5,6
day_wake=0,1,2,3,4,5,6
```

# Observation
Wakeonlan doesn't handle machines that are outside the local network very well.