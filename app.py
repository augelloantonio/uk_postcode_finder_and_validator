'''
Simple app that use uk_postcode_finder_and_validator library
'''

from postcode.postcode import *

def menu():
    '''
    Get a choice menu
    '''
    choice = input("""
                    Postcode finder
                      1: Find Postcode Data
                      2: Find nearest postcodes
                      3: Validate a Postcode
                      4: Format postcode
                      5: Exit

                      Please enter your choice: """)
    if choice == '1':
        get_the_postcode_data()
    if choice == '2':
        get_near_postcodes()
    if choice == '3':
        validate_postcode()
    if choice == '4':
        format_a_postcode()
    if choice == '5':
        exit()
    

def validate_postcode():
    '''
    Validate a postcode
    '''
    postcode = input("Enter a valid postcode: ")

    if postcode_is_valid(postcode) == True:
        print ('The postcode is valid')
    else:
        print ('The postcode is not valid')


def format_a_postcode():
    '''
    Format a Postcode
    ''''
    postcode = input("Enter a valid postcode: ")
    formatted_postcode = (format_code(postcode))
    print (formatted_postcode)
    if formatted_postcode == None:
        return print ('The postcode has syntax error')


def get_the_postcode_data():
    '''
    Get a postcode data
    '''
    postcode = input("Enter a valid postcode: ")
    get_a_postcode(postcode)
    if get_a_postcode(postcode) == None:
        print('Invalid Postcode')

def get_near_postcodes():
    '''
    Get Nearest postcodes
    '''
    postcode = input("Enter a valid postcode: ")
    if postcode_is_valid(postcode) == True:
        postcodes = get_nearest_postcode(postcode)
        print(postcodes)
    else: 
        print('The postcode is invalid')


def exit():
    '''
    Simple exit function to exit te program
    '''
    return None

# run the program locally
menu()