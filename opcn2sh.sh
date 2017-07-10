#!/bin/sh

sudo python opcn2.py /dev/serial/by-id/usb-Devantech_Ltd._USB-ISS._00018223-if00 &

sleep 5

while [ 1 ]; do
    sleep 10
    node opcn2server.js &
done
