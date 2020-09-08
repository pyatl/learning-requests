import requests


html_response = requests.get('https://pyatl.dev/')

if html_response.status_code == requests.codes.not_found:
    print('Page not found')

elif html_response.status_code == requests.codes.ok:
    with open('pyatl.index.html', 'w') as f:
        f.write(teml_response.text)
    

