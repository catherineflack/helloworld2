# Hello World Python Reader App


# 1) set up logging to hw_output.log and establish format

# REFERENCES: 
# https://docs.python.org/3/howto/logging.html
# https://stackoverflow.com/questions/533048/how-to-log-source-file-name-and-line-number-in-python 

import logging
logging.basicConfig(filename='/Users/Catherine.Flack/VScode Workspaces/Hello World Local/hw_output.log',level=logging.DEBUG,format='%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s - %(message)s', datefmt='%H:%M:%S %d/%m/%y')

logging.info('logging enabled')

# 2) try to read file and print contents

# REFERENCE:
# https://www.pythontutorial.net/python-basics/python-read-text-file/#:~:text=To%20read%20a%20text%20file%20in%20Python%2C%20you%20follow%20these,the%20file%20close()%20method.

try:
    with open('/Users/Catherine.Flack/VScode Workspaces/Hello World Local/library/local/helloworld2/hwenvar.env', 'r') as hwfile:
        # read line
        hello_var = hwfile.readline()
        # split result into var name and value list
        split = hello_var.rsplit("=")
        # print list items, stripping trailing spaces
        for item in split:
            print(item.strip())
            # log printing of each item
            logging.info('printing item: ' + item)

# 3) print and log error if expected file not found
except:
    print("Oops! No File found!")
    logging.error('Missing Github File - check Ansible script')
