#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from time import sleep, time, strftime, localtime
from datetime import datetime
import usbiss
import opc

# Get arguments
if len(sys.argv) != 2:
    print('Usage: {} dev-path'.format(sys.argv[0]))
    sys.exit(1)

# Port
port = sys.argv[1]

# Sample period
period = 10

# Open connection to USB-ISS in SPI mode.
usb = usbiss.USBISS(port, 'spi', spi_mode=2, freq=500000)

# Give the USB connection to py-opc
alpha = opc.OPCN2(usb)

# Toggle to tur on properly
alpha.off()
sleep(1)

alpha.on()
sleep(1)

# log data
lastUpdated = 0

# data
latitude = str(37.295912)
longitude = str(126.975706)

latitude_file = open("latitude", 'w')
longitude_file = open("longitude", 'w')
latitude_file.write(latitude)
longitude_file.write(longitude)
latitude_file.flush()
longitude_file.flush()

try:
    while True:
        curTime = time()
        if (curTime-lastUpdated) >= period:
            lastUpdated = curTime

            # Get histogram
            data = alpha.histogram()

            # tnow = datetime.fromtimestamp(curTime).strftime("%Y-%m-%d %H:%M:%S")
            tnow = datetime.fromtimestamp(curTime)

            try:
                t = str(tnow)[0:19]
                pm1 = str(data['PM1'])
                pm2 = str(data['PM2.5'])
                pm10 = str(data['PM10'])
            except:
                continue

            t_file = open('time', 'w')
            pm1_file = open('pm1', 'w')
            pm2_file = open('pm2', 'w')
            pm10_file = open('pm10', 'w')

	    print('pm1 : ' + pm1)
	    print('pm2 : ' + pm2)
	    print('pm10 : ' + pm10)

            # Write to file
            t_file.write(t)
            pm1_file.write(pm1)
            pm2_file.write(pm2)
            pm10_file.write(pm10)

            t_file.flush()
            pm1_file.flush()
            pm2_file.flush()
            pm10_file.flush()

            alpha.off()

except KeyboardInterrupt:
    f.close()
    alpha.off()
    usb.close()
