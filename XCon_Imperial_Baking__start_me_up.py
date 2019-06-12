# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 17:29:59 2018

@author: IonTrap/JMHeinrich
"""

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
import pyqtgraph as pg
import csv
import numpy as np
#import matplotlib as plt
#from date_axis_item import DateAxisItem
from datetime import datetime
import time
import threading
from os import path as p

from XCon_Imperial_Baking_gui import Ui_XCon_Imperial_Baking

#from library.d_instr_Picolog_TC_08 import Picolog_TC_08
#from library.d_instr_Agilent_XGS600 import XGS600

from library.instr_Picolog_TC_08 import Picolog_TC_08
from library.instr_Agilent_XGS600 import XGS600


brush_background = (255,255,255,255)

blueBrush = (109,123,205,255)
blueBrush_alpha = (109,123,205,100)
bluePen = pg.mkPen(color = blueBrush, width = 2)

redBrush = (209,111,111,255)
redBrush_alpha = (209,111,111,100)
redPen = pg.mkPen(color = redBrush, width = 2)

blackBrush = (0,0,0,255)
blackPen = pg.mkPen(color = blackBrush, width = 2) 

aquaBrush = (0,255,255)
aquaPen = pg.mkPen(color = aquaBrush, width = 2) 

bluevioletBrush = (138,43,226)
bluevioletPen = pg.mkPen(color = bluevioletBrush, width = 2) 

chartreuseBrush = (102,205,0)
chartreusePen = pg.mkPen(color = chartreuseBrush, width = 2) 

chocolateBrush = (139,69,19)
chocolatePen = pg.mkPen(color = chocolateBrush, width = 2) 

goldBrush = (255,215,0)
goldPen = pg.mkPen(color = goldBrush, width = 2) 

labelstyle_L = {'color': '#000', 'font-size': '12pt'}


flag = True
class window(Ui_XCon_Imperial_Baking):
    
    def __init__(self, dialog):
        Ui_XCon_Imperial_Baking.__init__(self)
        self.setupUi(dialog)

        self.filename = ''
        self.filename1 = ''
        self.flag = True
        
        self.pushButton_browse.clicked.connect(self.browse_data)
        self.pushButton_Browse1.clicked.connect(self.browse_data1)
        self.pushButton_import.clicked.connect(self.update_data)
        self.pushButton_Start.clicked.connect(self.start_oven_logger)
        self.pushButton_Stop.clicked.connect(self.stop_oven_logger)
        
        self.lineEdit_ch_1.setText('')
        self.lineEdit_ch_2.setText('')
        self.lineEdit_ch_3.setText('')
        self.lineEdit_ch_4.setText('')
        self.lineEdit_ch_5.setText('')
        self.lineEdit_ch_6.setText('')
        self.lineEdit_ch_7.setText('')
        self.lineEdit_ch_8.setText('')
    
        self.time = None
        self.p = None
        self.T_channels = None
        

        #---------------------------------------------------------------------#
        #--- PLOTS, PUSH BUTTONS AND TIMERS FOR TEMPERATURE ------------------#
        #---------------------------------------------------------------------#        
        self.plot_temp = pg.PlotWidget(name = 'widget_plot_temp')
        self.plot_temp.setBackground(background = brush_background)
        self.plot_temp.setLabel('left', 'T', units = '[Celsius]', **labelstyle_L)
        self.plot_temp.setLabel('bottom', 'time', units = '', **labelstyle_L)
        self.plot_temp.showGrid(x = True, y = True)
        
#        axis = DateAxisItem(orientation='bottom')
#        axis.attachToPlotItem(self.plot_temp.getPlotItem())
        
        self.verticalLayout_temp.addWidget(self.plot_temp)
        #---------------------------------------------------------------------#
        
        #---------------------------------------------------------------------#
        self.timer_data = QtCore.QTimer()
        self.timer_data.setInterval(2000)
        self.timer_data.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer_data.timeout.connect(self.import_data)
        #---------------------------------------------------------------------#



        #---------------------------------------------------------------------#
        #--- PLOTS, PUSH BUTTONS AND TIMERS FOR PRESSURE ---------------------#
        #---------------------------------------------------------------------#        
        self.plot_pressure = pg.PlotWidget(name = 'widget_plot_pressure')
        self.plot_pressure.setBackground(background = brush_background)
        self.plot_pressure.setLabel('left', 'p', units = '[mbar]', **labelstyle_L)
        self.plot_pressure.setLabel('bottom', 'time', units = '', **labelstyle_L)
        self.plot_pressure.showGrid(x = True, y = True)
        self.plot_pressure.setLogMode(x=None, y=True)
        
        self.verticalLayout_pressure.addWidget(self.plot_pressure)
        #---------------------------------------------------------------------#
        
        #---------------------------------------------------------------------#
        self.timer_plot_data = QtCore.QTimer()
        self.timer_plot_data.setInterval(2000)
        self.timer_plot_data.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer_plot_data.timeout.connect(self.t_plots)
        self.timer_plot_data.start()
        #---------------------------------------------------------------------#  
    
    
    
    ###########################################################################
    ### FUNCTIONS DATA SELECTION ##############################################
    ###########################################################################  

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def browse_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog    
        self.filename_monitoring, _ = QFileDialog.getOpenFileName(None,"import data", "","all files (*);; asc files (*.asc);; txt files (*.txt)", options=options)
        
        if self.filename_monitoring:
            self.lineEdit_data.setText(self.filename_monitoring)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def browse_data1(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog    
        self.filename_save, _ = QFileDialog.getSaveFileName(None,"save data", "","all files (*);; asc files (*.asc);; txt files (*.txt)", options=options)
        
        if self.filename_save:
            self.lineEdit_savefile.setText(self.filename_save)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
    #~~~ start and stop oven_logger ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def start_oven_logger(self):
        self.flag = True
        
        
        a = self.lineEdit_savefile.text()
        b = a.rfind('/')
        c = a[:(b+1)]
        d = a.rfind('.')
        save_path = str(c)
        if d == -1:
            e = a[(b+1):]
            self.save_label(e,save_path)
            self.start_oven_thread(e)
        else:
            e = a[(b+1):d]
            self.save_label(e,save_path)
            self.start_oven_thread(e)
    
    
    def stop_oven_logger(self):
        self.flag = False
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    
    
    def save_label(self, n,s):
        current_time = datetime.today()
        file_name = p.join(s, 'Channel labels ' + str(n)+".txt")
        data_file = open(file_name,'a+') 
        data_file.write('\n ' + str(current_time) + '\n ' + 'Channel 1: ' + str(self.lineEdit_ch1in.text()) + '\n '+ 
                    'Channel 2: ' + str(self.lineEdit_ch2in.text()) + '\n '+ 'Channel 3: ' + str(self.lineEdit_ch3in.text()) + '\n '+
                    'Channel 4: ' + str(self.lineEdit_ch4in.text()) + '\n '+ 'Channel 5: ' + str(self.lineEdit_ch5in.text()) + '\n '+
                    'Channel 6: ' + str(self.lineEdit_ch6in.text()) + '\n '+ 'Channel 7: ' + str(self.lineEdit_ch7in.text()) + '\n '+
                    'Channel 8: ' + str(self.lineEdit_ch8in.text()) + '\n ')
        data_file.close()
        
    
    def start_oven_thread(self, n):
        start_ovenlog = threading.Thread(target = self.oven_log, args=[n])
        start_ovenlog.start()
             
        
        

    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def import_data(self):
        ### read filename
        self.filename = str(self.lineEdit_data.text())

        ### load and prepare data
        try:
            self.import_txt_file(self.filename)
        except FileNotFoundError:
            print('nothing found to that name')
        except UnicodeDecodeError:
            print('not a suitable file format selected')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def import_labels(self):
        ### read filename
        a = self.lineEdit_data.text()
        b = a.rfind('/')
        c = a.rfind('.')
        d = a[(b+1):c]
        e = a[:(b+1)]
        self.filename1 = str(e) + 'Channel labels ' + str(d) + '.txt'

        ### load and prepare data
        try:
            self.import_txt_file1(self.filename1)
        except FileNotFoundError:
            print('nothing found to that name')
        except UnicodeDecodeError:
            print('not a suitable file format selected')
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
       
    #~~~ import txt file with monitoring of parameters ~~~~~~~~~~~~~~~~~~~~~~~#
    def import_txt_file(self,filename):
        
        ### read the file
        with open(filename) as inputfile:
            data_import = list(csv.reader(inputfile))
#        print(data_import)
#        print(data_import[0])
#        print(data_import[0][0])
        
        ### format the data into an array of floats
#        time = [data_import[i][0] for i in range(len(data_import))]
        time_ = [time.mktime(datetime.strptime(data_import[i][0][:-7], '%Y-%m-%d %H:%M:%S').timetuple()) for i in range(len(data_import))]
        
        p = [float(data_import[i][1]) for i in range(len(data_import))]
        
        T_channels = []
        for j in range(2,10):
            T_channel = [float(data_import[i][j]) for i in range(len(data_import))]
            T_channels.append(T_channel)
            
#        print(T_channels[3])
        self.time = time_
        
#        now = time.time()
#        timestamps = np.linspace(now - len(p), now, len(p))
#        self.time = timestamps
        
        self.p = p
        self.T_channels = T_channels
        
#        print(self.time)        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    #~~~ import txt file with channel labels ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def import_txt_file1(self,filename):
        
        ### read the file
        with open(filename) as inputfile:
            data_import = list(csv.reader(inputfile))
            self.lineEdit_ch_1.setText(str(data_import[2])[14:-2])
            self.lineEdit_ch_2.setText(str(data_import[3])[14:-2])
            self.lineEdit_ch_3.setText(str(data_import[4])[14:-2])
            self.lineEdit_ch_4.setText(str(data_import[5])[14:-2])
            self.lineEdit_ch_5.setText(str(data_import[6])[14:-2])
            self.lineEdit_ch_6.setText(str(data_import[7])[14:-2])
            self.lineEdit_ch_7.setText(str(data_import[8])[14:-2])
            self.lineEdit_ch_8.setText(str(data_import[9])[14:-2])
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def update_data(self):
        
        if self.radioButton_monitoring.isChecked() == True:
            #-----------------------------------------------------------------#
            self.timer_data.start()

            
            #-----------------------------------------------------------------#
        else:
            try:
                print('s')
                self.timer_data.stop()
            except:
                pass
        self.import_data()
        self.import_labels()
        self.t_plots()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    def t_plots(self):

        try:               
            x = np.arange(len(self.time))
        except Exception:
            pass
        
        try:                
            self.plot_pressure.plot(x,self.p ,pen = bluePen, symbol = 'o', symbolBrush = blackBrush, name = 'pressure', clear = True)
        except Exception:
            pass
        if self.radioButton_ch_1.isChecked() == True:
            try:               
               self.plot_temp.plot(x,self.T_channels[0] ,pen = bluePen, symbol = 'o', symbolBrush = blueBrush, name = 'ch_1', clear = True)
            except Exception:
                #pass
                print('eh')
            
        if self.radioButton_ch_2.isChecked() == True:
            try:               
                self.plot_temp.plot(x,self.T_channels[1] ,pen = redPen, symbol = 'o', symbolBrush = redBrush, name = 'ch_2')
            except Exception:
                #pass
                print('eh1')       
        
        if self.radioButton_ch_3.isChecked() == True:
            try:               
                self.plot_temp.plot(x,self.T_channels[2] ,pen = aquaPen, symbol = 'o', symbolBrush = aquaBrush, name = 'ch_3')
            except Exception:
                #pass
                print('eh2')
         
        if self.radioButton_ch_4.isChecked() == True:
            try:               
                self.plot_temp.plot(x,self.T_channels[3] ,pen = bluevioletPen, symbol = 'o', symbolBrush = bluevioletBrush, name = 'ch_4')
            except Exception:
                #pass
                print('eh3')
            
        if self.radioButton_ch_5.isChecked() == True:
            try:               
                self.plot_temp.plot(x,self.T_channels[4] ,pen = chartreusePen, symbol = 'o', symbolBrush = chartreuseBrush, name = 'ch_5')
            except Exception:
                #pass
                print('eh4')   
         
        if self.radioButton_ch_6.isChecked() == True:
            try:               
                self.plot_temp.plot(x,self.T_channels[5] ,pen = blackPen, symbol = 'o', symbolBrush = blackBrush, name = 'ch_6')
            except Exception:
                #pass
                print('eh5')
         
        if self.radioButton_ch_7.isChecked() == True:
            try:               
                self.plot_temp.plot(x,self.T_channels[6] ,pen = chocolatePen, symbol = 'o', symbolBrush = chocolateBrush, name = 'ch_7')
            except Exception:
                #pass
                print('eh6')   
         
        if self.radioButton_ch_8.isChecked() == True:
            try:               
                self.plot_temp.plot(x,self.T_channels[7] ,pen = goldPen, symbol = 'o', symbolBrush = goldBrush, name = 'ch_8')
            except Exception:
                #pass
                print('eh7')      
                
#            time_plot = []
#            for i in range(len(self.time)):
#                time_plot.append(time.mktime(datetime.datetime.now().timetuple()))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
    #~~~ define logging function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def oven_log(self, n):
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
        a = self.lineEdit_savefile.text()
        b = a.rfind('/')
        c = a[:(b+1)]
        d = n.rfind('.')

        save_path = str(c)
        
        #date_time = p.join(save_path, str(n)+".txt")
        
        
        while self.flag == True:
            res_P = pressure_reader.read_all_pressures()
            res_T = temp_reader.get_single()
            current_time = datetime.today()
            if d == -1:
                date_time = p.join(save_path, str(n)+".txt")
                data_file = open(date_time,'a+')
                data_file.write(str(current_time) + ', ' + str(res_P[0]) + ', ' + str(res_T[0])+ ', ' + str(res_T[1]) + ', ' + str(res_T[2]) + ', ' + str(res_T[3]) + ', ' + str(res_T[4]) + ', ' + str(res_T[5]) + ', ' + str(res_T[6]) + ', ' + str(res_T[7]) + '\n')
                data_file.close()
                time.sleep(5)
            else:
                e = n[:d]

                date_time = p.join(save_path,  + str(e) + ".txt")
                data_file = open(date_time,'a+')
                data_file.write(str(current_time) + ', ' + str(res_P[0]) + ', ' + str(res_T[0])+ ', ' + str(res_T[1]) + ', ' + str(res_T[2]) + ', ' + str(res_T[3]) + ', ' + str(res_T[4]) + ', ' + str(res_T[5]) + ', ' + str(res_T[6]) + ', ' + str(res_T[7]) + '\n')
                data_file.close()
                time.sleep(30)
                
                

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
      
    
    


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    dialog_lc = QtWidgets.QMainWindow()
    
    programm_lc = window(dialog_lc)
    dialog_lc.show()
    
    sys.exit(app.exec_())