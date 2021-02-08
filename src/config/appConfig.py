import pandas as pd
from typing import List
from typeDefs.fileInfo import IFileInfo
from typeDefs.measInfo import IMeasInfo


fileMappings: List[IFileInfo] = []
measConfs: List[IMeasInfo] = []


def loadFileMappings(filePath='config.xlsx', sheetname='file_mapping') -> List[IFileInfo]:
    # TODO load the file_mapping sheet as dataframe
    global fileMappings
    return fileMappings


def loadMeasInfo(filePath='config.xlsx', sheetname='meas_info') -> List[IMeasInfo]:
    # TODO load the meas info sheet as dataframe
    global measConfs
    return measConfs


def getFileMappings() -> List[IFileInfo]:
    global fileMappings
    return fileMappings


def getMeasInfo() -> List[IMeasInfo]:
    global measConfs
    return measConfs
