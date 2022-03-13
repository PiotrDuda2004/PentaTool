from javascript import require, once, On
import multiprocessing
import time
import re
import os
import json


try:
    with open("config.json") as f:
        CONFIG = json.loads(f.read())
except Exception as e:
    print("Failed to load config.json!")
    print(e)
    exit()

mineflayer = require('mineflayer')

random_number = id([]) % 1000 # Give us a random number upto 1000
BOT_USERNAME = f'Steve_{random_number}'





def createBot(host,port):
    bot = mineflayer.createBot({ 'host': host, 'port': port, 'username': BOT_USERNAME, 'hideErrors': True, 'checkTimeoutInterval': 1*1000, 'version': CONFIG["MC_VERSION"]})
    once(bot, 'login')
    print("Found it! ")
    bot.quit()
    with open("MoreTrueOutput.txt","a") as blackie:
        blackie.write(("Server	")+host+":"+str(port)+'\n')
        blackie.close()


if __name__ == '__main__':
    with open("Output.txt","r") as file:
        for line in file:
            line = re.split('[:]',line)
            host = line[0]
            port = int(line[1])
            print("Checking "+host+":"+str(port))

            p = multiprocessing.Process(target=createBot, args=(host,str(port)))
            p.start()
            time.sleep(5)
            p.terminate()
            p.join()
            
