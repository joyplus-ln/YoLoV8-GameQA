import asyncio

from adbutils import AdbDevice

from Code.Init import tableManager, yoloModel


class GameAction():
    def __init__(self,actionId:int,device:AdbDevice):
        self.actionId = actionId
        self.device = device
        self.finish = False

        # 检测逻辑
    def Check(self):
        return self.finish

    async def Run(self):

        from GenCode.schema import ActionConfig
        def _predict(actionConfig: ActionConfig):
            from Code.ADBControl import capture_android
            results = yoloModel.predict(capture_android(self.device),actionConfig.classList,actionConfig.conf)
            if results.count() > 0:
                for result in results:
                    infos = result.summary()
                    for info in infos:
                        print(info)
                        centx = (info["box"].get("x1") + info["box"].get("x2")) / 2
                        centy = (info["box"].get("y1") + info["box"].get("y2")) / 2
                        from Code.ADBControl import Click_Screen
                        Click_Screen(self.device, centx + actionConfig.click_offset_x, centy + actionConfig.click_offset_y)
                return True
            return False

        from GenCode.schema import ActionConfig
        actionConfig: ActionConfig = tableManager.tables.TbActions.get(self.actionId)
        if actionConfig.beforeDelay > 0:
            await asyncio.sleep(actionConfig.beforeDelay)
        for number in range(actionConfig.predictTimes):
            find = _predict(actionConfig)
            if find is True:
                await asyncio.sleep(actionConfig.afterDelay)
                self.finish = True
                break
            await asyncio.sleep(actionConfig.predictTimesDuration)
        self.finish = True