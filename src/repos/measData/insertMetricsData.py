from typing_extensions import final
import cx_Oracle
from typing import List
from src.typeDefs.metricsDataRecord import IMetricsDataRecord


def insertMetricsData(appDbConnStr: str, dataSamples: List[IMetricsDataRecord]) -> bool:
    """Inserts a entity metrics time series data into the app db

    Args:
    appDbConnStr (str): [description]
    dataSamples (List[IMetricsDataRecord]): [description]

    Returns:
        bool: returns true if process is ok
    """
    dbConn = None
    dbCur = None
    isInsertSuccess = True
    try:
        dbConn = cx_Oracle.connect(appDbConnStr)
        dbCur = dbConn.cursor()
        colsNames = [" "," "," "," "]
        sqlPlaceHldrsTxt = ','.join([':{0}'.format(x+1)
                                     for x in range(len(colsNames))])
        for dataSample in dataSamples:
            insertSql = "INSERT INTO MIS_WAREHOUSE.STATE_FILES_DATA({0}) VALUES ({1})".format(colsNames, sqlPlaceHldrsTxt)
            
            dbCur.execute(insertSql,dataSample)
            dbConn.commit()
    
    except Exception as err:
        isInsertSuccess = False
        print('Error while insertion of Metric Data')
        print(err)

    finally:
        if dbCur is not None:
            dbCur.close()
        if dbConn is not None:
            dbConn.close()
        
    return isInsertSuccess
