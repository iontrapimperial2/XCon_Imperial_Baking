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
        self.timer_data.setInterval(30000)
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
#
#        #---------------------------------------------------------------------#   
#        self.pushButton_lock_laser_blue_2_on.clicked.connect(self.pushButton_lock_laser_blue_2_on_clicked)
#        self.pushButton_lock_laser_blue_2_off.clicked.connect(self.pushButton_lock_laser_blue_2_off_clicked)
#        
#        self.pushButton_smooth_change_laser_blue_2_start.clicked.connect(self.pushButton_smooth_change_laser_blue_2_start_clicked)
#        self.pushButton_smooth_change_laser_blue_2_stop.clicked.connect(self.pushButton_smooth_change_laser_blue_2_stop_clicked)
#        #---------------------------------------------------------------------#
#
#        #---------------------------------------------------------------------#
#        self.timer_t_dependent_plots_laser_blue_2 = QtCore.QTimer()
#        self.timer_t_dependent_plots_laser_blue_2.setInterval(250)
#        self.timer_t_dependent_plots_laser_blue_2.setTimerType(QtCore.Qt.PreciseTimer)
#        self.timer_t_dependent_plots_laser_blue_2.timeout.connect(self.t_dependent_updates_laser_blue_2)
#        self.timer_t_dependent_plots_laser_blue_2.start()
#        #---------------------------------------------------------------------#        
# 
#
#
#        #---------------------------------------------------------------------#
#        #--- PLOTS, PUSH BUTTONS AND TIMERS FOR LASER RED 1 ------------------#
#        #---------------------------------------------------------------------#        
#        self.plot_nu_red_1 = pg.PlotWidget(name = 'widget_plot_nu_red_1')
#        self.plot_nu_red_1.setBackground(background = brush_background)
#        self.plot_nu_red_1.setLabel('left', 'nu', units = '[THz]', **labelstyle_L)
#        self.plot_nu_red_1.setLabel('bottom', 'time', units = '', **labelstyle_L)
#        self.plot_nu_red_1.showGrid(x = True, y = True)
#        
#        self.verticalLayout_nu_laser_red_1.addWidget(self.plot_nu_red_1)
#        #---------------------------------------------------------------------#
#
#        #---------------------------------------------------------------------#   
#        self.pushButton_lock_laser_red_1_on.clicked.connect(self.pushButton_lock_laser_red_1_on_clicked)
#        self.pushButton_lock_laser_red_1_off.clicked.connect(self.pushButton_lock_laser_red_1_off_clicked)
#        
#        self.pushButton_smooth_change_laser_red_1_start.clicked.connect(self.pushButton_smooth_change_laser_red_1_start_clicked)
#        self.pushButton_smooth_change_laser_red_1_stop.clicked.connect(self.pushButton_smooth_change_laser_red_1_stop_clicked)
#        #---------------------------------------------------------------------#
#
#        #---------------------------------------------------------------------#
#        self.timer_t_dependent_plots_laser_red_1 = QtCore.QTimer()
#        self.timer_t_dependent_plots_laser_red_1.setInterval(250)
#        self.timer_t_dependent_plots_laser_red_1.setTimerType(QtCore.Qt.PreciseTimer)
#        self.timer_t_dependent_plots_laser_red_1.timeout.connect(self.t_dependent_updates_laser_red_1)
#        self.timer_t_dependent_plots_laser_red_1.start()
#        #---------------------------------------------------------------------#
#        
#        
#        #---------------------------------------------------------------------#
#        #--- PLOTS, PUSH BUTTONS AND TIMERS FOR LASER RED 2 ------------------#
#        #---------------------------------------------------------------------#        
#        self.plot_nu_red_2 = pg.PlotWidget(name = 'widget_plot_nu_red_2')
#        self.plot_nu_red_2.setBackground(background = brush_background)
#        self.plot_nu_red_2.setLabel('left', 'nu', units = '[THz]', **labelstyle_L)
#        self.plot_nu_red_2.setLabel('bottom', 'time', units = '', **labelstyle_L)
#        self.plot_nu_red_2.showGrid(x = True, y = True)
#        
#        self.verticalLayout_nu_laser_red_2.addWidget(self.plot_nu_red_2)
#        #---------------------------------------------------------------------#
#
#        #---------------------------------------------------------------------#   
#        self.pushButton_lock_laser_red_2_on.clicked.connect(self.pushButton_lock_laser_red_2_on_clicked)
#        self.pushButton_lock_laser_red_2_off.clicked.connect(self.pushButton_lock_laser_red_2_off_clicked)
#        
#        self.pushButton_smooth_change_laser_red_2_start.clicked.connect(self.pushButton_smooth_change_laser_red_2_start_clicked)
#        self.pushButton_smooth_change_laser_red_2_stop.clicked.connect(self.pushButton_smooth_change_laser_red_2_stop_clicked)
#        #---------------------------------------------------------------------#
#
#        #---------------------------------------------------------------------#
#        self.timer_t_dependent_plots_laser_red_2 = QtCore.QTimer()
#        self.timer_t_dependent_plots_laser_red_2.setInterval(250)
#        self.timer_t_dependent_plots_laser_red_2.setTimerType(QtCore.Qt.PreciseTimer)
#        self.timer_t_dependent_plots_laser_red_2.timeout.connect(self.t_dependent_updates_laser_red_2)
#        self.timer_t_dependent_plots_laser_red_2.start()
#        #---------------------------------------------------------------------#    
#
#
#
#        #---------------------------------------------------------------------#
#        #--- PLOTS, PUSH BUTTONS AND TIMERS FOR SAWTOOTH ---------------------#
#        #---------------------------------------------------------------------#         
#        self.plot_sawtooth1 = pg.PlotWidget(name = 'widget_plot_sawtooth')
#        self.plot_sawtooth1.setBackground(background = brush_background)
#        self.plot_sawtooth1.setLabel('left', 'nu', units = '[THz]', **labelstyle_L)
#        self.plot_sawtooth1.setLabel('bottom', 'time', units = '', **labelstyle_L)
#        self.plot_sawtooth1.showGrid(x = True, y = True)
#        
#        self.verticalLayout_sawtooth_blue_1.addWidget(self.plot_sawtooth1)
#        #---------------------------------------------------------------------#
#        
#        #---------------------------------------------------------------------#        
#        self.plot_sawtooth2 = pg.PlotWidget(name = 'widget_plot_sawtooth')
#        self.plot_sawtooth2.setBackground(background = brush_background)
#        self.plot_sawtooth2.setLabel('left', 'nu', units = '[THz]', **labelstyle_L)
#        self.plot_sawtooth2.setLabel('bottom', 'time', units = '', **labelstyle_L)
#        self.plot_sawtooth2.showGrid(x = True, y = True)
#        
#        self.verticalLayout_sawtooth_blue_2.addWidget(self.plot_sawtooth2)
#        #---------------------------------------------------------------------#
#        
#        self.pushButton_sawtooth_laser_blue_1_and_2_start.clicked.connect(lc.sawtooth_laser_blue_1_and_2_on)
#        self.pushButton_sawtooth_laser_blue_1_and_2_stop.clicked.connect(lc.sawtooth_laser_blue_1_and_2_off)
#        
#        #---------------------------------------------------------------------#
#        self.timer_t_dependent_plots_sawtooth = QtCore.QTimer()
#        self.timer_t_dependent_plots_sawtooth.setInterval(250)
#        self.timer_t_dependent_plots_sawtooth.setTimerType(QtCore.Qt.PreciseTimer)
#        self.timer_t_dependent_plots_sawtooth.timeout.connect(self.t_dependent_updates_sawtooth)
#        self.timer_t_dependent_plots_sawtooth.start()
#        #---------------------------------------------------------------------#
        
        
        
        
        
        
        
        
        
        #---------------------------------------------------------------------#
        self.timer_plot_data = QtCore.QTimer()
        self.timer_plot_data.setInterval(15000)
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
        for j in range(2,9):
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
#    def pushButton_lock_laser_blue_1_off_clicked(self):
#        lc.lock_laser_blue_1_off()
#        self.label_lock_blue_1_status.setText('OFF')
#        self.label_lock_blue_1_status.setStyleSheet('color: red')
#        
#    def pushButton_smooth_change_laser_blue_1_start_clicked(self):
#        lc.nu_blue_1_smooth_want = float(self.doubleSpinBox_nu_blue_1_smooth_want.value())
#        lc.nu_blue_1_smooth_delta_t = float(self.doubleSpinBox_nu_blue_1_smooth_delta_t.value())
#        lc.smooth_change_laser_blue_1_start()
#
#    def pushButton_smooth_change_laser_blue_1_stop_clicked(self):
#        lc.smooth_change_laser_blue_1_stop()
#    ###########################################################################   
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
        
        try:               
            self.plot_temp.plot(x,self.T_channels[0] ,pen = blackPen, symbol = 'o', symbolBrush = blueBrush, name = 'nu_blue_1_was', clear = True)
        except Exception:
            pass

        try:               
            self.plot_temp.plot(x,self.T_channels[1] ,pen = blackPen, symbol = 'o', symbolBrush = blueBrush, name = 'nu_blue_1_was')
        except Exception:
            pass       
        
            
