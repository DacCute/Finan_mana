import numpy as np
import pandas as pd
import datetime
import sys
from openpyxl import *
import subprocess
from AddAccessHistory import *

# file address
file_path = "./Data.xlsx"

# &Instruction function
def Instruction():
    print("""
--------------------------------------------
Type 1 to add Transaction
     2 to
     3 to 
     End to finish.
--------------------------------------------
          """)

# ?Input task function
def InputTask():
    task = str(input('Telling what to do: '))
    task = task.upper()

# ^Get Time
def GetTime():
    current_time = datetime.datetime.now()

# ^Add transaction funtion
def AddTrans():
    print('dob')

def AddAccessHistory():
    subprocess.run(["python", "./AddAccessHistory.py"])



# ^import file
tran = pd.read_excel(file_path,
                     sheet_name=['Transaction'])

# ^Time access
current_time = datetime.datetime.now()
AddAccessHistory

# ^Hello script
print('''WELLCOME TO CALCULATION TRANSACTION SYSTEMS!
--------------------------------------------
Current time is:''',current_time,
'\n--------------------------------------------')

# !Program work here!
Instruction()
count = 0
while True:
    #task = str(input('Telling what to do: '))
    #task = task.upper()
    task = 'END'
    if task == 'END':
        break
    else:
        count +=1

GetTime()

print('--------------------------------------------',
      '\nEND TASK AT:  ',current_time,
      '\n\n  ', count, 'task have done\n',
      '\n--------------------------------------------'
      )