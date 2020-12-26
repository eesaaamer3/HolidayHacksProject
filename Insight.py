from radar import RadarClient
from typing import Tuple
# initialize client with your project's secret key
SECRET_KEY = r"prj_test_sk_94074d07a4f84ea1670d2ceabb5ae3a0706eab4d"
PUBLIC_KEY = r'prj_test_pk_c4e161b1b185d10745b2b72e70aedbe837518436'
main_radar = RadarClient(SECRET_KEY, PUBLIC_KEY)

UofT_geofence = main_radar.geofences.get(tag='School', externalId=123)
my_house_geofence = main_radar.geofences.get(tag='Place', externalId=456)
abdus_user = main_radar.users.get(id='5fe60d18097c9b007650866b',
                                  userId='AF7C4486-E013-408B-BEEB-AB78012E71D9',
                                  deviceId='AF7C4486 - E013 - 408B - BEEB - AB78012E71D9')

eesa_user = main_radar.users.get(id='5fe60e529b22530098cb47d6',
                                 userId='455F95AF-FB74-4909-B459-F046225FDAE6',
                                 deviceId='455F95AF-FB74-4909-B459-F046225FDAE6')
