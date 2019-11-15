from postcode.postcode import *

postcode_address = get_data_postcode('CW9 6GN')
postcode_valid = postcode_is_valid('CW9 6GN')
postcode_nearest = get_nearest_postcode('CW9 6GN')

print(postcode_valid)