from read_data import read_data 

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    id_list = []
    for i in data['messages']:
        if i['type'] == 'service':
            id_list.append(i['actor_id'])
        elif i['type'] == 'message':
            id_list.append(i['from_id'])
    return id_list
    
    
