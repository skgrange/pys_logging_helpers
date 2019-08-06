# Load modules
import time, datetime, pytz
from math import floor
import gc
import os

# Function to sleep until the start of the next minute. 
# 
# Used for clean starting of log files.
def nice_starter(verbose = True):
  
  # Get time
  date_run = datetime.datetime.utcnow()
  
  # Get time to start
  date_to_start = 60 - (date_run.second + date_run.microsecond / 1000000.0)
  
  if verbose:
    print(str(date_unix(integer = True)) + \
      ': Waiting until the beginning of the next minute (' + \
      str(int(date_to_start)) + 
      ' seconds) before starting logging...')
    
  # Sleep until future
  time.sleep(date_to_start)


# Function to sleep until the next clean time period. 
#
# Used at the end of a process. 
def nice_waiter(frequency):
  
  # Find current time
  date_now = time.time()
  
  # When should the need iteration be? 
  date_next = floor(date_now) + int(frequency)
  
  # Find the time to wait
  seconds_to_wait = date_next - time.time()
  
  # Ensure date is nice and clean, if not fix it
  date_modulo = date_next % int(frequency)
  
  if date_modulo == 0:
    pass
  else:
    # Reassign to clean date
    date_next = date_next - date_modulo

  seconds_to_wait = date_next - time.time()
  
  # Sleep until the clean time
  time.sleep(seconds_to_wait)


def housekeeping():
  # Garbage collection, once an hour
  if datetime.datetime.fromtimestamp(time.time()).minute % 15 == 0:
    gc.collect()
  else:
    pass  


def date_unix(integer = False):

  # Get date
  date = time.time()

  # Data type
  if integer: 
    date = floor(date)
    date = int(date)
  else:	  
    pass

  return date


def date_message():
  
  # Get date
  date = date_unix()
  
  # To string
  date = datetime.datetime.utcfromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S UTC')
  date = date + ': '
  
  return date


def create_directory(directory): 
  if not os.path.exists(directory):
    os.makedirs(directory)
  else: 
    pass
