#!/usr/bin/python
#-*- coding:utf-8 -*-

import server

if __name__ == '__main__':
    server.app.run(host='0.0.0.0', port=5050)
    print("Successfully executed!")
