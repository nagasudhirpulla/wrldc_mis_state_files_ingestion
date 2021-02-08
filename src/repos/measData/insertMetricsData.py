from typing import List
from src.typeDefs.metricsDataRecord import IMetricsDataRecord


def insertMetricsData(appDbConnStr: str, dataSamples: List[IMetricsDataRecord]) -> bool:
    """inserts a entity metrics time series data into the app db

    Args:
    appDbConnStr (str): [description]
    dataSamples (List[IMetricsDataRecord]): [description]

    Returns:
        bool: returns true if process is ok
    """
    # TODO complete this
    return False
