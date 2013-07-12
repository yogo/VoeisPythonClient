def API_LoadLoggerData(LoggerFile, site_id, api, project, template_id):
    
    from encode import multipart_encode
    from streaminghttp import register_openers
    import urllib2, os, csv
    
      
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

        # Register the streaming http handlers with urllib2
        register_openers()
        
        # Start the multipart/form-data encoding of the file "DSC0001.jpg"
        # "image1" is the name of the parameter, which is normally set
        # via the "name" parameter of the HTML <input> tag.
        
        # headers contains the necessary Content-Type and Content-Length
        # datagen is a generator object that yields the encoded parameters
        datagen, headers = multipart_encode ({'datafile': open('Upload_File.csv', 'rb'),
                            'data_template_id': template_id,
                            'site_id': site_id,
                            'start_line': startline,
                            'api_key': api
                            })
        
        # Create the Request object
        request = urllib2.Request(url, datagen, headers)
        # Actually do the request, and get the response
        print urllib2.urlopen(request).read()