from utils import queryCDA
import pandas as pd
import json

def retreive_ts_group(apiRoot,p_group_id,p_category_id,p_office_id,dataframe=True):
    
    endPoint = f'/timeseries/group/{p_group_id}'
    
    params = {
        "office": p_office_id,
        "category-id": p_category_id
    }
    
    headerList={
        "Accept": "application/json"
    }
    
    responce = queryCDA(apiRoot+endPoint,params,headerList).json()
    
    if dataframe:
        responce = pd.DataFrame(responce['assigned-time-series'])
        
    return responce

def retrieve_ts(apiRoot,p_tsId,p_office_id=None,p_unit=None,p_datum=None,p_start_date=None,p_end_date=None,p_timezone=None,dataframe=True,p_page_size=500,):
    #creates the dataframe from the timeseries data
    endPoint = '/timeseries'
    if p_start_date is not None: p_start_date = p_start_date.strftime('%Y-%m-%dT%H:%M:%S')
    
    if p_end_date is not None: p_end_date = p_end_date.strftime('%Y-%m-%dT%H:%M:%S') 
    
    params = {
        "office": p_office_id,
        "name": p_tsId,
        "unit": p_unit,
        "begin": p_start_date,
        "end": p_end_date,
        "page-size" : p_page_size
    }
    
    headerList={
        "Accept": "application/json;version=2"
    }
    responce = queryCDA(apiRoot+endPoint,params,headerList).json()
    
    if dataframe:
        responce = pd.DataFrame(responce['values'], columns = ["date_time","val","quality_code"])
        responce.date_time = pd.to_datetime(responce.date_time, unit='ms')
        responce=responce.set_index('date_time')
    return responce
