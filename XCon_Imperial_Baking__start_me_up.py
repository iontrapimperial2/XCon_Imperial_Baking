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
import matplotlib as plt
from date_axis_item import DateAxisItem
from datetime import datetime
import time

#from XCon_Imperial_main import laser_control
from XCon_Imperial_Baking_gui import Ui_XCon_Imperial_Baking


brush_background = (255,255,255,255)

blueBrush = (109,123,205,255)
blueBrush_alpha = (109,123,205,100)
bluePen = pg.mkPen(color = blueBrush, width = 2)

redBrush = (209,111,111,255)
redBrush_alpha = (209,111,111,100)
redPen = pg.mkPen(color = redBrush, width = 2)

blackBrush = (0,0,0,255)
blackPen = pg.mkPen(color = blackBrush, width = 2) 

labelstyle_L = {'color': '#000', 'font-size': '12pt'}



class window(Ui_XCon_Imperial_Baking):
    
    def __init__(self, dialog):
        Ui_XCon_Imperial_Baking.__init__(self)
        self.setupUi(dialog)

        self.filename = ''

        self.pushButton_browse.clicked.connect(self.browse_data)  
        self.pushButton_import.clicked.connect(self.update_data)
        self.pushButton_save_ch_input.clicked.connect(self.save_channel_input)
        
        self.time = None
        self.p = None
        self.T_channels = None
        

        #---------------------------------------------------------------------#
        #--- PLOTS, PUSH BUTTONS AND TIMERS FOR PRESSURE ---------------------#
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
#
#        #---------------------------------------------------------------------#   
#        self.pushButton_lock_laser_blue_1_on.clicked.connect(self.pushButton_lock_laser_blue_1_on_clicked)
#        self.pushButton_lock_laser_blue_1_off.clicked.connect(self.pushButton_lock_laser_blue_1_off_clicked)
#        
#        self.pushButton_smooth_change_laser_blue_1_start.clicked.connect(self.pushButton_smooth_change_laser_blue_1_start_clicked)
#        self.pushButton_smooth_change_laser_blue_1_stop.clicked.connect(self.pushButton_smooth_change_laser_blue_1_stop_clicked)
#        #---------------------------------------------------------------------#
#
        self.timer_data = QtCore.QTimer()
        self.timer_data.setInterval(2000)
        self.timer_data.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer_data.timeout.connect(self.import_data)




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
        
        
#    ###########################################################################
#    ###########################################################################
#    ### THE FUNCTIONS FOR THE PUSH BUTTONS ####################################
#    ###########################################################################
#    ########################################################################### 
#    
#    
#    
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
    
    def save_channel_input(self):
        current_time = datetime.today()
        #options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog    
        #self.filename_monitoring, _ = QFileDialog.setNameFileter(tr("all files (*);; asc files (*.asc);; txt files (*.txt)"), options=options)
        
        #if self.filename_monitoring:
        #self.lineEdit_data.setText(self.filename_monitoring)
        file_name = 'Channel labels.txt'
        data_file = open(file_name,'a+')       
        data_file.write('\n ' + str(current_time) + '\n ' + 'Channel 1: ' + str(self.lineEdit_ch_1.text()) + '\n '+ 
                        'Channel 2: ' + str(self.lineEdit_ch_2.text()) + '\n '+ 'Channel 3: ' + str(self.lineEdit_ch_3.text()) + '\n '+
                        'Channel 4: ' + str(self.lineEdit_ch_4.text()) + '\n '+ 'Channel 5: ' + str(self.lineEdit_ch_5.text()) + '\n '+
                        'Channel 6: ' + str(self.lineEdit_ch_6.text()) + '\n '+ 'Channel 7: ' + str(self.lineEdit_ch_7.text()) + '\n '+
                        'Channel 8: ' + str(self.lineEdit_ch_8.text()) + '\n ')
        data_file.close()
    
    ### import txt file with monitoring of parameters #############################
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
        
    ###############################################################################
        

    def update_data(self):
        if self.radioButton_monitoring.isChecked() == True:
            #---------------------------------------------------------------------#
            self.timer_data.start()
            #---------------------------------------------------------------------#
        else:
            try:
                print('s')
                self.timer_data.stop()
            except:
                pass
            self.import_data()
            self.t_plots()



   
