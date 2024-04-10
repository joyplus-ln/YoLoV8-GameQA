import asyncio

from adbutils import AdbDevice

from Code import Log
from Code.GameAction import GameAction
from Code.Log import log
from Code.TableManager import tableManager
from GenCode.schema import MissionConfig


class MissionManager:
    def __init__(self,missionId:int,device:AdbDevice):
        self.missionId = missionId
        self.missionFinish = False
        self.device = device
        self.action:GameAction = None
        self.actionIndex = 1
        self.missionConfig:MissionConfig = tableManager.tables.MissionTable.get(self.missionId)
        self.checkFinishAction = GameAction(self.missionConfig.FinishAction,self.device)


    def createAction(self,actionId:int):
        return GameAction(actionId,self.device)

    #循环检测mission
    async def Run(self):
        log.Info(f'GameAction Start {self.missionConfig.mission.get(self.actionIndex)}')
        if self.action is None:
            self.action = self.createAction(self.missionConfig.mission.get(self.actionIndex).ActionId)
            asyncio.run(self.action.Run())
        while  self.missionFinish is False:
            self.check()
            await self.checkFind()
            await asyncio.sleep(0.05)
            asyncio.run(self.Run())


    def check(self):
        if self.action.Check() :
            self.actionIndex += 1
            if self.missionConfig.mission.get(self.missionConfig.mission.get(self.actionIndex).ActionId) is None :
                self.actionIndex = 1
            self.action = None


    async def checkFind(self):
        find:bool = await self.checkFinishAction.Run()
        if find is not False :
            self.missionFinish = True


    def CheckMissionFinish(self):
        return self.missionFinish
