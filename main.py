#!/usr/bin/python
# -*- coding:utf-8 -*-

import server
import argparse
import configparser


def evaluate_args():
    parser = argparse.ArgumentParser(description="Help of arguments used by the serverside of nao!")
    # Add arguments here
    parser.add_argument("--r", action="store_true", help="Run the server!")
    parser.add_argument("--i", action="store_true", help="Import template data into database!")

    # Check for arguments and do stuff with it
    args = parser.parse_args()
    if args.i:
        print("t1")
    if args.r:
        run_server()


def run_server():
    config = configparser.ConfigParser()
    config.read("config.ini")
    server.app.run(host=config.get('server', 'host'), port=config.get('server', 'port'))


if __name__ == '__main__':
    evaluate_args()
    print("Skript done!")
