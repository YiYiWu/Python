import os,string,time
from ctypes import windll

def get_driveStatus():
    devices = []
    record_deviceBit = windll.kernel32.GetLogicalDrives()#The GetLogicalDrives function retrieves a bitmask
    #representing the currently available disk drives.
    for label in string.ascii_uppercase : #The uppercase letters 'A-Z'
        if record_deviceBit & 1:
            devices.append(label)
        record_deviceBit >>= 1
    return devices

def detect_device():
        original = set(get_driveStatus())
        # print ('Detecting...')
        time.sleep(3)
        add_device =  set(get_driveStatus())- original
        subt_device = original - set(get_driveStatus())

        if (len(add_device)):
            print ("There were {} devices.".format(len(add_device)))
            for drive in add_device:
                print ("The drives added: {0}.".format(drive))

        elif(len(subt_device)):
            print ("There were {} devices.".format(len(subt_device)))
            for drive in subt_device:
                print ("The drives removed: {0}.".format(drive))
                    
if __name__ == '__main__':
    while True:
        detect_device() 