import requests

# URL of the web page
url = 'https://adventofcode.com/2023/day/1/input'

# Your session cookie (replace 'your_session_cookie' with the actual session cookie)
cookies = {
    'session': 'xxx'
}

# Send a GET request to fetch the content of the web page with the session cookie
response = requests.get(url, cookies=cookies)

# Check if the request was successful
if response.status_code == 200:
    content = response.text
    # Write the content to a file
    url_split = url.split('/')
    n = int(url_split[-2])
    print(url_split)
    filename = f'aoc_{n}_data1.txt'
    with open(filename, 'w') as file:
        file.write(content)
    print(f'Content saved to {filename}')
else:
    print(f'Failed to retrieve the web page. Status code: {response.status_code}')