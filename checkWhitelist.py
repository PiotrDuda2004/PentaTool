from javascript import require, once, On
import multiprocessing
import time
import re
import os
import json
from colorama import Fore, init
from console_progressbar import ProgressBar 

red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lwhite = Fore.LIGHTWHITE_EX
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
reset = Fore.RESET
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN


try:
    with open("config.json") as f:
        CONFIG = json.loads(f.read())
except Exception as e:
    print("Failed to load config.json!")
    print(e)
    exit()


#Change to user-input variable 
lengthie = sum(1 for line in open('Output.txt'))
mineflayer = require('mineflayer')

random_number = id([]) % 1000 # Give us a random number upto 1000
BOT_USERNAME = f'Steve_{random_number}'
pb = ProgressBar(total=lengthie, decimals=3, length=50, fill='█', zfill='-')




def createBot(host,port):
    bot = mineflayer.createBot({ 'host': host, 'port': port, 'username': BOT_USERNAME, 'hideErrors': True, 'checkTimeoutInterval': 1*1000, 'version': CONFIG["MC_VERSION"]})
    once(bot, 'login')
    bot.quit()
    with open("MoreTrueOutput.txt","a") as blackie:
        blackie.write(("Server	")+host+":"+str(port)+'\n')
        blackie.close()


if __name__ == '__main__':
    with open("Output.txt","r") as file:
        for line in file:
            lengthie-=1
            line = re.split('[:]',line)
            host = line[0]
            port = int(line[1])
            minutes, seconds = divmod(lengthie*CONFIG["SEARCH_TIME"], 60)
            print ("\033[A                                             \033[A")
            print(f"{white}[{green}Start{white}]   {green}Checking "+host+":"+str(port)+(f" | Estimated time: {white}"+str(minutes)+f"{green} minutes {white}")+str(seconds+(CONFIG["SEARCH_TIME"])*2)+f"{green} seconds {white}|| {green}"+f"Found {yellow}"+str(sum(1 for line in open('MoreTrueOutput.txt')))+ f"{green} Servers")  #Generating message                                  
            #print("Found "+str(sum(1 for line in open('MoreTrueOutput.txt')))+ " Servers")
    
            pb.print_progress_bar(sum(1 for line in open('Output.txt'))-lengthie)

            p = multiprocessing.Process(target=createBot, args=(host,str(port)))
            p.start()
            time.sleep(5)
            p.terminate()
            p.join()