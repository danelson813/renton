# renton/src/main.py
import pandas as pd
from dotenv import load_dotenv
import os

from src.helpers import get_soup_pw
from src.helpers.to_parquet import save_pq, read_parquet


load_dotenv()

url = os.getenv("URL")
soup = get_soup_pw(url)
books = soup.find_all("div", role="listitem")
results = []
for index, book in enumerate(books):
    try:
        title = book.select_one("h2").text
    except AttributeError:
        title = "unknown "
    try:
        link = book.select_one("a")["href"]
    except AttributeError:
        title = "unknown "

    result = {"index": index, "title": title, "link": "https://www.amazon.com" + link}
    results.append(result)
df = pd.DataFrame(results)
df.to_csv("data/results.csv", index=0)
save_pq(df, "data/data.parquet")
df3 = read_parquet("data/data.parquet")
print("df3")
print(df3.head())
