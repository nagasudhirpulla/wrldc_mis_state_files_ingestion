from src.config.appConfig import loadFileMappings
from src.app.readFilesData import InsertFilesDataRepo
import datetime as dt
# fileMappings = loadFileMappings()
# print(fileMappings)

# initiate object
readFiles = InsertFilesDataRepo()
targetDt = dt.datetime.today()- dt.timedelta(days=1)
print(targetDt)
isInsertionSuccess = readFiles.insertFilesData(targetDt)
