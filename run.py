import json
import requests
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_token_list():
    url = "http://www.clanker.world/api/tokens"
    response = requests.get(url, verify=False)

    data = response.json()

    fids = []
    dataAwal = []
    for token in data['data']:
        fids.append(str(token['requestor_fid']))
        dataAwal.append(token)

    url = 'http://www.clanker.world/api/get-multiple-users-by-fid?fids=' + ','.join(fids)
    response = requests.get(url, verify=False)
    data = response.json()
    for idx, user in enumerate(data['users']):
        print("==========================")
        print('Nama Token       : '+dataAwal[idx]['name'])
        print('Simbol           : '+dataAwal[idx]['symbol'])
        print('Contract Address : '+dataAwal[idx]['contract_address'])
        print('Username WP      : '+json.dumps(user.get('username')))
        print('Total Followers  : '+json.dumps(user.get('follower_count')))

if __name__ == '__main__':
    print(u"░█▀▀░█░░░█▀█░█▀█░█░█░█▀▀░█▀▄░░░█▀▄░█▀▀░▀█▀░█▀▀░█▀▀░▀█▀\n"
          u"░█░░░█░░░█▀█░█░█░█▀▄░█▀▀░█▀▄░░░█░█░█▀▀░░█░░█▀▀░█░░░░█░\n"
          u"░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░░░▀▀░░▀▀▀░░▀░░▀▀▀░▀▀▀░░▀░\n\n")
    i = 0
    while True:
        try:
            i += 1
            print("***********************")
            print("Scan number " + str(i))
            get_token_list()
        except Exception as e:
            print(e)
        input("Press Enter to rescan...")


