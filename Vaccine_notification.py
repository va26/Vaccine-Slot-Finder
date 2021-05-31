
import urllib.request, json
import os
from datetime import datetime
import time
import random


from slack import WebClient
def slack_message(message, channel):
    slack_token = os.environ['SLACK_BOT_TOKEN']
    client = WebClient(token=slack_token)

    response = client.chat_postMessage(channel=channel, text=message)

def get_info(center, session):
    name = center['name']
    pin = center['pincode']
    fee_type = center['fee_type']
    date = session['date']
    cap = session['available_capacity']
    vaccine = session['vaccine']
    
    if vaccine == "":
        vaccine = "Not Specified"
    
    info_str = "Found a slot!!!\nCenter Name: {}\nPincode: {}\nDate: {}\nFee Type: {}\nCapacity: {}\nVaccine: {}".format(name, pin, date,
                                                                                                        fee_type, cap, vaccine)
    
    return info_str

def get_slot(state, district, date):
    with urllib.request.urlopen("https://cdn-api.co-vin.in/api/v2/admin/location/states") as url:
        data= json.loads(url.read().decode())
        
    state_id = next((item for item in data["states"] if item["state_name"] == state), None)["state_id"]
    
    with urllib.request.urlopen("https://cdn-api.co-vin.in/api/v2/admin/location/districts/" + str(state_id)) as url:
        state_data = json.loads(url.read().decode())
    
    district_id = next((item for item in state_data["districts"] if item["district_name"] == district), None)["district_id"]
    
    with urllib.request.urlopen("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(district_id, date)) as url:
        center_data = json.loads(url.read().decode())
        
    found = 0
    sess_cnt = 0
    e_centers = 0
    for i in range(len(center_data['centers'])):
        center_found = 0
        for j in range(len(center_data['centers'][i]['sessions'])):
            if center_data['centers'][i]['sessions'][j]['min_age_limit'] == 18:
                sess_cnt += 1
                center_found = 1
            if center_data['centers'][i]['sessions'][j]['min_age_limit'] == 18 and center_data['centers'][i]['sessions'][j]['available_capacity'] > 0:
                slack_message(get_info(center_data['centers'][i], center_data['centers'][i]['sessions'][j]), "#vaccine_alert")
                found = 1
                break
        if center_found:
            e_centers += 1
        if found:
            break
        
    return found, sess_cnt, e_centers

state = "Karnataka"
district = "BBMP"

while True:
    date = datetime.today().strftime('%d-%m-%Y')
    found, sess_count, e_centers = get_slot(state, district, date)
    
    #print("No of eligible centers searched: {}\nNo of Sessions searched(total): {}".format(e_centers, sess_count))
    
    if found:
        slack_message("Slot found. Closing the API calls...", "#vaccine_alert")
        break
    
    random.seed(datetime.now())
    sec = random.randint(1, 10)
    time.sleep(sec)