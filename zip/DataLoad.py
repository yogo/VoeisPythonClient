# -*- coding: utf-8 -*-
"""
DateTime conversion script for CR10X loggers that store year, day, hr_min data in three separate columns. Script moves all datetime info to a single column.
Created on Wed Aug 31 15:26:03 2011

@author: - Seth Mason
"""

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
    
    if filecmp.cmp(LoggerFile, 'Updater.csv') == False:    
        return "OK to Upload"

####################

def Make_updater(LoggerFile, startline):
    import os, csv
    
    if os.path.isfile(os.getcwd()+'\Updater.csv') == False:
        a = open(LoggerFile, 'rb')
        logger = csv.reader(a)
        b = open('Updater.csv', 'wb')
        update = csv.writer(b, delimiter=',',quoting=csv.QUOTE_NONE)
        
        data = list(logger)
    
        for row in data[:(int(startline)-1)]:
            update.writerow(row)
        
        a.close()
        b.close()
            
#######################

def API_LoadLoggerData(LoggerFile, site_id, api, project, template_id):
    
    from encode import multipart_encode
    from streaminghttp import register_openers
    import urllib2, os, csv
    
    class Test:
       def __init__(self):
           self.contents = ''
    
       def body_callback(self, buf):
           self.contents = self.contents + buf
      
    print LoggerFile       
    a = open(LoggerFile, 'rb')
    logger = csv.reader(a)
    UpdateFile = 'Updater.csv'
    b = open(UpdateFile, 'rb')
    update = csv.reader(b)
    c = open('Upload_File.csv','wb')
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

        upload_file = os.getcwd()+'\Upload_File.csv'
        print "File to Upload to VOEIS="+upload_file

        url='https://voeis.msu.montana.edu/projects/'+str(project)+'/apivs/upload_data.json?'
        print 'URL='+url
                
        params = ({'datafile': open('Upload_File.csv', 'rb'),
                   'data_template_id': template_id,
                   'site_id': site_id,
                   'start_line': startline,
                   'api_key': api
                   })
        # Register the streaming http handlers with urllib2
        register_openers()

        # headers contains the necessary Content-Type and Content-Length
        # datagen is a generator object that yields the encoded parameters
        datagen, headers = multipart_encode(params)
        print headers
        # Create the Request object
        request = urllib2.Request(url, datagen, headers)
        # Actually do the request, and get the response
        result = urllib2.urlopen(request).read()
        print result
        return result