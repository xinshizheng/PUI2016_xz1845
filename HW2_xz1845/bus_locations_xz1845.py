from __future__ import print_function
import sys
import requests
import json

mta_key = sys.argv[1]
bus_line = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" \
      % (mta_key, bus_line)

response = requests.get(url)
data = response.content
dic_data = json.loads(data)

vehicle_activity = dic_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
number_of_bus = len(vehicle_activity)

print("Bus Line : {}".format(bus_line))
print("Number of Active Buses : {}".format(number_of_bus))
for i in range(number_of_bus):
    latitude = vehicle_activity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = vehicle_activity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print("Bus {} is at latitude {} and longitude {}".format(i, latitude, longitude))
