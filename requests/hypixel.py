import requests

print ("We need your Hypixel API key to access bank data.  "
       "The key can be found by joining Hypixel and running /api new, or /api.")

ApiKey = input ("Api Key: ")

Name = input ("Minecraft username: ")

ProfileIdLink = requests.get("https://api.hypixel.net/player?key=" + ApiKey +"&name=" + Name).json()
ProfileId = list(ProfileIdLink['player']['stats']['SkyBlock']['profiles'].keys())[0]

data = requests.get("https://api.hypixel.net/skyblock/profile?key=" + ApiKey + "&profile=" + ProfileId).json()
CoinPurse = str(data['profile']['members'][ProfileId]['coin_purse'])

print ("Balance is... " + CoinPurse)