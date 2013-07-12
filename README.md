VoeisPythonClient
=================

A python client to upload data to VOEIS

Both **POST_to_VOEIS.py** and **DataLoad.py** include a similar **API_LoadLoggerData** method.
**DataLoad.py** also includes logging of your uploads, and a means to track your previous 
uploads, only uploading the newest stuff from your upload file.

These scripts include the **requests** module you will either need to include the requests
directory in your working directory, or install requests (pip install requests).
See the **requests** module [here](https://github.com/kennethreitz/requests/tree/master/requests)
