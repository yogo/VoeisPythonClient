# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 18:14:09 2011
Updated on Fri July 12 2013

@author: Seth Kurt-Mason
@author: Thomas Heetderks
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

#get working directory
working_dir = os.getcwd()

#set current datetime
now = datetime.datetime.now()
print now.strftime("Last Push to VOEIS: %Y-%m-%d %H:%M")
print '-----------------'
print ''
########################################################################
########################################################################
#Big Sky Streamflow Stations (NFork, WFork, SFork, UPWestFork, BaseStation)

#############
##NFork
#Change directory to were your file is
#os.chdir('.\BigSky_Streamflow\NFork')
#os.chdir('S:\SensorOutput\HBS_Roof\WXT520')

#os.chdir('C:\voeis\files')
#os.chdir(r'./files')

#specify the file you are going to upload
#LoggerFile = 'CR1000_BigSky_NFork.dat'
#LoggerFile = './files/HBS_Roof_WXT520.csv'
#LoggerFile = './files/testing201307.csv'
LoggerFile = './files/voeis_test.csv'
response = ''

try:
    api =  'f0f30a157c6fd2fbbcf7a1909db154ae188a35687e21ea0e8b4ada7908a3ee53' # HBS, KY
    project = '472ba996-d769-11e2-923a-828fa5c85a32'  # HBS, KY
    template_id = 3  # HBS, KY
    startline = 1 #THE LINE YOUR DATA STARTS ON - HBS, KY
    #api =  'af4685cf01e992adfc4bb3a309a843af5f1d23ae2f497732c1ecf8f7d52227a2' ## yogo
    #project = 'b6db01d0-e606-11df-863f-6e9ffb75bc80' ## Big Sky
    #project = '472ba996-d769-11e2-923a-828fa5c85a32'  #THIS IS YOUR PROJECTS UID the example is for big sky change it to your project
    #template_id = 9  # UPLOAD TEMPLATE ID - Big Sky (LOCAL)
    #startline = 2 #THE LINE YOUR DATA STARTS ON
    site_id = 1 #THE ID OF THE SITE YOU WANT TO LOAD THE DATA INTO
    DataLoad.Make_updater(LoggerFile, startline)
    response = DataLoad.API_LoadLoggerData(LoggerFile, site_id, api, project, template_id)
except:
    print 'FAILURE!!'

print 'DONE!'
print '---------------'
print repr(response.headers)
#print '---------------'
#print response.text
