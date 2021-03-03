#! python3
# downloader.py
# ABSP - Chapter 17

import requests
import bs4
import shelve
import os


def downloader(url):
    """
    Summary:
        [description]
    Args:
        url ([type]): [description]
    """
    # Make request to website
    res = requests.get(url)
    res.raise_for_status()

    # find date with 'headers'
    currDate = res.headers["Last-Modified"]
    print(currDate)

    # shelf file to store previous date
    shelfFile = shelve.open("prevDate")

    if not shelfFile.keys():
        print("<---Very First Request--->")
        shelfFile["prev"] = currDate

    else:
        print("Starting daily check...")
        prevDate = shelfFile["prev"]

        # If website has not been updated, return
        if prevDate == currDate:
            print("No updates available.")
            return

    # If website was updated, get img url, create folder for file, make request, save
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    imgUrl = soup.select("#comic img")[0].get("src")
    os.makedirs("comics", exist_ok=True)

    try:
        print("Making comic img request...")
        res2 = requests.get('https:' + imgUrl)
        res2.raise_for_status()
        
        print('Saving image...')
        with open(os.path.join('comics', os.path.basename(imgUrl)), 'wb') as imgFile:
            for chunk in res2.iter_content(100000):
                imgFile.write(chunk)
    except Exception as exc:
        print(exc)

    # Update and close shelve file
    print('Updating shelfFile...')
    shelfFile['prev'] = currDate
    shelfFile.close()
    print('Done.')

    
if __name__ == '__main__':
    downloader('https://xkcd.com')