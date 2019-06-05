#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:04:36 2019

@author: oliver
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import os

###set pandas float import precision###
pd.set_option('precision', 5)
###read csv file, creates pandas DataFrame###
data_raw = pd.read_csv(os.getcwd()+'/Data/2019_03_29.txt',header=None,names=['t','pressure','chamber_top','air_top','heater_l','out_top','foil_top','heater_r','valve','out_cross'])
t0 = datetime.strptime(data_raw['t'][0][0:19],'%Y-%m-%d %H:%M:%S')	# start time
ts = np.zeros(len(data_raw['t']))
for idx, dateString in enumerate(data_raw['t']):
    t1 = datetime.strptime(dateString[0:19],'%Y-%m-%d %H:%M:%S')
    td = t1-t0
    ts[idx] = td.total_seconds()/(60*60) #hours


###Ploting###
fig,ax = plt.subplots(2,1,sharex=True)
ax[0].plot(ts,data_raw['air_top'])
ax[0].plot(ts,data_raw['foil_top'])
ax[0].plot(ts,data_raw['chamber_top'])
ax[0].plot(ts,data_raw['valve'])
ax[0].plot(ts,data_raw['heater_r'])
ax[0].plot(ts,data_raw['heater_l'])
ax[0].plot(ts,data_raw['out_top'])
ax[0].plot(ts,data_raw['out_cross'])
ax[0].set_ylabel('temperature (deg)')
ax[0].legend(loc='center left',bbox_to_anchor=(1,0.5))
ax[0].grid()

ax[1].plot(ts,data_raw['pressure'])
ax[1].set_ylabel('pressure (mbar)')
ax[1].set_xlabel('time (hours)')
ax[1].yaxis.set_ticks_position('both')
ax[1].set_yscale("log")

ax[1].grid(which='major')
ax[1].grid(which='minor',color='0.8')



plt.show()



