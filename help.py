import os
import pandas as pd
import numpy as np
import sys
import json
import ipywidgets as widgets
#import voila
from IPython.display import display
from datetime import datetime
from urllib.request import urlopen

all_DF = []

def setData(df):
    global all_DF
    dataTypes = []
    for typ in df['valueDetailList']:
        all_DF.append([typ['type'],pd.DataFrame(typ['valueInfoList'])])
        dataTypes.append(typ['type'])
    return all_DF
    #display(all_DF[0][1].cross_map_header)
def showData(typ):
    for df in all_DF:
        if typ in df[0]:
            print("Below is the {} info".format(typ))
            display(df[1])