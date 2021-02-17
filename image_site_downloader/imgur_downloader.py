#! python3
# imgur-downloader.py
# ABSP Ch. 12 Project

import requests
import os
import bs4


def downloader(query, max_save):
    """
    Args:
        query (str): search query
        max_save (int): max number of images to save to results
    Returns:
        None
    """
    # results folder name
    folder_name = "imgur_" + query

    # image url search
    searchUrl = "https://imgur.com/search"
    queryUrl = searchUrl + "?q=" + query

    # set folder_name path
    abs_folder_path = os.path.abspath(folder_name)
    os.makedirs(abs_folder_path, exist_ok=True)

    # Make request to imgur with query
    res = requests.get(queryUrl)

    try:  
        res.raise_for_status()

        # Parse res.text with bs4 to images
        soup = bs4.BeautifulSoup(res.text, "html.parser")

        # Find URL of image and make sure list not empty
        imgElem = soup.select(".image-list-link img")
        if imgElem == []:
            print("Could not find any images.")
        else:
            # Extract urls
            save_num = min(max_save, len(imgElem))
            download_links = ["https:" + img.get("src") for img in imgElem[:save_num]]

            # Download images
            for link in download_links:
                print(f"Downloading image {link} ...")

                # Request image link from imgur
                res2 = requests.get(link)

                try:
                    res2.raise_for_status()

                    # Save image to folder
                    imgFile = open(os.path.join(abs_folder_path, os.path.basename(link)), "wb")
                    for chunk in res2.iter_content(1000000):
                        imgFile.write(chunk)
                    imgFile.close()
                
                except Exception as exc:
                    print(f'There was a problem: {exc}')

        print(f"{save_num} images downloaded to {abs_folder_path}.")

    except Exception as exc:
        print(f'There was a problem: {exc}')

if __name__ == "__main__":
    query = input("Enter a search query: ")
    max_save = int(input("Enter a max number of results: "))

    downloader(query, max_save)
