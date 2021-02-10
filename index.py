from src.config.appConfig import initConfig
from src.app.readFilesData import InsertFilesDataRepo
import datetime as dt
# instantiate loadFileMappings, 

initConfig()

# initiate object
readFiles = InsertFilesDataRepo()
targetDt = dt.datetime.today()- dt.timedelta(days=1)
# print(targetDt)
isInsertionSuccess = readFiles.insertFilesData(targetDt)
