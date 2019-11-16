# import the api
import postcodes_io_api
import re

# assign the api to a variable
api = postcodes_io_api.Api(debug_http=False, timeout=None, base_url=None)


def get_a_postcode(postcode):
    '''
    check if the postcode exist, if it does not exist it will
    give as output 'Invalid Postcode' message to the user,
    if it exist will give a simple address extract
    from the postcode
    '''

    if postcode_is_valid(postcode):
        data = get_data_postcode(postcode)
        return data, print(data)
    else:
        return None


def get_data_postcode(postcode):
    ''' Retrive the postcode data by checking first if the syntax is correct
    and then validating the code with postcode api to double check if
    the given postcode eexist and prevent having postcode that does not exist passing true
    '''
    postcode_data = api.get_postcode(postcode)
    return postcode_data


def format_code(postcode):
    '''
    Format the postcode if is not formatted
    or if there is a typo error
    '''
    # Minimum size is 5 letters
    # Maximum size is 8 letters
    if len(postcode) < 5 or len(postcode) > 9:
        return None
    postcode = postcode.upper()
    # Get the outward code
    outward_code = postcode[:-3].strip()
    # Get the inward code
    inward_code = postcode[-3:].strip()

    postcode = outward_code + ' ' + inward_code
    return postcode


def postcode_is_valid(postcode):
    """
        Uses regular expressions to test the pattern of the postcode.
        Followed postcode format as for wikipedia -
        https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
        and following the related question on stackoverflow - 
        https://stackoverflow.com/questions/378157/python-regular-expression-postcode-search
    """
    postcode = format_code(postcode)

    if postcode == None:
        return False

    inward_code = postcode.split(" ")[1]
    outward_code = postcode.split(" ")[0]

    if re.match("^[0-9][ABD-HJLNP-UW-Z]{2}$", inward_code) is None:
        return False
    if re.match("^[A-PR-UWYZ]{1}(([0-9]{1,2}|[0-9][A-HJKS-UW])|\
([A-HK-Y]{1}([0-9]{1,2}|[0-9][A-Z])))$", outward_code) is None:
        return False

    return True


def get_nearest_postcode(postcode):
    '''
    Get nearest postcodes
    '''
    postcodes = []
    postcode_data = api.get_nearest_postcodes_for_postcode(
        postcode=postcode)
    
    for postcode in postcode_data['result']:
        postcodes.append(postcode['postcode'])
    return True, postcodes
