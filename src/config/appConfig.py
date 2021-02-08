import pandas as pd
from typing import List
from typeDefs.fileInfo import IFileInfo
from typeDefs.measInfo import IMeasInfo


fileMappings: List[IFileInfo] = []
measConfs: List[IMeasInfo] = []


def loadFileMappings(filePath='config.xlsx', sheetname='file_mapping') -> List[IFileInfo]:
    # TODO load the file_mapping sheet as dataframe
    global fileMappings
    fileMappings = pd.read_excel(filepath=filePath , sheet_name=sheetname )
    #Convert Nan to None
    fileMappings = fileMappings.where(pd.notnull(fileMappings),None)
    fileMappings = fileMappings.to_dict('records')
    return fileMappings


def loadMeasInfo(filePath='config.xlsx', sheetname='meas_info') -> List[IMeasInfo]:
    # TODO load the meas info sheet as dataframe
    global measConfs
    measConfs = pd.read_excel(filepath=filePath , sheet_name=sheetname)

    measConfs = measConfs.where(pd.notnull(fileMappings),None)
    measConfs = measConfs.to_dict('records')
    return measConfs
    


def getFileMappings() -> List[IFileInfo]:
    global fileMappings
    return fileMappings


def getMeasInfo() -> List[IMeasInfo]:
    global measConfs
    return measConfs
