from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
from fake_useragent import UserAgent
from pathlib import Path
from src.helpers.decorators_ import log, timing_decorator

load_dotenv()


@timing_decorator
@log
def get_soup_pw(url: str) -> bs:
    ua = UserAgent()
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        context = browser.new_context(user_agent=ua.random)
        page = context.new_page()
        page.goto(url)  # Replace with your target URL
        html = page.content()
        soup = bs(html, "html.parser")
        browser.close()
        save_html(html)
        return soup


def save_html(html_: str) -> None:
    filepath = Path("data/html.txt")
    if filepath.exists():
        pass
    else:
        with open(filepath, "w") as f:
            f.write(html_)
            print(f"{filepath} was written")
