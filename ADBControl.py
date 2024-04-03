import os
import platform
import subprocess
import sys

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


def is_android_device_connected():
    """检查是否有Android设备连接"""
    result = run_adb_shell_command('devices').decode('utf-8').strip()
    for i in range(1, len(result) - 1):
        if result[i].startswith("*") and result[i].endswith("*"):
            pass
        else:
            print(result[i].split("\t"))


# # 检查是否有设备连接
# if is_android_device_connected():
#     # 执行ADB Shell命令
#     output = run_adb_shell_command('ls /sdcard/')
#     if output:
#         print(f"命令输出: {output}")
#     else:
#         print("命令执行失败")
# else:
#     print("没有设备连接")

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

def capture_android(device_id):
    sh1 = "adb -s " + device_id + " shell /system/bin/screencap -p /sdcard/screenshot.png"
    sh2 = "adb -s " + device_id + " pull /sdcard/screenshot.png d:/screenshot.png"
    execute_shell(sh1)
    execute_shell(sh2)


def execute_shell(shell):
    p = subprocess.Popen(shell, shell=True, stdout=subprocess.PIPE)
    out = p.stdout.readlines()
    return out


# if __name__ == '__main__':
#     print(sys.argv)
#     if len(sys.argv) == 2:
#         device_id = sys.argv[1]
#         capture_android(sys.argv[1])
#         if ("Windows" in platform.platform()):
#             os.startfile("d:\\screenshot.png")
is_android_device_connected()