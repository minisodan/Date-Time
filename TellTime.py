import time
import sys
from datetime import datetime
from time import sleep
from sys import stdout
while True:
   now = datetime.now()
   stdout.write(now.strftime("\r%m/%d/%Y %I:%M:%S")),
   stdout.flush()
   sleep(1)
stdout.write("\n")
