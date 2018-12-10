import pexpect
import requests
from time import sleep

API_TOKEN = "2ca4ddd5-9cca-4076-bbe0-18457d419b45"
API_ENDPOINT = "https://graph.api.smartthings.com:443/api/smartapps/installations/85dbd7d6-33db-4804-9b10-0f81734289a3"
headers = {"Authorization":"Bearer "+API_TOKEN}
dbstring = "d34d269269249b4924934924924924924924e0"
#process = subprocess.Popen(shlex.split('rtl_433 -f 916800000 -q -X "Honeywell Doorbell:FSK_PCM:160:160:340,bits=149,match={4}0xe"'),stdout=subprocess.PIPE,universal_newlines=True,bufsize=1)
process = pexpect.spawn('rtl_433',['-f','916800000','-q','-X',"Honeywell Doorbell:FSK_PCM:160:160:340,bits=149,match={4}0xe"],timeout=None)

while True:
#    try:
#        process.expect('.*d34d269269249b4924934924924924924924e0.*',timeout=None)
#        r = requests.put(API_ENDPOINT+"/switches/on",headers=headers)
#        count = 0
#        while process.readline() and count <=27:
#             count +=1
#    except pexpect.exceptions.TIMEOUT:
#        print "ERROR!"
#        continue

    output = process.readline()
    if dbstring in output:
        r = requests.put(API_ENDPOINT+"/switches/on",headers=headers)
        sleep(1)
        while dbstring in output:
           output = process.readline()
