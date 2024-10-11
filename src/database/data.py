import pandas as pd
from decouple import config
from src.models.prototypes import SheetObject,Sheet

def DataBase(df, sheet):
    if not df.isnull().all().all():
        df = df.dropna(axis=0,how='all')
        fields= ["register","title","author","year_edition","ISBN_ISSN","editorial","page","colection","city","ejem","support","type_support","materia","location","observations"] #df.iloc[0,:].values
        df = df.iloc[1:,]
        data = df.values
        return SheetObject(sheet,fields,data).constructor()
    return None



def getDataBase(sheet):
    path = config('PATH_RELATIVE_EXCEL')
    file = pd.ExcelFile(path,engine='openpyxl')
    
    try:
        df_sheet = file.parse(sheet_name=sheet,header=None)
        object_sheet = DataBase(df_sheet,sheet)
        return object_sheet
    except Exception:
        return None

def getSheets():
    path = config('PATH_RELATIVE_EXCEL')
    file = pd.ExcelFile(path, engine='openpyxl')
    sheets_names= file.sheet_names
    json = [Sheet(object,i).constructor() for i,object in enumerate(sheets_names)]
    return json

