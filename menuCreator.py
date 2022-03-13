from colorama import Fore, init, Back
import os
import json

init(strip=False)
os.system("cls || clear")



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


menu = rf""" 
{lblack}                                __   {lgreen}   __________               __       ___________           .__
{green}                              .d$$b     \______   \ ____   _____/  |______\__    ___/___   ____ |  |
{lyellow}                            .' TO$;\  {lgreen}   |     ___// __ \ /    \   __\__  \ |    | /  _ \ /  _ \|  |
{green}                           /  : TP._;    |    |   \  ___/|   |  \  |  / __ \|    |(  <_> |  <_> )  |__
{lblack}                          / _.;  :Tb|  {lgreen}  |____|    \___  >___|  /__| (____  /____| \____/ \____/|____/
{green}                         /   /   ;j$j                  \/     \/          \/
{lblack}                     _.-"       d$$$$
{lyellow}                   .' ..       d$$$$;
{lwhite}                  /  /P'      d$$$$P. |\
{green}                 /   "      .d$$$P' |\^"l    
{lblack}               .'           `T$P^""\"""  :
{green}            ._.'      _.'                ;                            {lyellow} Discord: Bloody#3521 {Back.BLACK} 
{lblack}         `-.-".-'-' ._.       _.-"    .-"                           {lyellow} Github: PiotrDuda2004
{lyellow}      `.-\" _____  ._              .-"
{lwhite}      -(.g$$$$$$$b.              .'
{green}       ""^^T$$$P^)            .(:
{lblack}         _/  -"  /.'         /:/;
{green}      ._.'-'`-'  ")/         /;/;
{lblack}   `-.-"..--""   " /         /  ;
{lyellow}  .-" ..--""        -'          :
{lwhite}  ..--""--.-"         (\      .-(\
{green}    ..--""              `-\(\/;`
{lblack}      _.                      :
{green}                              ;`-
{lblack}                            :\
{lyellow}                           ; 
"""  

help_message = f"""
{lgreen}     ╔══════════════════════════════════╗                          
{lgreen}     ║  {lwhite} ► Commands: {lgreen}                   ║
{lgreen}     ║                                  ║
{lgreen}     ║  {lblack} • start {lgreen}                       ║
{lgreen}     ║  {lblack} • showconfig  {lgreen}                 ║
{lgreen}     ║  {lblack} • editconfig  {lgreen}                 ║
{lgreen}     ║  {lblack} • cls    {lgreen}                      ║
{lgreen}     ║                                  ║
{lgreen}     ╚══════════════════════════════════╝"""





def commandListening():
    argument = input().split()
    
    command = argument[0]
    if len(argument) == 0:
        print(f"\n   Unknown command. Type help to see the available commands.")
    elif command.lower() == "cls" or command.lower() == "clear":
         os.system("cls || clear")
         print(menu)
    elif command.lower() == "help":
        print(help_message)
    elif command.lower() == "showconfig":
        try:
            with open("config.json") as f:
                CONFIG = json.loads(f.read())
                print(json.dumps(CONFIG, indent=4, sort_keys=True))
        except Exception as e:
            print("Failed to load config.json!")
            print(e)
            exit()
    elif command.lower() == "editconfig":    
        os.system('notepad.exe config.json')
    elif command.lower() == "start":
        os.system('main.py')


if __name__ == "__main__":
    os.system("clear || cls & title PentaTool")
    print(menu)
    while True:
        if os.name == "nt":
            py = "python"
            print(f"\n {reset}{green}    root@windows:~/PentaTool# {lblack}» {white} ", end="")
            commandListening()
        else:
            py = "python3"
            print(f"\n {reset}{green}    root@linux:~/PentaTool# {lblack}» {white} ", end="")
            commandListening()