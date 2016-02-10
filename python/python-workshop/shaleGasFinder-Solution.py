import json
import operator
from pprint import pprint
from json import dumps,loads, load
import sys
from operator import itemgetter

# Open the json file and print it
def get_json_data_from_file(file_name):
    with open(file_name) as jsonFile:
        return json.load(jsonFile)

# Print pretty JSON
def print_json_data(json_data):
    print json.dumps(json_data, indent=4, sort_keys = True)

# Print out the area specified by user input
def find_area_object_with_name(area_name, areas):
    for area in areas:
        if area["name"].lower() == area_name.lower():
            return area

# Get the total shale gas fields found for a specific area
def get_total_fields_found(year_data):
    total_fields = 0
    for value in year_data.itervalues() :
        total_fields = total_fields + value
    return total_fields

# Find and print the top five areas that have discovered the most shale gas fields
def get_top_areas(number_of_areas_needed, areas):
    for area in areas:
        year_data = area['newFields']
        total_for_area = get_total_fields_found(year_data)
        #add totalFieldsFound property to area dictionary so we can compare
        area['totalFieldsFound'] = total_for_area

    area_object = sorted(areas, key = lambda area: (area['totalFieldsFound']), reverse=True)
    area_object = area_object[:number_of_areas_needed]
    return area_object

# Save them to a json file
def write_json_to_file(jsonData, fileName):
    with open(fileName + '.json', 'w') as outfile:
        json.dump(jsonData , outfile, indent = 4)

# Upload it to our analytics server

def main():
    json_data = get_json_data_from_file("newFieldData.json")
    # print_json_data(json_data)
    #Print Area
    #print_json_data(json_data["areas"][0])
    areas = json_data['areas']
    #area_name = raw_input("Enter in the name of the area you are searching for: ")
    #area_data = find_area_object_with_name(area_name, areas)
    #total_for_area = get_total_fields_found(area_data["newFields"])
    number_of_areas_needed = int(raw_input("How many top areas do you want? "))
    top_areas = get_top_areas(number_of_areas_needed, areas)
    print "The top areas " + str(number_of_areas_needed) + " are:"
    print_json_data(top_areas)

    #Assign top areas to json object to
    json_data['areas'] = top_areas
    output_file_name = raw_input("Enter in the output file name for the analytics server: ")
    write_json_to_file(json_data, output_file_name)
    print "Wrote to \"" + output_file_name + ".json\""


############### MAIN ###############
if __name__ == "__main__":
    main()