#        
    ###########################################################################        
    def t_plots(self):
        
#        self.label_nu_blue_1_is.setText(str(lc.nu_blue_1_is))
        
#        self.doubleSpinBox_nu_blue_1_want.setValue(lc.nu_blue_1_want)
           
#        lc.lock_blue_1_alpha = float(self.doubleSpinBox_lock_blue_1_alpha.value())
#        lc.lock_blue_1_beta = float(self.doubleSpinBox_lock_blue_1_beta.value())

        try:               
            x = np.arange(len(self.time))
        except Exception:
            pass


        
        try:
#            time_plot = []
#            for i in range(len(self.time)):
#                time_plot.append(time.mktime(datetime.datetime.now().timetuple()))
                
            self.plot_pressure.plot(x,self.p ,pen = blackPen, symbol = 'o', symbolBrush = blueBrush, name = 'nu_blue_1_was', clear = True)
        except Exception:
            pass
        if self.radioButton_ch_1.isChecked() == True:
            try:               
               self.plot_temp.plot(x,self.T_channels[0] ,pen = blackPen, symbol = 'o', name = 'nu_blue_1_was', clear = True)
            except Exception:
                #pass
                print('eh')
            
        if self.radioButton_ch_2.isChecked() == True:
            try:               
                self.plot_temp.plot(x,self.T_channels[1] ,pen = blackPen, symbol = 'o', name = 'nu_blue_1_was')
            except Exception:
                #pass
                print('eh1')       
        
        if self.radioButton_ch_3.isChecked() == True:
            try:               
                self.plot_temp.plot(x,self.T_channels[2] ,pen = blackPen, symbol = 'o', name = 'nu_blue_1_was')
            except Exception:
                #pass
                print('eh2')
         
        if self.radioButton_ch_4.isChecked() == True:
            try:               
                self.plot_temp.plot(x,self.T_channels[3] ,pen = blackPen, symbol = 'o', name = 'nu_blue_1_was')
            except Exception:
                #pass
                print('eh3')
            
        if self.radioButton_ch_5.isChecked() == True:
            try:               
                self.plot_temp.plot(x,self.T_channels[4] ,pen = blackPen, symbol = 'o', name = 'nu_blue_1_was')
            except Exception:
                #pass
                print('eh4')   
         
        if self.radioButton_ch_6.isChecked() == True:
            try:               
                self.plot_temp.plot(x,self.T_channels[5] ,pen = blackPen, symbol = 'o', name = 'nu_blue_1_was')
            except Exception:
                #pass
                print('eh5')
         
        if self.radioButton_ch_7.isChecked() == True:
            try:               
                self.plot_temp.plot(x,self.T_channels[6] ,pen = blackPen, symbol = 'o', name = 'nu_blue_1_was')
            except Exception:
                #pass
                print('eh6')   
         
        if self.radioButton_ch_8.isChecked() == True:
            try:               
                self.plot_temp.plot(x,self.T_channels[7] ,pen = blackPen, symbol = 'o', name = 'nu_blue_1_was')
            except Exception:
                #pass
                print('eh7')   
            
#        nu_blue_1_upper = pg.PlotCurveItem([0,500],[755.186881,755.186881],pen = bluePen)
#        nu_blue_1_lower = pg.PlotCurveItem([0,500],[755.186879,755.186879],pen = bluePen)
#        nu_blue_1_fill = pg.FillBetweenItem(nu_blue_1_upper,nu_blue_1_lower,blueBrush_alpha)
        
#        self.plot_nu_blue_1.addItem(nu_blue_1_upper)
#        self.plot_nu_blue_1.addItem(nu_blue_1_lower)
#        self.plot_nu_blue_1.addItem(nu_blue_1_fill)        
    ###########################################################################    


      
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    dialog_lc = QtWidgets.QMainWindow()
    
    programm_lc = window(dialog_lc)
    dialog_lc.show()
    
    sys.exit(app.exec_())