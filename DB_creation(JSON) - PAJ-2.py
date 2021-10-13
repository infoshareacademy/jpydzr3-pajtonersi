import json

def from_JSON_and_to_JSON():

    # Open 'JSON_users_list.json' file
    with open('JSON_users_list.json') as json_file:
        #Load its content and save to a new dictionary
        data = json.load(json_file)
        print(data)

    # Simulation of deleted data (in the dict "data") by admin
    #add or delete
    #data["Adrian"] = "password"
    #del data["Adrian"]["password"]
    print(data)

    # Open 'JSON_users_list.json', update dict = data, and save all changes back to 'JSON_users_list.json'
    with open('JSON_users_list.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    from_JSON_and_to_JSON()
