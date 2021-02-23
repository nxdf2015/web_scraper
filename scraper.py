import requests
from bs4 import BeautifulSoup
import json

def get_url():
    print("Input the URL:")
    return input()

# def get_quote(url):
#     response = requests.get(url)
#     data =  json.loads(response.text)
#     if not response.status_code == 200 or data == "" or "content" not in data:
#         return "Invalid quote resource!"
#     else:
#         return data["content"]
#
# def get_content(url):
#     """
#     request GET url
#     save content if status code is  200
#     """
#     response = requests.get(url)
#     if response.status_code == 200:
#         with open("source.html", "wb") as f:
#             f.write(response.content)
#             print("Content saved")
#     else:
#         print(f"The URL returned {response.status_code}!")
#
# def  get_title(soup):
#
#     title =  soup.select("div.originalTitle")[0]
#     id = title.text.index("(")
#     return title.text[:id-1]
#
#
#
# def get_description(soup):
#     description = soup.select(".summary_text")[0]
#     return description.text.strip()


def get_articles(soup):
    return soup.find_all("article")

def is_news(article):
    return article.select("span[data-test='article.type']")[0].text == "News"

def get_link(article):
    return article.select("a[data-track-action='view article']")[0]["href"]

if __name__ == "__main__":
     url = "https://www.nature.com/nature/articles"



     response = requests.get(url)
     soup = BeautifulSoup(response.content, "html.parser")
     articles = get_articles(soup)

     for article in articles:
        if is_news(article):
            link = get_link(article)
    # try:
    #     title = get_title(soup)
    #     description = get_description(soup)
    #     data = {
    #         "title": title,
    #         "description": description
    #     }
    #     print(data)
    # except Exception as e:
    #     print("Invalid movie page!")


