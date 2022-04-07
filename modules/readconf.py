#!/usr/bin/python 

import configparser
import sys


def readconf():
    Config = configparser.ConfigParser()
    try:
        Config.read('config.ini')
    except:
        print('Read config.ini error')
        sys.exit(1)

    ini_dict = {}
    for section in Config.sections():
        for option in Config.options(section):
            vals = Config.get(section, option)
            dict_vals = dict(x.split('=') for x in vals.split(','))
            ini_dict[option] = dict_vals
    return ini_dict

if __name__ == '__main__':
    conf = readconf()
    print(conf)
