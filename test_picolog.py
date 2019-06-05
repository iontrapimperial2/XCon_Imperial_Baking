# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
@author: IonTrap/JMHeinrich
"""

import numpy as np
import string
import time
from datetime import datetime

from instr_Picolog_TC_08 import Picolog_TC_08
from instr_Agilent_XGS600 import XGS600

### the filename to save the stuff inside #####################################

date_time = 'C:\\Users\\iontrap\\Dropbox\\Imperial Ion Trap\\Oven\\Data\\2019_03_22.txt'



### INITIALIZE THE TEMPERATURE READING ########################################

Temp_Reader = Picolog_TC_08()

Temp_Reader.set_mains()

channels = np.arange(10)

for i in range(len(channels)):
    Temp_Reader.set_channel(channels[i])
    


### INITIALIZE THE PRESSURE READING ###########################################

Pressure_Reader = XGS600()

x = 1
while x == 1:
    data_file = open(date_time,'a+')
    
    res_P = Pressure_Reader.read_all_pressures()
    res_T = Temp_Reader.get_single()
    
    data_file.write(str(datetime.today()) + ', ' + str(res_P[0]) + ', ' + str(res_T[0])+ ', ' + str(res_T[1]) + ', ' + str(res_T[2]) + ', ' + str(res_T[3]) + ', ' + str(res_T[4]) + ', ' + str(res_T[5]) + ', ' + str(res_T[6]) + ', ' + str(res_T[7]) + '\n')
    data_file.close()
    
    time.sleep(5)
    










