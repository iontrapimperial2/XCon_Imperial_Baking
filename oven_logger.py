# -*- coding: utf-8 -*-
"""
@author: IonTrap/OCorfield
"""

import time
from datetime import datetime

from library.instr_Picolog_TC_08 import Picolog_TC_08
from library.instr_Agilent_XGS600 import XGS600

### define logging function
def oven_log(n):
    "Oven log function. Input file name."

    ### inititialise temp and pressure readers ###
    pressure_reader = XGS600()
    temp_reader = Picolog_TC_08()
    
    ### accepts 50 Hz ###
    temp_reader.set_mains()
    
    ### define and set 10 thermocouple channels ###
    for i in range(10):
        temp_reader.set_channel(i)

    ### define data file as dateString in /p_recording ###
    date_time = 'C:\\Users\\iontrap\\Dropbox\\Imperial Ion Trap\\Oven\\Data\\' + str(n) + '.txt'
    
    
    print('bake recording ctrl_c to stop')
    while(True):
        try:
            data_file = open(date_time,'a+')
            res_P = pressure_reader.read_all_pressures()
            res_T = temp_reader.get_single()
            current_time = datetime.today()
            data_file.write(str(current_time) + ', ' + str(res_P[0]) + ', ' + str(res_T[0])+ ', ' + str(res_T[1]) + ', ' + str(res_T[2]) + ', ' + str(res_T[3]) + ', ' + str(res_T[4]) + ', ' + str(res_T[5]) + ', ' + str(res_T[6]) + ', ' + str(res_T[7]) + '\n')
            data_file.close()
            time.sleep(5)
        except KeyboardInterrupt:
            pressure_reader.close_connection()
            print ('stopped')
            raise
