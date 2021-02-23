

import requests
from bs4 import BeautifulSoup
from string import punctuation
import os


def get_url(page = 0):
      if page:
        return f"https://www.nature.com/nature/articles?page={page}"
      else:
          return f"https://www.nature.com/nature/articles"



def get_articles(soup):
    return soup.find_all("article")

def is_type(article , article_type):
    return article.select("span[data-test='article.type']")[0].text == article_type.strip()

def get_link(article):
    return article.select("a[data-track-action='view article']")[0]["href"]

def get_title(article):
    return article.select("a[data-track-action='view article']")[0].text

def transform(title):
    t = str.maketrans('', '', punctuation)
    title = title.strip().translate(t)
    return title.strip().replace(" ", "_")



def get_content(link):
    content =  BeautifulSoup(requests.get(link).content, "html.parser").select(".article__body")
    if content:
        return content[0]
    else:
        content =  BeautifulSoup(requests.get(link).content, "html.parser").select(".article-item__body")
        return content[0]




def save_articles(article_type, page ):
         BASE = "https://www.nature.com"

         response = requests.get(get_url(page))
         soup = BeautifulSoup(response.content, "html.parser")
         articles = get_articles(soup)
         titles = []

         os.mkdir(f"Page_{page}")
         os.chdir(f"Page_{page}")
         for article in articles:
             if is_type(article, article_type):
                    link_article = get_link(article)
                    link = f"{BASE}{link_article}"
                    title = transform(get_title(article))
                    titles.append(title + ".txt")

                    with open(f"{title}.txt", "wb") as f:
                        try:
                            f.write(get_content(link).text.strip().encode("utf-8"))
                        except Exception as e:
                            pass


         os.chdir("..")
         print(titles)
         print("Saved all articles.")


if __name__ == "__main__":
     BASE = "https://www.nature.com"
     url = BASE + "/nature/articles"


     page = int(input())
     article_type = input()
     for i in range(1, page  + 1):
        save_articles(article_type, i)





