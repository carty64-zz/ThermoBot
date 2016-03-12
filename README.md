# ThermoBot

This repo is for the creation and documentation of **THERMOBOT**.

ThermoBot is a Raspberry Pi with a temperature sensor that connects to Slack and can respond to requests for temperature updates. Future upgrades to ThermoBot include a light sensor (which will help determine if the sensor is in direct sunlight) and a piezo buzzer (which will buzz at certain thresholds).

Currently, the sensor is connected and can get the temperature in C, F, and K. I still need to be able to create a program that will automatically retrieve the temperature values at given intervals and store them in a database. I have installed sqlite, but I don't know how to get them to talk to each other yet.

3/12/16 Update:
I have added an LCD display that is displaying the date, time, and temp in F and C with live updates. I have also added an LED to the board, but I don't know when it should light up yet.
