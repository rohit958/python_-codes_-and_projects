# testing log files and adding random numbers 
import logging
import sys
import random 

logging.basicConfig(filename='D:\python_ codes_ and_projects\logfile.log',format="{asctime} {levelname:<8} {message}", style="{", encoding='UTF-8',level=logging.DEBUG)


a=random.randint(0,10) 
b=random.randint(10,15)

def add_num(p,q):
    s=p+q
    return s

test= add_num(a,b)
logging.debug('add: {} + {} = {}'.format(a, b, test))
logging.info('code exceuted successfully!')
