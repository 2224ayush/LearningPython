import os
from datetime import datetime
import time
def sthdwn():

    x=int(input("enter hour: "))
    y=int(input("enter minute: "))
    while True:
        now=datetime.now().time()
        if now.hour==x and now.minute==y:
            print("Shutting down..")
            os.system("shutdown -s")
            break
        else:
            print("current time",now)
            time.sleep(60)
sthdwn()