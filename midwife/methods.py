def get_users(requested_users, county_users, ntown_users):
    county_users_list = []
    ntown_users_list = []

    for user in requested_users:
        if user.location == county_users:
            county_users_list.append(user)
        if user.nearest_town == ntown_users:
            ntown_users_list.append(user)

    if len(ntown_users) < 0:
        return county_users
    else:
        return ntown_users


def final_list(requested_users, county_users, ntown_users):
    '''
    Method that add all the list and truncates the products based on priority in terms of price,town
    and location  in that order
    '''
    final_list = ntown_users
    if len(final_list) < 5:
        final_list += [user for user in county_users if user not in ntown_users]
        if len(final_list) < 5:
            final_list += [user for user in requested_users if user not in final_list]

    return final_list


def get_phonenumbers(final_list):
    '''
    Method that takes in a list of objects and returns the phonenumbers of the
    users associated with those products as a string
    '''
    phonenumbers = {users.user.name: str(users.user.phonenumber) + '\n' +
                                       str(users.user.nearest_town) + '\n' + str(users.user.location) + "\n" + str(users.name)+ '@' +
                                       str(users.price) + '\n' for users in final_list}
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