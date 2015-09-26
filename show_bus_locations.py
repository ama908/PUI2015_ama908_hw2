import json
import sys
import urllib2

if __name__ =='__main__':

   url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
   request = urllib2.urlopen(url)
   metadata = json.loads(request.read())

   bus_count = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
   #print (bus_count.keys())
   active_bus = len(bus_count)

   print "Bus Line : ", sys.argv[2]
   print "Number of Active Buses: " , active_bus

   bus = 0
    
   for i in range(active_bus):

       bus +=1

       latitude = bus_count[i]['MonitoredVehicleJourney']['VehicleLocation']["Latitude"]
       longitude = bus_count[i]['MonitoredVehicleJourney']['VehicleLocation']["Longitude"]

       print 'Bus %s is at longitude %s and latitude %s' % (bus, longitude, latitude)