#        nu_blue_1_upper = pg.PlotCurveItem([0,500],[755.186881,755.186881],pen = bluePen)
#        nu_blue_1_lower = pg.PlotCurveItem([0,500],[755.186879,755.186879],pen = bluePen)
#        nu_blue_1_fill = pg.FillBetweenItem(nu_blue_1_upper,nu_blue_1_lower,blueBrush_alpha)
        
#        self.plot_nu_blue_1.addItem(nu_blue_1_upper)
#        self.plot_nu_blue_1.addItem(nu_blue_1_lower)
#        self.plot_nu_blue_1.addItem(nu_blue_1_fill)        
    ###########################################################################    
#        
#
#
#    ###########################################################################
#    ### FUNCTIONS FOR LASER BLUE 2 ############################################
#    ###########################################################################           
#        
#    ###########################################################################
#    def pushButton_lock_laser_blue_2_on_clicked(self):
#        lc.nu_blue_2_want = float(self.doubleSpinBox_nu_blue_2_want.value())
#        lc.lock_laser_blue_2_on()
#        self.label_lock_blue_2_status.setText('ON')
#        self.label_lock_blue_2_status.setStyleSheet('color: black')        
#        
#    def pushButton_lock_laser_blue_2_off_clicked(self):
#        lc.lock_laser_blue_2_off()
#        self.label_lock_blue_2_status.setText('OFF')
#        self.label_lock_blue_2_status.setStyleSheet('color: red')
#        
#    def pushButton_smooth_change_laser_blue_2_start_clicked(self):
#        lc.nu_blue_2_smooth_want = float(self.doubleSpinBox_nu_blue_2_smooth_want.value())
#        lc.nu_blue_2_smooth_delta_t = float(self.doubleSpinBox_nu_blue_2_smooth_delta_t.value())
#        lc.smooth_change_laser_blue_2_start()
#
#    def pushButton_smooth_change_laser_blue_2_stop_clicked(self):
#        lc.smooth_change_laser_blue_2_stop()
#    ###########################################################################   
#        
#    ###########################################################################        
#    def t_dependent_updates_laser_blue_2(self):
#        
#        self.label_nu_blue_2_is.setText(str(lc.nu_blue_2_is))
#        
##        self.doubleSpinBox_nu_blue_1_want.setValue(lc.nu_blue_1_want)
#           
#        lc.lock_blue_2_alpha = float(self.doubleSpinBox_lock_blue_2_alpha.value())
#        lc.lock_blue_2_beta = float(self.doubleSpinBox_lock_blue_2_beta.value())
#       
#        try:
#            self.plot_nu_blue_2.plot(np.arange(500),lc.nu_blue_2_was[-500:],pen = blackPen, symbol = 'o', symbolBrush = blueBrush, name = 'nu_blue_2_was', clear = True)
#        except Exception:
#            pass
#            
#        nu_blue_2_upper = pg.PlotCurveItem([0,500],[755.258221,755.258221],pen = bluePen)
#        nu_blue_2_lower = pg.PlotCurveItem([0,500],[755.258219,755.258219],pen = bluePen)
#        nu_blue_2_fill = pg.FillBetweenItem(nu_blue_2_upper,nu_blue_2_lower,blueBrush_alpha)
#        
#        self.plot_nu_blue_2.addItem(nu_blue_2_upper)
#        self.plot_nu_blue_2.addItem(nu_blue_2_lower)
#        self.plot_nu_blue_2.addItem(nu_blue_2_fill)        
#    ###########################################################################         
# 
#
#
#    ###########################################################################
#    ### FUNCTIONS FOR LASER RED 1 #############################################
#    ###########################################################################           
#        
#    ###########################################################################
#    def pushButton_lock_laser_red_1_on_clicked(self):
#        lc.nu_red_1_want = float(self.doubleSpinBox_nu_red_1_want.value())
#        lc.lock_laser_red_1_on()
#        self.label_lock_red_1_status.setText('ON')
#        self.label_lock_red_1_status.setStyleSheet('color: black')        
#        
#    def pushButton_lock_laser_red_1_off_clicked(self):
#        lc.lock_laser_red_1_off()
#        self.label_lock_red_1_status.setText('OFF')
#        self.label_lock_red_1_status.setStyleSheet('color: red')
#        
#    def pushButton_smooth_change_laser_red_1_start_clicked(self):
#        lc.nu_red_1_smooth_want = float(self.doubleSpinBox_nu_red_1_smooth_want.value())
#        lc.nu_red_1_smooth_delta_t = float(self.doubleSpinBox_nu_red_1_smooth_delta_t.value())
#        lc.smooth_change_laser_red_1_start()
#
#    def pushButton_smooth_change_laser_red_1_stop_clicked(self):
#        lc.smooth_change_laser_red_1_stop()
#    ###########################################################################   
#        
#    ###########################################################################        
#    def t_dependent_updates_laser_red_1(self):
#        
#        self.label_nu_red_1_is.setText(str(lc.nu_red_1_is))
#        
##        self.doubleSpinBox_nu_blue_1_want.setValue(lc.nu_blue_1_want)
#           
#        lc.lock_red_1_alpha = float(self.doubleSpinBox_lock_red_1_alpha.value())
#        lc.lock_red_1_beta = float(self.doubleSpinBox_lock_red_1_beta.value())
#       
#        try:
#            self.plot_nu_red_1.plot(np.arange(500),lc.nu_red_1_was[-500:],pen = blackPen, symbol = 'o', symbolBrush = redBrush, name = 'nu_red_1_was', clear = True)
#        except Exception:
#            pass
#            
#        nu_red_1_upper = pg.PlotCurveItem([0,500],[346.000255,346.000255],pen = redPen)
#        nu_red_1_lower = pg.PlotCurveItem([0,500],[346.000245,346.000245],pen = redPen)
#        nu_red_1_fill = pg.FillBetweenItem(nu_red_1_upper,nu_red_1_lower,redBrush_alpha)
#        
#        self.plot_nu_red_1.addItem(nu_red_1_upper)
#        self.plot_nu_red_1.addItem(nu_red_1_lower)
#        self.plot_nu_red_1.addItem(nu_red_1_fill)        
#    ###########################################################################   
 
