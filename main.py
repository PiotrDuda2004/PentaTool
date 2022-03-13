
from colorama import Fore, init
import requests
import json
import os

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


# Shodan search query endpoint
API_URL = "https://api.shodan.io/shodan/host/search"

# results per page
PAGE_SIZE = 100


# user config loaded from config.json
CONFIG = {}
with open('MoreTrueOutput.txt', 'a') as the_file:
    the_file.truncate(0)

def do_request(page_num):
    # construct API request
    api_params = {
        "key": CONFIG["API_KEY"],
        "page": page_num,
        "query": "Minecraft"
    }

    if CONFIG["MC_VERSION"] != "":
        api_params["query"] = "Minecraft " + CONFIG["MC_VERSION"]

    result = requests.get(API_URL, params=api_params)

    if result.status_code == 401:
        print("Error 401 from Shodan, your API key is most likely incorrect.")
        print("Go to https://account.shodan.io/ and copy the API key into")
        print("your config.json correctly.")
        exit()

    result = result.json()
    if "error" in result:
        # API call returned an error
        print("SHODAN ERROR: " + result["error"])
        return None

    return result

def parse_page(page_json):
    result = []
    for server in page_json["matches"]:
        if CONFIG["ACTIVE_ONLY"]:
            if "Online Players: 0" in server["data"]:
                continue

        ip = server["ip_str"]
        port = str(server["port"])
        result.append(ip + ":" + port)
    return result

if __name__ == "__main__":
    try:
        with open("config.json") as f:
            CONFIG = json.loads(f.read())
    except Exception as e:
        print("Failed to load config.json!")
        print(e)
        exit()

    if CONFIG["API_KEY"] == "":
        print("API_KEY must be set!")
        print("Create a free account at https://shodan.io/ and")
        print("put your API key in config.json.")
        exit()

    if CONFIG["PAGES"] < 1:
        print("PAGES must be greater than 0.")
        exit()

    print(f"{reset}{green}Searching for servers...")
    server_results = []
    for i in range(CONFIG["PAGES"]):
        resp = do_request(i + 1)

        if resp is not None:
            ips = parse_page(resp)
            server_results.extend(ips)

    if CONFIG["OUTPUT_FILE"] == "":
        # print results to stdout
        for ip in server_results:
            print(ip)
    else:
        try:
            with open(CONFIG["OUTPUT_FILE"], "w") as f:
                for ip in server_results:
                    f.write(ip + "\n")
            os.system("checkWhitelist.py 1")
            os.system('cd go-serversdat-master & go run main.go -u -d '+CONFIG["MC_PATH"]+'"Vanilla_"'+CONFIG["MC_VERSION"]+'"/.minecraft/servers.dat"')
        except Exception as e:
            print("Failed to open output file!")
            print(e)
            exit()
