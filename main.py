import requests


# request the pyatl.dev index page and save it to file as html
# html_response = requests.get('https://pyatl.dev/')

# if html_response.status_code == requests.codes.not_found:
#     print('Page not found')

# elif html_response.status_code == requests.codes.ok:
#     with open('pyatl.index.html', 'w') as f:
#         f.write(html_response.text)


# response = requests.get('https://api.github.com/events')
# print(response)
# events = response.json()
# for event in events:
#     print(event)

    
# response = requests.post(
#     'https://httpbin.org/post',
#     data={
#         'name': 'pyatl'
#     }
# )
# print(response.text)


# payload = {'key1': 'value1', 'key2': 'value2'}
# response = requests.get('https://httpbin.org/get', params=payload)
# print(response.text)

# get images (requires pillow)
# from PIL import Image
# from io import BytesIO

# image_url ='https://www.101computing.net/wp/wp-content/uploads/python-logo-1.png'
# response = requests.get(image_url)

# python_logo_image = Image.open(BytesIO(response.content))
# python_logo_image.save('pythonlogo.png', 'PNG')

