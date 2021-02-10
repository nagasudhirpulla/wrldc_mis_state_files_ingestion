from typing import Optional
from typing import Optional, Any
from openpyxl.worksheet.worksheet import Worksheet
import math

def getMeasData(sheetData: Worksheet, addresses: str, aggStrategy: Optional[str], equation: Optional[str]) -> Optional[float]:
    """get measurement value from file sheet data

    Args:
        sheetData (Worksheet): [description]
        addresses (str): [description]
        aggStrategy (Optional[str]): [description]
        equation (Optional[str]): [description]

    Returns:
        Optional[float]: [description]
    """    
    # split the addresses by comma
    addressList = addresses.split(',')
    addressList = [x.strip() for x in addressList]

    # get the values in a list
    valuesList = [sheetData[a].value for a in addressList]

    # check if aggStrategy is present, if present perform aggregation
    if (aggStrategy is not None) and (aggStrategy.lower() == "average"):
        valuesList = [sum(valuesList) / len(valuesList)]

    if (aggStrategy is not None) and (aggStrategy.lower() == "sum"):
        valuesList = [sum(valuesList)]

    # check if equation is present, if present evaluate equation
    if equation != 'nan':
        subEquation = equation
        for itr, val in enumerate(valuesList):
            subEquation = subEquation.replace("{{"+str(itr)+"}}", str(val))
        valuesList = [eval(subEquation)]

    # return the value
    return valuesList[0]
