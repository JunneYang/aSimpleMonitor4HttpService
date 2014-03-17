#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging

LogFilePath="./log/monitorUserPreference.log"
logging.basicConfig(level=logging.ERROR,
                format='[%(levelname)s] [%(asctime)s] [%(filename)s-line:%(lineno)d] [%(funcName)s-%(threadName)s] %(message)s',
                datefmt='%a,%Y-%m-%d %H:%M:%S',
                filename=LogFilePath,
                filemode='w')


if __name__ == "__main__":
    logging.debug("HelloWorld")
