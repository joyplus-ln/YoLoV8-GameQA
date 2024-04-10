import asyncio

from Code.TableManager import TableManager
from Code.YoloFinder import YoloFinder

tableManager = TableManager()
yoloModel = YoloFinder()


missionId = 13001

async def Start():
    from Code.MissionManager import MissionManager
    mission = MissionManager(missionId)
    asyncio.run(mission.Run())
    finish = False
    while finish is False :
        finish = mission.CheckMissionFinish()
        await asyncio.sleep(0.1)

