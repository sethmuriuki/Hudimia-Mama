def get_users(requested_users, county_users, ntown_users):
    county_users = []
    ntown_users = []

    for user in requested_users:
        if user.county == county_users:
            county_users.append(user)
        if user.ntown_users == ntown_users:
            ntown_users.append(user)

    if len(ntown_users) < 0:
        return county_users
    else:
        return ntown_users

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