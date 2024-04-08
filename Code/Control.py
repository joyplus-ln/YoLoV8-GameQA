import asyncio

import pyautogui




async def MoveAsync(x, y, time):
    i = 10
    while(i > 0):
        pyautogui.move(x, y)
        await asyncio.sleep(time)
        i-=1


asyncio.run(MoveAsync(100,100,0.1))