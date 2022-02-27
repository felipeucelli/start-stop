# -*- coding: utf-8 -*-

# @autor: Felipe Ucelli
# @github: github.com/felipeucelli

# Built-in
import logging
import subprocess
from time import sleep
from datetime import datetime


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


def main(address: list, mac: list, time_shutdown: list, time_wakeonlan: list):
    """
    Checks the time list and calls the corresponding function when it is time
    :param address: List with the IP addresses of the machines
    :param mac: List of macs of machines to be connected
    :param time_shutdown: List of shutdown hours
    :param time_wakeonlan: List with the hours to start the machines
    :return:
    """
    while True:
        sleep(1)
        for time1 in time_shutdown:
            now = str(datetime.now().time()).split('.')[0]
            if now == time1:
                shutdown(address=address)
        for time2 in time_wakeonlan:
            now = str(datetime.now().time()).split('.')[0]
            if now == time2:
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

# Wake up on lan time
_time_wakeonlan = [
    '21:30:00',
    '07:30:00'
]

if __name__ == '__main__':
    main(address=_address, mac=_mac, time_shutdown=_time_shutdown, time_wakeonlan=_time_wakeonlan)
