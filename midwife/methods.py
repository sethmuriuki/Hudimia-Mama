
def inputed_county(location, user_type, list_locations):
    '''
    Method that filters based on the inputed county of the current user
    '''
    if user_type == '1':
        requested_type = '2'
    else:
        requested_type = '1'
    list_county = []  # list of produce that match the current user's county requirements
    if requested_type == '2':
        for location in list_locations:
            if location.county  = (county):
                list_county.append(location)
    elif requested_type == '1':
        for county in list_locations:
            if location.county =(county):
                list_county.append(location)
    return list_county

def inputed_town(town, list_county):
    '''
    Method that filters based on the nearest town of the current user and returns a list of users matching that creteria
    '''
    list_town = []
    for location in list_county:
        if location.user.nearest_town == town:
            list_town.append(location)
    return list_town

def final_list(filtered_locations, list_county, list_town):
    '''
    Method that add all the list and truncates the location based on county,town
    and location  in that order
    '''
    final_list = list_town
    if len(final_list) < 5:
        final_list += [location for location in list_county if location not in list_town]
        if len(final_list) < 5:
            final_list += [location for location in list_town if product not in final_list]
            if len(final_list) < 5:
                final_list += [location for location in filtered_locations if location not in final_list]

    return final_list

def get_phonenumbers(final_list):
    '''
    Method that takes in a list of objects and returns the phonenumbers of the
    users associated with those locationsts as a string
    '''
    phonenumbers = {location.user.name: str(location.user.phonenumber) + '\n' +
                                       str(location.user.nearest_town) + '\n' + str(location.user.county) + "\n" + str(location.name)+ '@' +
                                       str(location.county) + '\n' for location in final_list}
    return phonenumbers

def details_generator(found_phonenumbers):
    '''
    Methods that takes in a dictionary of number and user_name and return numbers and user names as a string
    '''
    string = ''
    for item in found_phonenumbers:
        string += item + ' '
        string += found_phonenumbers[item] + '\n' + ' '

    for item in found_phonenumbers:
        details = []

    return string
