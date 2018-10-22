"""
Brad Duvall
1/11/17
Website Blocker based on time of day and websites listed

"""

import time
from datetime import datetime as dt #sets the datetime methods as dt


#r prefix tells python it is a raw string (no special characters).  Or can use \\ for each folder
host_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect="127.0.0.1"
website_list=["www.facebook.com","wtfuun.tumblr.com/","www.nexusmods.com/skyrim/?","www.nexusmods.com/skyrimspecialedition/?"]



while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,7) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,8):


        with open(host_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
            #print(content)


    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list): #learn about any()
                    file.write(line)
                file.truncate()


    time.sleep(30)   #waits # of seconds
