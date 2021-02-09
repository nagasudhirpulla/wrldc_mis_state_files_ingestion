from src.config.appConfig import loadFileMappings, loadMeasInfo
from src.dataFetchers.getFileData import getFileData
import datetime as dt

class InsertFilesDataRepo():    
    def insertFilesData(self, targetDt: dt.datetime):
        fileMappingsInfo = loadFileMappings()
        for each in fileMappingsInfo:
            getFileData(each, targetDt)
        # print(fileMappingsInfo)
        return fileMappingsInfo