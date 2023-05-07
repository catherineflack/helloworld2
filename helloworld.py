# Hello World Python Reader App


# 1) set up logging to hw_output.json and establish format

# REFERENCES: 
# https://docs.python.org/3/howto/logging.html
# https://stackoverflow.com/questions/533048/how-to-log-source-file-name-and-line-number-in-python 

from cgitb import handler
import logging
from pyexpat.errors import messages
# https://www.elastic.co/guide/en/cloud/current/ec-getting-started-search-use-cases-python-logs.html
import ecs_logging
import time

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('/home/ubuntu/helloworld/hw-git-copy/hw_output.json')
handler.setFormatter(ecs_logging.StdlibFormatter())
logger.addHandler(handler)

logger.info('logging enabled')

# 2) try to read file and print contents

# REFERENCE:
# https://www.pythontutorial.net/python-basics/python-read-text-file/#:~:text=To%20read%20a%20text%20file%20in%20Python%2C%20you%20follow%20these,the%20file%20close()%20method.

run = 0
while run < 6:
    run +=1
    try:
        with open('/home/ubuntu/helloworld/hw-git-copy/hwenvar.env', 'r') as hwfile:
            # read line
            hello_var = hwfile.readline()
            logger.info('reading file')
            # split result into var name and value list
            split = hello_var.rsplit("=")
            logger.debug('splitting variables')
            # print list items, stripping trailing spaces
            for item in split:
                print(item.strip())
                # log printing of each item
                logger.info('printing item: ' + item)

    # 3) print and log error if expected file not found
    except:
        print("Oops! No File found!")
        logger.error('Missing Github File - check Ansible script')
