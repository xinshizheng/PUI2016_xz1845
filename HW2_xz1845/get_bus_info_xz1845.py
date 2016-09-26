from __future__ import print_function
import sys
import requests
import json
import csv

mta_key = sys.argv[1]
bus_line = sys.argv[2]
output_csv = sys.argv[3]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" \
      % (mta_key, bus_line)

response = requests.get(url)
data = response.content
dic_data = json.loads(data)

vehicle_activity = dic_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
number_of_bus = len(vehicle_activity)

with open(output_csv, 'w') as csvfile:
    fieldnames = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
    writer = csv.DictWriter(csvfile, lineterminator='\n', fieldnames=fieldnames)
    writer.writeheader()
    for i in range(number_of_bus):
        latitude = vehicle_activity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        longitude = vehicle_activity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        stop_info = vehicle_activity[i]['MonitoredVehicleJourney']['OnwardCall']
        stop_name = stop_info['OnwardCall'][1]['StopPointName']
        if stop_name == '':
            stop_name = 'N/A'
        stop_status = stop_info['OnwardCall'][1]['Extensions']['Distances']['PresentableDistance']
        if stop_status == '':
            stop_status = 'N/A'
        writer.writerow({'Latitude': latitude, 'Longitude': longitude, 'Stop Name': stop_name, 'Stop Status': stop_status})
