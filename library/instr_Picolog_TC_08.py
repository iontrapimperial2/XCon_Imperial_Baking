# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 15:01:39 2019

@author: IonTrap/JMHeinrich
"""

import ctypes
import time


class Picolog_TC_08(object):
    
    def __init__(self):
        
        ''' loads the dll-library of the temperature logger ''' 
        self.dll_TC = ctypes.windll.LoadLibrary("C:\\Program Files\\Pico Technology\\PicoLog 6\\usbtc08.dll")
        
        
        ''' this routine returns a valid handle to the USB TC-08 if the driver
            successfully opens it '''
        self.device = self.dll_TC.usb_tc08_open_unit()
        
        self.dll_TC.usb_tc08_set_channel.argtypes = [ctypes.c_int16,ctypes.c_int16,ctypes.c_int8]
        
        self._temp=(ctypes.c_float *9)()
        self._overflow_flags=ctypes.c_int16()
        self._units = ctypes.c_int16(0)




    def set_mains(self):        
        ''' this routine sets the USB TC-08 to reject either 50 or 60 Hz - 
            here it is set to reject the 60Hz '''
            
        self.dll_TC.usb_tc08_set_mains(self.device, 50)


    
    def set_channel(self, channel):
        ''' call this routine once for each channel that you want to use. you
            can do this any time after calling usb_tc08_open_unit. by default,
            all channels are disabled. '''
        
        tc_type = ord('K')

        self.dll_TC.usb_tc08_set_channel(self.device, channel, tc_type)


    def get_single(self):
        ''' you must set up the channels before calling this function. you must
            not have put the unit into streaming mode with usb_tc08_run, as
            this will cause usb_tc08_get_single to fail. '''
        
        self.dll_TC.usb_tc08_get_single(self.device, ctypes.byref(self._temp), ctypes.byref(self._overflow_flags), self._units)
        
#        time.sleep(5)
        
        return [self._temp[1],self._temp[2],self._temp[3],self._temp[4],self._temp[5],self._temp[6],self._temp[7],self._temp[8]]

    def stop(self):
        self.dll_TC.usb_tc08_close_unit(self.device)