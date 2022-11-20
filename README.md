# start-stop
A simple script that turns Windows machines off and on automatically
 
## Description
The script was built to run inside a linux machine for shutdown and wake up Windows machines on the local network.

## Quickstart
This guide covers faster script usage.

### Installation
start-stop requires an installation of Python3 or greater. And run on a linux machine with some packages installed

Installing samba package with apt
```bash
$ sudo apt install samba
```

Installing wakeonlan package with apt
```bash
$ sudo apt install wakeonlan
```

### Windows configuration
* You must have a username with a password
* Open regedit and go to: `\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`
* create the file DWORD (32 bits): `LocalAccountTokenFilterPolicy` and set its value to `1`
* Configure your motherboard to wake up with magic packages

### Configuring the script
It is necessary to configure the script before starting to use it.

Edit the parameters below as per your need
```python
# IP address and username and password of Windows machines
# Username and password syntax: 'username%password'
_address = [
    ('192.168.0.105', 'user1%password1'),
    ('192.168.0.106', 'user2%password2')
]

# MAC address of Windows machines
_mac = [
    '00:00:00:00:00:00',
    '11:11:11:11:11:11'
]

# Shutdown time
_time_shutdown = [
    '21:00:00',
    '22:00:00'
]

# Monday: 0, Tuesday: 1, Wednesday: 2, Thursday: 3, Friday: 4, Saturday: 5, Sunday: 6
_week_shutdown = [
    0,  # Monday
    1,  # Tuesday
    2,  # Wednesday
    3,  # Thursday
    4,  # Friday
    5,  # Saturday
    6,  # Sunday
]

# Wake up on lan time
_time_wakeonlan = [
    '21:30:00',
    '07:30:00'
]

# Monday: 0, Tuesday: 1, Wednesday: 2, Thursday: 3, Friday: 4, Saturday: 5, Sunday: 6
_week_wakeonlan = [
    0,  # Monday
    1,  # Tuesday
    2,  # Wednesday
    3,  # Thursday
    4,  # Friday
    5,  # Saturday
    6,  # Sunday
]
```

## Observation
wakeonlan doesn't handle machines that are outside the local network very well.