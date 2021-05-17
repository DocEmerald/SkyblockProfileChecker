#Credit to __Zed (i don't know his Github), Chamos144, and many other members of the Hypixel Forums for originally building the basis of this script, which I expanded on
#Credit to Aspacesys for bringing it up, and DillPicklezzz for being the reason it was brought up
from urllib.request import urlopen
import json
import requests
import time


print("Your Hypixel API is required to access data. To retrieve it, 'run /api' or '/api new' on hypixel.net. \n Note that your API works for all users, no need to ask another user for their API so you can access their data.")

ApiKey = input("API Key: ")

Name = input("Minecraft Username: ")

ProfChoice = input("Profile Number (0 - 4): ")

TStamp = int(time.time()) 
TSTampOUT = str(TStamp)
print("Unix Timestamp: " + TSTampOUT)

UUIDGet = requests.get(
   "https://api.mojang.com/users/profiles/minecraft/" + Name + "?at=" + TSTampOUT).json() 
UUID = str(UUIDGet["id"])
print("Minecraft UUID: " + UUID)

Profnum = int(ProfChoice)

ProfileIdLink = requests.get("https://api.hypixel.net/player?key=" + ApiKey + "&uuid=" + UUID).json()
ProfileId = list(ProfileIdLink['player']['stats']['SkyBlock']['profiles'].keys())[Profnum] 
print("Internal Profile ID: " + ProfileId)

data = requests.get("https://api.hypixel.net/skyblock/profile?key=" + ApiKey + "&profile=" + ProfileId).json()
datan = urlopen("https://api.hypixel.net/skyblock/profile?key=" + ApiKey + "&profile=" + ProfileId)
dataco = datan.read()
datacon = json.loads(dataco)
fairy = False
coin = False
bal = False

try :
    CoinPurse = str(datacon['profile']['members'][UUID]['coin_purse'])
except KeyError:
    coin = True
try :
    Balance = str(datacon['profile']['banking']['balance'])
except KeyError:
    bal = True
try :
    FairySoulsCollected = str(datacon['profile']['members'][UUID]['fairy_souls_collected'])
except KeyError:
    fairy = True

if coin == False:
    print(Name + "'s purse contains: " + CoinPurse + " coins.")
elif coin == True:
    print(Name +" has their purse API disabled, or we ran into an error.")
if bal == False:
    print("There are " + Balance + " coins in the account.")
elif bal == True:
    print(Name + " has their balance API disabled, or we ran into an error.")
if fairy == False:
    print(Name + " has collected " + FairySoulsCollected + " Fairy Souls.")
elif fairy == True:
    print(Name + " has their Fairy Soul API disabled, or we ran into an error.")
