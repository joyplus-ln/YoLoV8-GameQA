import asyncio

import nest_asyncio
from adbutils import adb, AdbDevice

from Code.Log import log, Log
from Code.MissionManager import MissionManager
from Code.TableManager import TableManager
from Code.YoloFinder import YoloFinder

TableManager()
YoloFinder()
Log()

missionId = 13001

async def Start(device:AdbDevice):
    mission = MissionManager(missionId,device)
    asyncio.run(mission.Run())
    finish = False
    await asyncio.sleep(0.1)
    while finish is False :
        finish = mission.CheckMissionFinish()
        await asyncio.sleep(0.1)

nest_asyncio.apply()
devices = adb.device_list()
if devices:
    for device in devices:
        log.Info(f'{device.get_serialno()}')
        asyncio.run(Start(device))

