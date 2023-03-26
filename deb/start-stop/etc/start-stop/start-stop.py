# -*- coding: utf-8 -*-

# @autor: Felipe Ucelli
# @github: github.com/felipeucelli

# Built-in
import logging
import subprocess
import configparser
from time import sleep
from datetime import datetime, date


def shutdown(ip: str, username: str, password: str):
    """
    Turn off the machines
    :return:
    """
    try:
        result = subprocess.Popen(
            ['net', 'rpc', 'shutdown', '-I', ip, '-U', username + '%' + password],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        result_stdout = result.stdout.read().decode()
        result_stderr = result.stderr.read().decode()

        if result_stdout != '':
            logging.info(f'{result_stdout} - {ip}')
        else:
                logging.error(f'{result_stderr}')

    except Exception as error:
        logging.critical(error)


def wakeonlan(mac: str):
    """
    Turn on the machines using Wake up on Lan
    :param mac: List of macs of machines to be connected
    :return:
    """
    try:
        result = subprocess.Popen(
            ['wakeonlan', mac],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        result_stdout = result.stdout.read().decode()
        result_stderr = result.stderr.read().decode()

        logging.info(f'{result_stdout}') if result_stdout != '' else logging.error(f'{result_stderr}')

    except Exception as error:
        logging.critical(error)


def main(section: list):
    """
    Checks the time list and calls the corresponding function when it is time

    :return:
    """
    while True:
        now = str(datetime.now().time()).split('.')[0]
        day = str(date(date.today().year, date.today().month, date.today().day).weekday())
        sleep(1)
        for items in section:
            item = dict(config.items(items))
            if now in item['time_shutdown'] and day in item['day_shutdown']:
                shutdown(item['ip'], item['username'], item['password'])

            if now in item['time_wake'] and day in item['day_wake']:
                wakeonlan(item['mac'])



config = configparser.RawConfigParser()
config.read('/etc/start-stop/start-stop.conf')

log_format = '%(asctime)s - %(levelname)s : %(message)s'
log_path = config.get('LOG', 'path')

logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format=log_format)

if __name__ == '__main__':
    main(list(config.sections()[1:]))
