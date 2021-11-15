import urllib
import urllib.request


def read_zipcode(msg):
    while True:
        postal = input(msg)
        valid_characters = [
        '1', '2', '3', 
        '4', '5', '6', 
        '7', '8', '9', 
        '0']
        for each in postal:
            if each not in valid_characters:
                postal = postal.replace(each, '')
        if len(postal) != 8:
            return f'Error, {postal} is not a valid postal code'
            break
        try:
            postal = int(postal)
        except:
            return f'Error, {postal} is not a valid postal code'
            break
        else:
            postal = str(postal)
            return postal
            break

def check_zipcode_info(zipcode):
    from bs4 import BeautifulSoup
    import requests

    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    url = f'https://viacep.com.br/ws/{zipcode}/json/'
    site = requests.get(url)
    site = BeautifulSoup(site.content, 'html.parser').text
    site = site.replace('true', 'True')
    site = eval(site)
    if site == {'erro': True}:
        return f'Error, the zip code "{zipcode}" is not valid'
    else:
        return site
