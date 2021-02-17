#! python3
# verifyLinks.py
# ABSP - Chapter 12

import requests
import bs4

def verify(url):
    """
    Summary:
        Verifies all links within a page, prints broken links.
    Args:
        url (str): url of page to check.
    Returns:
        None
    """
    res = requests.get(url)

    try:
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "html.parser")

        pageLinks = [link.get("href") for link in soup.select("a") if link.get("href")]
        goodLinks = []
        badLinks = []

        for link in pageLinks:

            if link.startswith("http"):
                res2 = requests.get(link)

                try:
                    res2.raise_for_status()
                    print(f"Good: {link}")
                    goodLinks.append(link)

                except Exception as exc:
                    print(f"Broken: {link}")
                    badLinks.append(link)

    except Exception as exc:
        print(f"There was a problem: {exc}")

    print(f'Good links: {len(goodLinks)}. Broken links: {len(badLinks)}.')

if __name__ == "__main__":
    verify("https://automatetheboringstuff.com/2e/chapter12/")