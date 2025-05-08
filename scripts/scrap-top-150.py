from bs4 import BeautifulSoup
import requests

response = requests.get("https://myanimelist.net/anime/genre/10/Fantasy", headers={
    "Cookie": "search_view=list;"
})
soup = BeautifulSoup(response.text, "html.parser")
res = soup.find_all("a", {"class":"hoverinfo_trigger"})
assert len(res) == 200

with open("links.csv", "w", encoding="utf-8") as f:
    for i in range(0, 50*2, 2):
        f.write(res[i]['href'] + '/reviews' + "\n")

with open("links.csv", "a", encoding="utf-8") as f:
    for i in range(100, 100*2, 2):
        f.write(res[i]['href'] + '/reviews' + "\n")

response = requests.get("https://myanimelist.net/anime/genre/10/Fantasy?page=2", headers={
    "Cookie": "search_view=list;"
})
soup = BeautifulSoup(response.text, "html.parser")
res = soup.find_all("a", {"class":"hoverinfo_trigger"})
assert len(res) == 200

with open("links.csv", "a", encoding="utf-8") as f:
    for i in range(0, 50*2, 2):
        f.write(res[i]['href'] + '/reviews' + "\n")