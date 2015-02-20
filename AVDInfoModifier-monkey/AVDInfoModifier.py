import ConfigParser
import sys

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device_name = sys.argv[1]

print "AVD Info Modifier"
print "=============================================================="

print "Waiting for the device " + device_name + "...",

try:
    device = MonkeyRunner.waitForConnection()
    #device = MonkeyRunner.waitForConnection(10, device_name)
    testModel = device.getProperty('model')
except:
    device = None

if not device:
    print ""
    print "Cannot connect to the target device " + device_name + "."
    sys.exit(-1)
else:
    print "Connected"

print "Starting 008...",

#click dock button
device.touch(360, 1100, "DOWN_AND_UP")

#click 008 icon
device.touch(88, 256, "DOWN_AND_UP")

#wait the application start
MonkeyRunner.sleep(15)

print "Done"

print "Saving state...",

#click modify the data
device.touch(360, 400, "DOWN_AND_UP")

#click the save button
device.touch(50, 360, "DOWN_AND_UP")

#Back Home
device.touch(360, 1250, "DOWN_AND_UP")

print "Done"

#TODO: result checker.
#write a apk to save the current value into text file in sdcard
#then use monkey runner api to read this file.

'''
#device.removePackage('me.alfredis.helloworld')
#print "Removed"
#device.installPackage('helloworld.apk')
#print "Installed"

#device.startActivity(component='me.alfredis.helloworld/me.alfredis.helloworld.MainActivity')
print str(device.shell("more /storage/sdcard0/t.txt"))

print "Opened"

#result = device.takeSnapshot()

device.drag((672,27),(481,1666),3,10)
image = device.takeSnapshot()
sub_image = image.getSubImage((0, 0, 50, 100))
MonkeyRunner.sleep(5)
device.touch(402,126,"DOWN_AND_UP")
MonkeyRunner.sleep(5)
device.touch(805,100,"DOWN_AND_UP")
MonkeyRunner.sleep(5)
device.touch(531,730,"DOWN_AND_UP")
#result.writeToFile('./t.png')
#device.startActivity(component='me.alfredis.helloworld/.ApiDemos')
'''
