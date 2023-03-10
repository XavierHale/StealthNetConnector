from os import system
import winwifi
import time
ssid="DIRECT-ST341THN3T-OfficeJet-Pro1337"
passw=""
title="StealthNet"
system("title " + title)
print("StealthNet Connector Version 1.0")
wifi=winwifi
wifi.WinWiFi.connect(ssid, passw)
input('Press enter to disconnect from StealthNet and connect to CCPS-Internal: ')
ssid="CCPS-Internal"
wifi.WinWiFi.connect(ssid, passw)
print("Recconected, erasing StealthNet connection...")
time.sleep("101")
