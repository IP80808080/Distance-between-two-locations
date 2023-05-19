from geopy.distance import geodesic

# Use "https://latitude.to/map/in/india/cities" this site to locate latitude and longitude of any place.

l1 = (17.3850, 78.4867)
l2 = (12.9716, 77.5946)

distance = int(geodesic(l1,l2).km)
print("")
print(distance, "kilometer")