#
#
#    ###########################################################################        
#    def t_dependent_updates_sawtooth(self):
#       
#        lc.sawtooth_nu_blue_1_init = self.doubleSpinBox_sawtooth_nu_blue_1_init.value()
#        lc.sawtooth_nu_blue_1_detuned = self.doubleSpinBox_sawtooth_nu_blue_1_detuned.value()
#        lc.sawtooth_nu_blue_2_init = self.doubleSpinBox_sawtooth_nu_blue_2_init.value()
#        lc.sawtooth_nu_blue_2_detuned = self.doubleSpinBox_sawtooth_nu_blue_2_detuned.value()
#        lc.sawtooth_delta_t1 = self.doubleSpinBox_sawtooth_delta_t1.value()
#        lc.sawtooth_delta_t2 = self.doubleSpinBox_sawtooth_delta_t2.value()
#        lc.sawtooth_total_reps = self.spinBox_sawtooth_total_reps.value()
#        
#        lc.f_prepare_sawtooth_laser_blue_1_and_2()
#            
#        self.plot_sawtooth1.plot(lc.sawtooth_t_total,lc.sawtooth_nu1_total, order = 0, pen = bluePen, name = 'nu_sawtooth1', clear = True)
#        self.plot_sawtooth2.plot(lc.sawtooth_t_total,lc.sawtooth_nu2_total, order = 0, pen = bluePen, name = 'nu_sawtooth2', clear = True)
#    ###########################################################################   

      
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    dialog_lc = QtWidgets.QMainWindow()
    
    programm_lc = window(dialog_lc)
    dialog_lc.show()
    
    sys.exit(app.exec_())