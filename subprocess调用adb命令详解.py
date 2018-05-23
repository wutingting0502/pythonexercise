# coding=utf8
import os, subprocess
import re


def connectDevcie():
    '''检查设备是否连接成功，如果成功返回True，否则返回False'''
    try:
        '''获取设备列表信息，并用"\r\n"拆分'''
        deviceInfo = subprocess.check_output('adb devices').split("\r\n")
        deviceInfo = deviceInfo.decode('utf-8')
        '''如果没有链接设备或者设备读取失败，第二个元素为空'''
        if deviceInfo[1] == '':
            return False
        else:
            return True
    except Exception as e:
        print("Device Connect Fail:", e)


def getAndroidVersion():
    try:
        if connectDevcie():
            # 获取系统设备系统信息
            sysInfo = subprocess.check_output('adb shell cat /system/build.prop')
            sysInfo = sysInfo.decode('utf-8')
            # 获取安卓版本号
            androidVersion = re.findall("version.release=(\d\.\d)*", sysInfo, re.S)[0]
            androidVersion = androidVersion.decode('utf-8')
            return androidVersion
        else:
            return "Connect Fail,Please reconnect Device..."

    except Exception as e:
        print("Get Android Version:", e)


def getDeviceName():
    try:
        if connectDevcie():
            # 获取设备名
            deviceInfo = subprocess.check_output('adb devices -l')
            deviceName = re.findall(r'device product:(.*)\smodel', deviceInfo, re.S)[0]


            deviceName = deviceName.decode('utf-8')
            return deviceName
        else:
            return "Connect Fail,Please reconnect Device..."
    except Exception as e:
        print("Get Device Name:", e)


print (getDeviceName(), "\n", getAndroidVersion())