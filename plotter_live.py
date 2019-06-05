#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:04:36 2019

@author: oliver
"""
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.animation as animation


###set pandas float import precision###

pd.set_option('precision', 5)
fig,ax = plt.subplots(2,1,sharex=True)

###read csv file, creates pandas DataFrame###
data_raw = pd.read_csv(os.getcwd()+'/Data/2019_05_14.txt',header=None,names=['t','pressure','chamber_top','air_top','heater_l','out_top','foil_top','heater_r','chamber_base','out_cross'])
t0 = datetime.strptime(data_raw['t'][0][0:19],'%Y-%m-%d %H:%M:%S')	# start time
ts = np.zeros(len(data_raw['t']))
for idx, dateString in enumerate(data_raw['t']):
    t1 = datetime.strptime(dateString[0:19],'%Y-%m-%d %H:%M:%S')
    td = t1-t0
    ts[idx] = td.total_seconds()/(60*60) #hours
    
y1, = ax[0].plot(ts,data_raw['air_top'])
y2, = ax[0].plot(ts,data_raw['foil_top'])
y3, = ax[0].plot(ts,data_raw['chamber_top'])
y4, = ax[0].plot(ts,data_raw['chamber_base'])
y5, = ax[0].plot(ts,data_raw['heater_r'])
y6, = ax[0].plot(ts,data_raw['heater_l'])
y7, = ax[0].plot(ts,data_raw['out_top'])
y8, = ax[0].plot(ts,data_raw['out_cross'])
z1, = ax[1].plot(ts,data_raw['pressure'])
    
### initialization function: plot the background of each frame
def init():
    ###Ploting###
    ax[0].set_ylabel('temperature (deg)')
    ax[0].legend(loc='center left',bbox_to_anchor=(1,0.5))
    ax[0].grid()
    ax[1].set_ylabel('pressure (mbar)')
    ax[1].set_xlabel('time (hours)')
    ax[1].yaxis.set_ticks_position('both')
    ax[1].set_yscale("log")
    ax[1].grid(which='major')
    ax[1].grid(which='minor',color='0.8')
    return y1,y2,y3,y4,y5,y6,y7,y8,z1,ax[0],ax[1]

### animation function.  This is called sequentially
def animate(i):
    global ts,data_raw
    data_update = pd.read_csv(os.getcwd()+'/Data/update.txt',header=None,names=['t','pressure','chamber_top','air_top','heater_l','out_top','foil_top','heater_r','chamber_base','out_cross']) 
    ts_new = np.zeros(len(data_update['t']))
    time_last = ts[len(ts)-1]
    new_data = 0
    for idx, dateString in enumerate(data_update['t']):
        t1_new = datetime.strptime(dateString[0:19],'%Y-%m-%d %H:%M:%S')
        td_new = t1_new-t0
        ts_new[idx] = td_new.total_seconds()/(60*60) #hours
        if ts_new[idx] > time_last:
            data_raw = data_raw.append(data_update)
            ts = np.append(ts,ts_new[idx])
            new_data = 1
            
    if new_data == 1:
        ###Ploting###
        y1.set_data(ts,data_raw['air_top'])
        y2.set_data(ts,data_raw['foil_top'])
        y3.set_data(ts,data_raw['chamber_top'])
        y4.set_data(ts,data_raw['chamber_base'])
        y5.set_data(ts,data_raw['heater_r'])
        y6.set_data(ts,data_raw['heater_l'])
        y7.set_data(ts,data_raw['out_top'])
        y8.set_data(ts,data_raw['out_cross'])
        z1.set_data(ts,data_raw['pressure'])
        ax[0].relim()
        ax[0].autoscale_view(True,True,True)
        ax[1].relim()
        ax[1].autoscale_view(True,True,True)
                
    return y1,y2,y3,y4,y5,y6,y7,y8,z1,ax[0],ax[1]
    
ani = animation.FuncAnimation(fig,animate,init_func=init,interval=3000)



plt.show()



