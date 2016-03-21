#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime
#from w1thermsensor import W1ThermSensor
from w1thermsensor import *
import sqlite3
import subprocess

conn = sqlite3.connect('../../tempdatabase.db')
c = conn.cursor()
lcd = Adafruit_CharLCD()
lcd.begin(16, 1)
sensor = W1ThermSensor()
#temp_k = sensor.get_temperature(W1ThermSensor.KELVIN)

lcd.clear()

n = 0

while n < 5:
  temp_all = sensor.get_temperatures([W1ThermSensor.DEGREES_F,W1ThermSensor.DEGREES_C])
#  f = sensor.get_temperature(W1ThermSensor.DEGREES_F)
#  temp_f = sensor.get_temperature(W1ThermSensor.DEGREES_F)
#  temp_c = sensor.get_temperature(W1ThermSensor.DEGREES_C)
  lcd.message(datetime.now().strftime('%b %d  %l:%M %p\n'))
  lcd.message('  %.1fF  %.1fC' % (round(temp_all[0], 1),round(temp_all[1], 1)))
  lcd.home()
  t = (round(temp_all[0], 1))
  zone = "bedroom"
#  print t
#  print zone 
#  print type(t)
#  print type(zone)
#  print len(t)
#  print len(zone)
  c.executemany('INSERT INTO temps (time, date, temp, zone) VALUES (time(),date(),%f,%s)' % (t, zone),)
  sleep(5)
  n = n + 1

conn.commit()
