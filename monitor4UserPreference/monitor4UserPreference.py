#!/usr/bin/env python
#-*- coding: utf-8 -*-
from common.logLib import *
from common.msgSend import *
from common.queryUserPreference import *
import time
TM_INTERVAL=60
Exception_INTERVAL=3600
phonenum_list=['18665817689','18665910949','18666662305','13632979619']
msg_content="userPreference:getResponse failed"
cnt=1

while 1:
    status=queryUserPreference()
    if(status == 0 and cnt == 3):
        cnt=0
        time.sleep(TM_INTERVAL)
    elif(status == -1 and cnt ==3):
        logging.error(msg_content+str(cnt)+' times')
        msgSend(phonenum_list,msg_content)
        cnt=0
        time.sleep(Exception_INTERVAL)
    elif(status == -1 and cnt !=3):
        logging.error(msg_content+str(cnt)+' times')
        cnt+=1
        time.sleep(TM_INTERVAL)
    else:
        time.sleep(TM_INTERVAL)

