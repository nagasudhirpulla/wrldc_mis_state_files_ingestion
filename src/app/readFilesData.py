from src.config.appConfig import getFileMappings, getMeasInfo, getJsonConfig
from src.dataFetchers.getFileData import getFileData
import datetime as dt
from src.repos.measData.measDataRepo import MeasDataRepo
class InsertFilesDataRepo():    
    def insertFilesData(self, targetDt: dt.datetime):
        measInfo = getMeasInfo()
        fileMappingsInfo = getFileMappings()
        jsonConfig = getJsonConfig()
        measDataRepo = MeasDataRepo(jsonConfig['appDbConnStr'])
        for each in fileMappingsInfo:
            eachStateRecords = getFileData(each, targetDt)

            measDataRepo.insertMetricsData(eachStateRecords)
        return fileMappingsInfo