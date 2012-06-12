# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 18:14:09 2011

@author: -
"""

import DataLoad, os, sys, datetime

class MyOutput():
    def __init__(self, logfile):
        self.stdout = sys.stdout
        self.log = open(logfile, 'w')
 
    def write(self, text):
        self.stdout.write(text)
        self.log.write(text)
        self.log.flush()
 
    def close(self):
        self.stdout.close()
        self.log.close()
 
sys.stdout = MyOutput("log_file.txt") 

working_dir = os.getcwd()
now = datetime.datetime.now()
print now.strftime("Last Push to VOEIS: %Y-%m-%d %H:%M")
print '-----------------'
print ''
########################################################################
########################################################################
#Big Sky Streamflow Stations (NFork, WFork, SFork, UPWestFork, BaseStation)

#############
##NFork
os.chdir('.\BigSky_Streamflow\NFork')

LoggerFile = 'CR1000_BigSky_NFork.dat'

try:
    api =  'b9547a89e6481eb19c37c9177d7b597442d4da0fd7cb91a59e1a720adf4adb29'
    project = 'b6db01d0-e606-11df-863f-6e9ffb75bc80'
    template_id =  12
    startline = 5
    site_id = 2
    DataLoad.Make_updater(LoggerFile, startline)
    DataLoad.API_LoadLoggerData(LoggerFile, site_id, api, project, template_id)
except:
    pass 

os.chdir(working_dir)

#############
#SFork
os.chdir('.\BigSky_Streamflow\SFork')

LoggerFile = 'CR1000_BigSky_SFork.dat'

try:
    api =  'b9547a89e6481eb19c37c9177d7b597442d4da0fd7cb91a59e1a720adf4adb29'
    project = 'b6db01d0-e606-11df-863f-6e9ffb75bc80'
    template_id =  9
    startline = 5
    site_id = 1
    DataLoad.Make_updater(LoggerFile, startline)
    DataLoad.API_LoadLoggerData(LoggerFile, site_id, api, project, template_id)
except:
    pass  

os.chdir(working_dir)
        
#############
#WFork
os.chdir('.\BigSky_Streamflow\WFork')

LoggerFile = 'CR1000_BigSky_WFork.dat'

try:
    api =  'b9547a89e6481eb19c37c9177d7b597442d4da0fd7cb91a59e1a720adf4adb29'
    project = 'b6db01d0-e606-11df-863f-6e9ffb75bc80'
    template_id =  10
    startline = 5
    site_id = 3
    DataLoad.Make_updater(LoggerFile, startline)
    DataLoad.API_LoadLoggerData(LoggerFile, site_id, api, project, template_id)
except:
    pass   

os.chdir(working_dir)
        
#############
#UPWFork
os.chdir('.\BigSky_Streamflow\UPWFork')

LoggerFile = 'CR1000_BigSky_UPWFork.dat'

try:
    api =  'b9547a89e6481eb19c37c9177d7b597442d4da0fd7cb91a59e1a720adf4adb29'
    project = 'b6db01d0-e606-11df-863f-6e9ffb75bc80'
    template_id =  11
    startline = 5    
    site_id = 4
    DataLoad.Make_updater(LoggerFile, startline)
    DataLoad.API_LoadLoggerData(LoggerFile, site_id, api, project, template_id)
except:
    pass   
        
os.chdir(working_dir)

#############
#BaseStation
os.chdir('.\BigSky_Streamflow\BaseStation')

LoggerFile = 'CR1000_BigSky_Base.dat'

try:
    api =  'b9547a89e6481eb19c37c9177d7b597442d4da0fd7cb91a59e1a720adf4adb29'
    project = 'b6db01d0-e606-11df-863f-6e9ffb75bc80'
    template_id =  17
    startline = 5    
    site_id = 5
    DataLoad.Make_updater(LoggerFile, startline)
    DataLoad.API_LoadLoggerData(LoggerFile, site_id, api, project, template_id)
except:
    pass   

os.chdir(working_dir)


#######################################################################
#######################################################################
#Yellowstone Club Meteorological Stations (Andesite, BaseArea, Timber, ASprirt)

#####################
##Andesite datastream 
##This is loading to -dev
#os.chdir('.\YellowstoneClub\Andesite')
#
#try:
#    
#    RawCR10X = 'CR10X_YC_Andesite_winter.dat'
#    LoggerFile = 'AndesiteTimeAdjusted.csv'
#    
#    api =  'b9547a89e6481eb19c37c9177d7b597442d4da0fd7cb91a59e1a720adf4adb29'
#    project = 'b6db01d0-e606-11df-863f-6e9ffb75bc80'
#    template_id =  16
#    startline = 1
#    
#    DataLoad.timestamp_update(RawCR10X, LoggerFile)
#    
#    DataLoad.Make_updater(LoggerFile, startline)
#    DataLoad.API_Load2Dev(LoggerFile, api, project, template_id, startline)
#except:
#    pass 
#
#os.chdir(working_dir)
#    
#####################
##Timber datastream 
##This is loading to -dev
#os.chdir('.\YellowstoneClub\Timber')
#
#try:
#    
#    RawCR10X = 'CR10X_YC_Timber_winter.dat'
#    LoggerFile = 'TimberTimeAdjusted.csv'
#    
#    api =  'b9547a89e6481eb19c37c9177d7b597442d4da0fd7cb91a59e1a720adf4adb29'
#    project = 'b6db01d0-e606-11df-863f-6e9ffb75bc80'
#    template_id =  19
#    startline = 1
#    
#    DataLoad.timestamp_update(RawCR10X, LoggerFile)
#    
#    DataLoad.Make_updater(LoggerFile, startline)
#    DataLoad.API_Load2Dev(LoggerFile, api, project, template_id, startline)
#except:
#    pass
#
#os.chdir(working_dir)
#
#####################
##Base Area datastream 
##Connection to logger is not working
#
#
#####################
##American Spirit datastream 
##This is loading to -dev
#os.chdir('.\YellowstoneClub\ASpirit')
#
#try:
#
#    RawCR10X = 'CR10X_YC_ASpirit_winter.dat'
#    LoggerFile = 'ASpiritTimeAdjusted.csv'
#    
#    api =  'b9547a89e6481eb19c37c9177d7b597442d4da0fd7cb91a59e1a720adf4adb29'
#    project = 'b6db01d0-e606-11df-863f-6e9ffb75bc80'
#    template_id =  20
#    startline = 1
#    
#    DataLoad.timestamp_update(RawCR10X, LoggerFile)
#    
#    DataLoad.Make_updater(LoggerFile, startline)
#    DataLoad.API_Load2Dev(LoggerFile, api, project, template_id, startline)
#except:
#    pass
#
#os.chdir(working_dir)

######################