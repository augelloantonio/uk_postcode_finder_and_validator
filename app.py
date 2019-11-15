from postcode.postcode import *

from postcode.postcode import *

def menu():
    '''
    Get a choice menu
    '''
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

def exit():
    '''
    Simple exit function to exit te program
    '''
    return None

menu()