import os
from GenCode.schema import cfg_Tables
import json

class TableManager:
    def __init__(self):
        self.tables = cfg_Tables(self.loadTables)


    def loadTables(self,tableName:str):
        cwd = os.getcwd()
        return json.load(open(f'{cwd}/json/' + tableName + ".json", 'r', encoding="utf-8"))


tableManager = TableManager()
print(tableManager.tables.TbAttribute.getDataList())
