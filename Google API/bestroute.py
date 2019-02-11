import requests
import json
import geocoder
import math
import urllib.parse


class place:
    def __init__(self, init_lat = 0, init_long = 0, name = ""):
        self.name = name
        self.lat = str(init_lat)
        self.long = str(init_long)

def find_homeless_shelter(destination):

    picked_place = place()
    parameters_home = {"key" : "#insertapikeyhere#", "location" : destination.lat + "," + destination.long, "rankby" : "distance", "keyword" : "foodbank"}

    req_home = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?", params=parameters_home)
    jsonval = req_home.json()
    #print (jsonval)

    picked_place.lat = str(jsonval["results"][1]["geometry"]["location"]["lat"])
    picked_place.long = str(jsonval["results"][1]["geometry"]["location"]["lng"])
    picked_place.name = jsonval["results"][1]["name"]
    print("Picked Place Name: " + jsonval["results"][1]["name"])
    print("Picked Place Lat: " + str(picked_place.lat))
    print("Picked Plate Long: " + str(picked_place.long))
    #1 is used to avoid "highjinx" from picking up with coordinates 45.4245392,-75.701805 for demo
    print("")
    
    
    # for j in range(len(jsonval["results"])):
    # print(jsonval["results"][j]["name"])
    # print("")

    return picked_place
    
def find_restaurant (start, shelter, final_dest):
    #start -> restaurant -> shelter -> final_dest is the route
    picked_place = place()
    with open('C:\\Users\\lidar\\OneDrive - University of Waterloo\Hackathons\\2 - UOttaHacks 2019\\uOttaHack2019\\Google API\\test.json') as f:
        restaurant_list = json.load(f)


    minimum_index = 0
    lowest_time = 0
    for x in range(len(restaurant_list)):
        parameters_res = {"key" : "#insertapikeyhere#", "origin" : start.lat + "," + start.long, "destination" : final_dest.lat + "," + final_dest.long, "mode" : "driving", "waypoints" : str(restaurant_list[x]["lat"]) + "," + str(restaurant_list[x]["long"]) + "|" + shelter.lat + "," + shelter.long, "avoid" : "ferries|tolls"}
        req_res = requests.get("https://maps.googleapis.com/maps/api/directions/json?", params=parameters_res)
        jsonres = req_res.json()
        print("start: " + start.name + start.lat + "," + start.long)
        print("restaurant: " + restaurant_list[x]["name"] + " " + str(restaurant_list[x]["lat"]) + "," + str(restaurant_list[x]["long"]))
        print("shelter: "  + shelter.name + " " + shelter.lat + "," + shelter.long)
        print("final_dest: " + final_dest.name + " " + final_dest.lat + "," + final_dest.long)
        total_seconds = 0
        for y in range(len(jsonres["routes"][0]["legs"])):
            total_seconds = total_seconds + jsonres["routes"][0]["legs"][y]["duration"]["value"]
            #print("leg " + str(y) + ": " + str(total_seconds))
        
        if (x == 0):
            lowest_time = total_seconds
        elif (total_seconds < lowest_time):
            lowest_time = total_seconds
            minimum_index = x

        print(str(total_seconds/60) + " mins")

        #print("duration value: " + str(jsonres["routes"][0]["legs"][0]["duration"]["value"]))
        #print("duration text: " + jsonres["routes"][0]["legs"][0]["duration"]["text"])
        #print("start location: " + str(jsonres["routes"][0]["legs"][0]["steps"][0]["start_location"]["lat"]) + "," + str(jsonres["routes"][0]["legs"][0]["start_location"]["lng"]))
        #print("end location: " + str(jsonres["routes"][0]["legs"][0]["steps"][0]["end_location"]["lat"]) + "," + str(jsonres["routes"][0]["legs"][0]["end_location"]["lng"]))
        
        
        print("")

    print("Lowest time: " + str(math.ceil(lowest_time/60)) + " mins")
    print ("Fastest Restaurant: " + restaurant_list[minimum_index]["name"])

    picked_place.lat = str(restaurant_list[minimum_index]["lat"])
    picked_place.long = str(restaurant_list[minimum_index]["long"])
    return picked_place

def find_route(start, restaurant, shelter, finaldest):
    getVars = {"origin" : start.lat + "," + start.long, "destination" : finaldest.lat + "," + finaldest.long, "waypoints" : restaurant.lat + "," + restaurant.long + "|" + shelter.lat + "," + shelter.long}
    url = 'https://www.google.com/maps/dir/?api=1&'
    return url + urllib.parse.urlencode(getVars)


def main():
    my_location = geocoder.ip('me')
    final_destination = place(45.387536, -75.709345, "Canadian Agriculture and Food Museum")
    origin = place(str(my_location.lat), str(my_location.lng), "Marion Hall (MRN) ")
    homeless_shelter = find_homeless_shelter (final_destination)
    restaurant = find_restaurant (origin, homeless_shelter, final_destination)
    #print(restaurant.lat)
    #print(restaurant.long)
    #find_route returns url string
    route_url = find_route (origin, restaurant, homeless_shelter, final_destination)
    print("route url: " + route_url)
    #post_route_url = requests.post("localhost:/PickDriverPickup", data={'url': route_url, "remove_coordinates_lat" : restaurant.lat, "remove_coordinates_long" : restaurant.long})
    #print (post_route_url.status_code, post_route_url.reason)

if __name__ == "__main__":
    main()