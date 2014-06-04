#!/usr/bin/python
import subprocess
import os
import time
import RPi.GPIO as GPIO
import logging
from datetime import datetime

d = datetime.now()
initYear = "%04d" % (d.year) 
initMonth = "%02d" % (d.month) 
initDate = "%02d" % (d.day)
initHour = "%02d" % (d.hour)
initMins = "%02d" % (d.minute)
# solo cambiar la direccion de destino
folderToSave = "/media/usb/Timelapse_" + str(initYear) + str(initMonth) + str(initDate) + str(initHour) + str(initMins)
os.mkdir(folderToSave)

logging.basicConfig(filename=str(folderToSave) + ".log",level=logging.DEBUG)
logging.debug(" R A S P I L A P S E C A M -- Started Log for " + str(folderToSave))

list_ex  = ['off','auto','night','backlight','spotlight','fireworks']
list_awb = ['off','auto','sun','cloud','shade','tungsten','fluorescent','incandescent','flash','horizon']

# EV level
photo_ev = 0

# Photo dimensions and rotation
photo_width  = 1920
photo_height = 1080
#photo_width  = 800
#photo_height = 600
photo_rotate = 0
fileSerial = 1
photo_interval = 2    # Interval between photos (seconds)
photo_counter  = 0    # Photo counter
a = range (0, 1200)
total_photos = len(a) 

# Delete all previous image files
try:
  os.remove("photo_*.jpg")
except OSError:
  pass

# Lets start taking photos!
try:

  print "Starting photo sequence"

  for ex in  a:
   # Set FileSerialNumber to 000X using four digits
   fileSerialNumber = "%04d" % (fileSerial)
   # Capture the CURRENT time (not start time as set above) to insert into each capture image filename
   hour = "%02d" % (d.hour)
   mins = "%02d" % (d.minute)
   photo_counter = photo_counter + 1
   cmd = 'raspistill -n -q 100 -t 1000 -o ' + str(folderToSave) + '/' + str(fileSerialNumber) +  '.jpg  -w ' + str(photo_width) + ' -h ' + str(photo_height) + ' -awb auto -mm average' 
   logging.debug(' Image saved: ' + str(folderToSave) + "/" + str(fileSerialNumber) + "_" + str(hour) + str(mins) +  ".jpg")
   pid = subprocess.call(cmd, shell=True)
   print ' [' + str(photo_counter) + ' of ' + str(total_photos) + '] ' 
   fileSerial += 1 
   time.sleep(photo_interval)
  
  print "Finished photo sequence"
  
except KeyboardInterrupt:
  # User quit
  print "Goodbye!"

  #Ejecutar con > Python pi_timelapse.py &
