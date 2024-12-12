import requests
from bs4 import BeautifulSoup

url = "https://py4e-data.dr-chuck.net/comments_42.html"

response = requests.get(url)
response.raise_for_status()  

soup = BeautifulSoup(response.text, 'html.parser')

comments = soup.find_all('span', class_='comments')

total_comments = 0
for comment in comments:
    try:
        total_comments += int(comment.text)
    except ValueError:
        pass

print(f"Общее количество комментариев: {total_comments}")