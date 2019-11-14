import postcodes_io_api

api = postcodes_io_api.Api(debug_http=False, timeout=None, base_url=None)

def menu():

    choice = input("""
                    Postcode finder
                      1: Find a Postcode
                      2: Find nearest postcodes
                      3: exit

                      Please enter your choice: """)
    if choice == '1':
        ask_for_postcode()
    if choice == '2':
        get_nearest_postcode()
    if choice == '3':
        exit()


def ask_for_postcode():
    postcode = input("Enter a valid postcode: ")
    get_a_postcode(postcode)


def get_a_postcode(postcode):
    data = api.is_postcode_valid(postcode)
    if data == False:
        print('Invalid postcode')
    else:
        postcode_data = api.get_postcode(postcode)
        data = get_data_postcode(postcode)
        return data


def get_data_postcode(postcode):
    data = api.is_postcode_valid(postcode)

    if data == False:
        print('Invalid postcode')
    else:
        postcode_data = api.get_postcode(postcode)
        result = postcode_data['result']
        country = result['country']
        region = result['nhs_ha']
        town = result['primary_care_trust']
        district = result['admin_ward']

        address = country + ', ' + region + ', ' + town + ', ' + district
        return print(address)


def get_nearest_postcode():
    postcodes = []
    new_postcode = input("Enter a valid postcode: ")
    postcode_data = api.get_nearest_postcodes_for_postcode(
        postcode=new_postcode)
    for postcode in postcode_data['result']:
        postcodes.append(postcode['postcode'])
    return print(postcodes)

def exit():
    return None

menu()
