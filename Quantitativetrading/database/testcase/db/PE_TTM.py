import tushare as ts
import pyodbc
import pandas as pd
import numpy as np
import requests


def PE_TTM():
    tushare = ts.get_today_all()
    