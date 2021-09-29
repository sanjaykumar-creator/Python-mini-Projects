import subprocess
import re
def collectdata():
    if_config_eth0 = str(subprocess.check_output("ifconfig eth0", shell=True))
    if_config_wlan0 = str(subprocess.check_output("ifconfig wlan0", shell=True))
    IP = str(subprocess.check_output("(hostname -I | awk '{print $1}')", shell=True))
    print("***********************************************************************************************")
    internetstatus(if_config_eth0, if_config_wlan0, IP)
    if "inet" in if_config_eth0 or "inet" in if_config_wlan0:
        r = input("Do u want to change the mac address (Y/N): ")
        if r == "y" or r == "Y":
            mac_changer(r)
        else:
            print("***********************************************************************************************")
    else:
        print("***********************************************************************************************")
def mac_add_eth0(if_config_eth0):
    mac_address = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(if_config_eth0))
    print("MAC ADDRESS: "+ mac_address.group(0))
def mac_add_wlan0(if_config_wlan0):
    mac_address = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(if_config_wlan0))
    print("MAC ADDRESS: " + mac_address.group(0))
def internetstatus(if_config_eth0,if_config_wlan0,IP,):

    if "inet" in if_config_eth0:
        print("STATUS: Online")
        print("INTERFACE: Ethernet (eth0)")
        print("IP Address: "+ IP(0))
        mac_add_eth0(if_config_eth0)

    elif "inet" in if_config_wlan0:
        print("STATUS: Online")
        print("INTERFACE: WIFI (wlan0)")
        print("IP Address: " + IP)
        mac_add_wlan0(if_config_wlan0)
    elif "inet" not in if_config_eth0 or "inet" not in if_config_wlan0:
        print("Offline")

    else:
        print("STATUS: Offline")
def mac_changer(r):
   try:
        if r=="Y" or r=="y":
            print()
            interface=input("please enter the interface: ")
            print()
            new_mac = input("enter the new mac: ")
            print()
            subprocess.check_output("ifconfig "+ interface+ " down", shell= True)
            subprocess.check_output("ifconfig "+ interface+" hw ether "+new_mac, shell= True)
            subprocess.check_output("ifconfig "+ interface+ " up", shell= True)
            print()
            print("MAC address successfully changed")
            print()
            print()
            collectdata()
   except subprocess.CalledProcessError:
            print()
            print("please re-enter the interface and mac address")
            mac_changer(r)
collectdata()