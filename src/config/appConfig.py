import pandas as pd
from typing import List
from src.typeDefs.fileInfo import IFileInfo
from src.typeDefs.measInfo import IMeasInfo
import json


fileMappings: List[IFileInfo] = []
measConfs: List[IMeasInfo] = []
jsonConfig: dict = {}

def initConfig():
    loadFileMappings()
    loadJsonConfig()
    loadMeasInfo()

def loadJsonConfig(fName="config.json") -> dict:
    global jsonConfig
    with open(fName) as f:
        data = json.load(f)
        jsonConfig = data
        return jsonConfig

def loadFileMappings(filePath='config.xlsx', sheetname='files_info') -> List[IFileInfo]:
    global fileMappings
    fileMappingsDf = pd.read_excel(filePath, sheet_name=sheetname)
    # Convert Nan to None
    # fileMappings = fileMappingsDf.where(pd.notnull(fileMappings),None)
    fileMappings = fileMappingsDf.to_dict('records')
    return fileMappings


def loadMeasInfo(filePath='config.xlsx', sheetname='meas_info') -> List[IMeasInfo]:
    global measConfs
    measConfsDf = pd.read_excel(filePath, sheet_name=sheetname)

    # measConfs = measConfs.where(pd.notnull(fileMappings), None)
    measConfs = measConfsDf.to_dict('records')
    return measConfs


def getFileMappings() -> List[IFileInfo]:
    global fileMappings
    return fileMappings


def getMeasInfo() -> List[IMeasInfo]:
    global measConfs
    return measConfs

def getJsonConfig() -> dict:
    global jsonConfig
    return jsonConfig
