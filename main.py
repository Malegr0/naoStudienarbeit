#!/usr/bin/python
# -*- coding:utf-8 -*-

import server
import argparse
import configparser

import weighting


def evaluate_args():
    parser = argparse.ArgumentParser(description="Help of arguments used by the serverside of nao!")
    # Add arguments here
    parser.add_argument("-r", action="store_true", help="Run the server!")
    parser.add_argument("-i", action="store_true", help="Checks if the required table are present in the database, "
                                                        "clears them and then imports the template data into the "
                                                        "database!")

    # Check for arguments and do stuff with it
    args = parser.parse_args()
    if args.i:
        print("t1")
    if args.r:
        run_server()
    if not (args.i and args.r):
        print("Use -h to get help with the arguments!")


def run_server():
    config = configparser.ConfigParser()
    config.read("config.ini")
    server.app.run(host=config.get('server', 'host'), port=config.get('server', 'port'))


if __name__ == '__main__':
    keyword = ['Informatik', 'Studium', 'was', 'für', 'in', 'Informatik', 'HWR', 'wer', 'wo', 'Standort', 'Studium']
    weighting.calculate_weight(keyword)
    # evaluate_args()
    print("Skript done!")
