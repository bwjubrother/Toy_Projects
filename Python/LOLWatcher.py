from riotwatcher import LolWatcher
from datetime import datetime, timedelta
import time

lol_watcher = LolWatcher('RGAPI-c5797edc-d462-4f08-8ed3-83ee0e8a2178')

my_region = 'kr'

me = lol_watcher.summoner.by_name(my_region, '쵸비내안에서나가')

spectator = None

while True:
    print('[*] Checking...', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    try:
        spectator = lol_watcher.spectator.by_summoner(my_region, me['id'])

        start_time = datetime.fromtimestamp(spectator['gameStartTime'] / 1000)

        if datetime.now() - start_time < timedelta(minutes=5):
            print('[!] My son is playing LoL!', start_time.strftime('%Y-%m-%d %H:%M:%S'))
    except:
        pass

    time.sleep(5)