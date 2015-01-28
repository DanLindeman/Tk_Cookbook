import os, logging, sys

logging.basicConfig(filename='example.log',level=logging.INFO, filemode='w')

num_errors = 0
for eachfile in os.listdir('.'):
    if eachfile == 'log_runner.py':
        continue
    with open(eachfile, 'r') as myFile:
            lines = myFile.readlines()
            for line in lines:
                if ('Bad Text' in line) or ('Some Other Shiz' in line):
                    num_errors += 1
    if num_errors > 0:
        logging.info("Found {0} error(s) in {1}".format(num_errors, eachfile))
    num_errors = 0
