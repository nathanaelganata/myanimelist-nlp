from bs4 import BeautifulSoup

# https://myanimelist.net/anime/genre/10/Fantasy
with open("anime.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")
res = soup.find_all("a", class_="hoverinfo_trigger")

# with open("links.csv", "w") as f:
#     for i in range(0, 50*2, 2):
#         f.write(res[i]['href'] + '/reviews' + "\n")

with open("links.csv", "w") as f:
    for i in range(100, 100*2, 2):
        f.write(res[i]['href'] + '/reviews' + "\n")