from colorama import Fore, init
from sys import stdout
import os
init(strip=False)

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
{lblack}                                __   {cyan}   __________               __       ___________           .__
{lcyan}                              .d$$b     \______   \ ____   _____/  |______\__    ___/___   ____ |  |
{lblack}                            .' TO$;\  {cyan}   |     ___// __ \ /    \   __\__  \ |    | /  _ \ /  _ \|  |
{lcyan}                           /  : TP._;    |    |   \  ___/|   |  \  |  / __ \|    |(  <_> |  <_> )  |__
{lblack}                          / _.;  :Tb|  {cyan}  |____|    \___  >___|  /__| (____  /____| \____/ \____/|____/
{lcyan}                         /   /   ;j$j                  \/     \/          \/
{lblack}                     _.-"       d$$$$
{lcyan}                   .' ..       d$$$$;
{lblack}                  /  /P'      d$$$$P. |\
{lcyan}                 /   "      .d$$$P' |\^"l
{lblack}               .'           `T$P^""\"""  :
{lcyan}            ._.'      _.'                ;
{lblack}         `-.-".-'-' ._.       _.-"    .-"
{lcyan}      `.-\" _____  ._              .-"
{lblack}      -(.g$$$$$$$b.              .'
{lcyan}       ""^^T$$$P^)            .(:
{lblack}         _/  -"  /.'         /:/;
{lcyan}      ._.'-'`-'  ")/         /;/;
{lblack}   `-.-"..--""   " /         /  ;
{lcyan}  .-" ..--""        -'          :
{lblack}  ..--""--.-"         (\      .-(\
{lcyan}    ..--""              `-\(\/;`
{lblack}      _.                      :
{lcyan}                              ;`-
{lblack}                            :\
{lcyan}                           ; 
"""  

os.system("cls || clear")
print(menu)
os.system("pause")