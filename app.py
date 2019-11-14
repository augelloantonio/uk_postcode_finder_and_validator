import postcodes_io_api

api = postcodes_io_api.Api(debug_http=False, timeout=None, base_url=None)


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
    return postcodes


ask_for_postcode()
