import os
import platform
import subprocess
import sys
from adbutils import adb

adb_path = "D:\\Softs\\Unity\\2022.3.22f1\\Editor\\Data\\PlaybackEngines\\AndroidPlayer\\SDK\\platform-tools\\adb.exe"
def run_adb_shell_command(command):
    # 构建完整的adb shell命令
    full_command = [adb_path, command]
    # 使用subprocess执行命令
    try:
        result = subprocess.check_output(full_command, stderr=subprocess.STDOUT, shell=False)
        return result # 将字节串解码为字符串并去除首尾空白字符
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {e}")
        return None


def run_adb_shell_command_byId(deviceid,command):
    # 构建完整的adb shell命令
    full_command = [adb_path,"-s",deviceid, command]
    # 使用subprocess执行命令
    try:
        result = subprocess.check_output(full_command, stderr=subprocess.STDOUT, shell=False)
        return result # 将字节串解码为字符串并去除首尾空白字符
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {e}")
        return None
#
def Collect_android_device_connected():
    """检查是否有Android设备连接"""
    devices = []
    result = run_adb_shell_command('devices').decode('utf-8').strip()
    lines = result.split('\n')
    for line in lines:
        if line.endswith('device'):
            devices.append(line.split()[0])
    return devices


def adb_screenshot(local_path):

    #local_path: 截图在本地的保存路径和文件名
    result = run_adb_shell_command(' shell /system/bin/screencap -p')
    if result is None:
        print("截图失败")
        return None
    else:
        # 将截图的二进制数据写入本地文件
        try:
            with open(local_path, 'wb') as f:
                f.write(result)
            print(f"截图已保存到: {local_path}")
        except Exception as e:
            print(f"保存截图到本地失败: {e}")

# adb_screenshot("D:\\temp\\1.png")
# is_android_device_connected()

def capture_android(device):
    # 执行screencap命令并保存截图到本地文件
    # 注意：screencap命令可能因Android版本和设备制造商的不同而有所差异
    screenshot_path_on_device = "/sdcard/screenshot.png"
    screenshot_path_on_host = "D:\\temp/screenshot.png"
    # 在设备上执行screencap命令
    # device.shell(f"screencap -p {screenshot_path_on_device}")
    # 从设备拉取截图文件到本地
    image = device.screenshot()
    return image





def execute_shell(shell):
    p = subprocess.Popen(shell, shell=True, stdout=subprocess.PIPE)
    out = p.stdout.readlines()
    return out

def Touch_android(deviceid,x,y):
    result = run_adb_shell_command_byId(deviceid,'input tap ' + x + " " + y)


# if __name__ == '__main__':
#     print(sys.argv)
#     if len(sys.argv) == 2:
#         device_id = sys.argv[1]
#         capture_android(sys.argv[1])
#         if ("Windows" in platform.platform()):
#             os.startfile("d:\\screenshot.png")

# devices = Collect_android_device_connected()
# for device in devices:
#     Touch_android(device,100,100)

# 确保ADB服务器已经启动，并且设备已经连接


def Get_ScreenShot():
    devices = adb.device_list()
    if devices:
        device = devices[0]  # 选择第一个连接的设备
        print(f"Connected device: {device}")
        return capture_android(device)
    else:
        print("No device connected.")
        return None

# # 模拟点击屏幕坐标 (x, y)
# x = 500
# y = 1000
# device.shell(f'input tap {x} {y}')