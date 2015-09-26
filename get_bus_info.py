import json
import sys
import urllib2
import csv

if __name__ == '__main__':

    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (
        sys.argv[1], sys.argv[2])
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    active_bus = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    bus_count = len(active_bus)

    print bus_count
    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)

        bus = 0

        for i in range(bus_count):
          bus += 1

          latitude = active_bus[i]['MonitoredVehicleJourney'][
              'VehicleLocation']["Latitude"]
          longitude = active_bus[i]['MonitoredVehicleJourney'][
              'VehicleLocation']["Longitude"]

          stop_Name = 'N/A'
          stop_Status = 'N/A'

          if active_bus[i]['MonitoredVehicleJourney']['OnwardCalls'] is not 0:
            stop_Status = active_bus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']["PresentableDistance"]
            stop_Name = active_bus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]["StopPointName"]

          writer.writerow([latitude, longitude, stop_Name, stop_Status])

