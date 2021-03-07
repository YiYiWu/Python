import os,string,time
from ctypes import windll
from datetime import datetime

def get_drive_status():
    devices = []
    #The GetLogicalDrives function retrieves a bitmask
    #representing the currently available disk drives.
    record_deviceBit = windll.kernel32.GetLogicalDrives()
    for label in string.ascii_uppercase : #The uppercase letters 'A-Z'
        if record_deviceBit & 1:
            devices.append(label)
        record_deviceBit >>= 1
    return devices

def detect_device():
        original = set(get_drive_status())
        time.sleep(3)
        add_device =  set(get_drive_status())- original
        subt_device = original - set(get_drive_status())
        f = open("log.txt", "a")
        if (len(add_device)):
            for drive in add_device:
                f.write("The drives added: {0} at {1}.\n".format(drive, datetime.now()))

        elif(len(subt_device)):
            for drive in subt_device:
                f.write("The drives removed: {0} at {1}.\n".format(drive, datetime.now()))
        f.close()

if __name__ == '__main__':
    while True:
        detect_device() 