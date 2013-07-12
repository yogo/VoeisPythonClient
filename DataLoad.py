# -*- coding: utf-8 -*-
"""
DateTime conversion script for CR10X loggers that store year, day, hr_min data in three separate columns. Script moves all datetime info to a single column.
Created on Wed Aug 31 15:26:03 2011
Updated on Fri July 12 2013

@author: Seth Kurt-Mason
@author: Thomas Heetderks
"""

### INPUT FILES PATH
file_path = './files/'

### HOST URL
voeis_host = 'https://voeis.msu.montana.edu'
#voeis_host = 'https://voeis-dev.msu.montana.edu'
#voeis_host = 'http://localhost:3000'


updater_file_name = 'Updater.csv'
upload_file_name = 'Upload_File.csv'
updater_file = file_path+updater_file_name
upload_file = file_path+upload_file_name


def timestamp_update(RawCR10X, TimeModified):
    import csv, datetime
    
    data = csv.reader(open(RawCR10X, 'rb'))  
    output = csv.writer(open(TimeModified,'wb'), delimiter=',',quoting=csv.QUOTE_NONE)
        
    for row in data:
        if row[0] == '60':
            hr_mn= row[3]
            hr = hr_mn[:-2]
            mn = hr_mn[-2:]
            if hr == '24':
                hr = 00
            date = datetime.datetime(int(row[1]), 1, 1, int(hr), int(mn)) + datetime.timedelta(int(row[2])-1)
            data_row = []
            data_row.insert(0, str(date))
            data_row.extend(row[4:len(row)]) 
            output.writerow(data_row)
            
    data.close()
    output.close()
    
 ##################   
    
def CheckNewData(LoggerFile):    
    import filecmp
    
    if filecmp.cmp(LoggerFile, updater_file) == False:    
        return "OK to Upload"

####################

def Make_updater(LoggerFile, startline):
    import os, csv
    
    if os.path.isfile(updater_file) == False:
        a = open(LoggerFile, 'rb')
        logger = csv.reader(a)
        b = open(updater_file, 'wb')
        update = csv.writer(b, delimiter=',',quoting=csv.QUOTE_NONE)
        
        data = list(logger)
    
        for row in data[:(int(startline)-1)]:
            update.writerow(row)
        
        a.close()
        b.close()
            
#######################

def API_LoadLoggerData(LoggerFile, site_id, api, project, template_id):
    
    import requests
    import os, csv
    
    class Test:
       def __init__(self):
           self.contents = ''
    
       def body_callback(self, buf):
           self.contents = self.contents + buf
      
    print LoggerFile       
    a = open(LoggerFile, 'rb')
    logger = csv.reader(a)
    b = open(updater_file, 'rb')
    update = csv.reader(b)
    c = open(upload_file,'wb')

    upload_data = csv.writer(c, delimiter=',',quoting=csv.QUOTE_NONE)

    data = list(logger)
    up = list(update)
    diff = len(data)-len(up)
    print "# New Data Rows=", diff
    
    if diff > 0:
        print "Creating Upload File"
        startline = 1
        for row in data[-(diff):]:
            upload_data.writerow(row)
   
        a.close()
        b.close()
        c.close()

        print "File to Upload to VOEIS="+upload_file

        url = voeis_host+'/projects/%s/apivs/upload_data.json?api_key=%s'%(project,api)
        #url = 'https://posttestserver.com/post.php'
        print 'URL='+url
        
        params = {'data_template_id': template_id,
                   'site_id': site_id,
                   'start_line': startline,
                   'api_key': api
                   }
        files = {'datafile': open(upload_file, 'rb')}

        # POST request
        return requests.post(url, data=params, files=files)
