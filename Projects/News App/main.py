import requests
query =input("Whtat do you want to search for? ")
api ="9aeb9c127dad400dac50bc1631fe213d"
url=f"https://newsapi.org/v2/everything?q=tesla&from=2025-04-22&sortBy=publishedAt&apiKey={api}"

print(url)
c= requests.get(url)
data = c.json()
articles = data.get('articles', [])
for index, article in enumerate(articles):
    print(index, article['title'])
    print(article['url'])
    print("\n #########################\n")