import requests
from bs4 import BeautifulSoup
import json

def get_url():
    print("Input the URL:")
    return input()

def get_quote(url):
    response = requests.get(url)
    data =  json.loads(response.text)
    if not response.status_code == 200 or data == "" or "content" not in data:
        return "Invalid quote resource!"
    else:
        return data["content"]

def  get_title(soup):

    title =  soup.select("div.originalTitle")[0]
    id = title.text.index("(")
    return title.text[:id-1]



def get_description(soup):
    description = soup.select(".summary_text")[0]
    return description.text.strip()





if __name__ == "__main__":
    url = get_url()

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    try:
        title = get_title(soup)
        description = get_description(soup)
        data = {
            "title": title,
            "description": description
        }
        print(data)
    except Exception as e:
        print("Invalid movie page!")

