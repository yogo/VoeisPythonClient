# TEST: Python DataLoad

import DataLoad

api = 'e79b135dcfeb6699bbaa6c9ba9c1d0fc474d7adb755fa215446c398cae057adf'
project = 'cfee5aec-c520-11e0-a45c-c82a14fffebf'
LoggerFile = 'voeis_test.csv'
template_id = 36
site_id = 7
startline = 2

DataLoad.Make_updater(LoggerFile, startline)
data = DataLoad.API_LoadLoggerData(LoggerFile, site_id, api, project, template_id)
