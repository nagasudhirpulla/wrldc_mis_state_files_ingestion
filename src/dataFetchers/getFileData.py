from openpyxl.worksheet.worksheet import Worksheet
from src.typeDefs.fileInfo import IFileInfo
import datetime as dt
from openpyxl import load_workbook

def getFileData(fileInfo: IFileInfo, targetDt: dt.datetime) -> Worksheet:
    # TODO fetch with openpyxl
    wb = load_workbook(fileInfo.folder_location, data_only=True)
    ws = wb.active
    
    return ws
