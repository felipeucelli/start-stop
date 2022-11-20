# -*- coding: utf-8 -*-

# @autor: Felipe Ucelli
# @github: github.com/felipeucelli

# Built-in
import logging
import subprocess
from time import sleep
from datetime import datetime, date


def shutdown(address: list):
    """
    Turn off the machines
    :param address: List with the IP addresses of the machines
    :return:
    """
    try:
        for i in range(len(address)):
            result = subprocess.Popen(
                ['net', 'rpc', 'shutdown', '-I', address[i][0], '-U', address[i][1]],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            result_stdout = result.stdout.read().decode()
            result_stderr = result.stderr.read().decode()

            if result_stdout != '':
                logging.info(f'{result_stdout} - {address[i][0]}')
            else:
                logging.error(f'{result_stderr}')

    except Exception as erro:
        logging.critical(erro)


def wakeonlan(mac: list):
    """
    Turn on the machines using Wake up on Lan
    :param mac: List of macs of machines to be connected
    :return:
    """
    try:
        for i in range(len(mac)):
            result = subprocess.Popen(
                ['wakeonlan', mac[i]],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            result_stdout = result.stdout.read().decode()
            result_stderr = result.stderr.read().decode()

            logging.info(f'{result_stdout}') if result_stdout != '' else logging.error(f'{result_stderr}')

    except Exception as erro:
        logging.critical(erro)


def main(address: list,
         mac: list,
         time_shutdown: list,
         week_shutdown: list,
         time_wakeonlan: list,
         week_wakeonlan: list
         ):
    """
    Checks the time list and calls the corresponding function when it is time
    :param address: List with the IP addresses of the machines
    :param mac: List of macs of machines to be connected
    :param time_shutdown: List of shutdown hours
    :param week_shutdown: List of days of the week to turn off
    :param time_wakeonlan: List with the hours to start the machines
    :param week_wakeonlan: List of days of the week to turn on
    :return:
    """
    while True:
        sleep(1)
        for time1 in time_shutdown:
            now = str(datetime.now().time()).split('.')[0]
            week = date(date.today().year, date.today().month, date.today().day).weekday()
            if now == time1 and week in week_shutdown:
                shutdown(address=address)
        for time2 in time_wakeonlan:
            now = str(datetime.now().time()).split('.')[0]
            week = date(date.today().year, date.today().month, date.today().day).weekday()
            if now == time2 and week in week_wakeonlan:
                wakeonlan(mac=mac)


log_format = '%(asctime)s - %(levelname)s : %(message)s'
log_path = '/var/log/start-stop.log'  # Full path to save the log file
logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format=log_format)

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

if __name__ == '__main__':
    main(address=_address,
         mac=_mac,
         time_shutdown=_time_shutdown,
         week_shutdown=_week_shutdown,
         time_wakeonlan=_time_wakeonlan,
         week_wakeonlan=_week_wakeonlan
         )
