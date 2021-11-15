# Only works with brazilian postal codes
# API USED: https://viacep.com.br/

from utilities import *

while True:
    while True:
        zipcode = read_zipcode('Zip code [br]: ')
        print('-=-'*10)
        if 'error' not in zipcode.lower():
            break
        else:
            print(zipcode)
    zip_info = check_zipcode_info(zipcode)
    if 'Error' not in zip_info:
        break
    else:
        print(zip_info)

print('-=-'*10)
for k, v in zip_info.items():
    print(f'{k}: {v}')
print('-=-'*10)