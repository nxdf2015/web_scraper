

import requests
from bs4 import BeautifulSoup
from string import punctuation


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

def get_title(article):
    return article.select("a[data-track-action='view article']")[0].text

def transform(title):
    t = str.maketrans('', '', punctuation)
    title = title.strip().translate(t).replace(",", "")

    return title.strip().replace(" ", "_")



def get_content(link):
    return BeautifulSoup(requests.get(link).content, "html.parser").select(".article__body")[0]


if __name__ == "__main__":
     BASE = "https://www.nature.com"
     url = BASE + "/nature/articles"
     response = requests.get(url)
     soup = BeautifulSoup(response.content, "html.parser")
     articles = get_articles(soup)
     titles = []
     for article in articles:
        if is_news(article):
            link_article = get_link(article)

            link = f"{BASE}{link_article}"

            title = transform(get_title(article))
            titles.append(title + ".txt")

            with open(f"{title}.txt", "wb") as f:
                f.write(get_content(link).text.strip().encode("utf-8"))
     print("Saved articles:")
     print(titles)
