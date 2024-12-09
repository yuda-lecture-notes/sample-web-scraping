# import packages
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

# prepare lists to contain the extracted data
teams = []
years = []
wins = []
losses = []

# create webdriver instance
driver = webdriver.Chrome()

# load webpage
driver.get("https://www.scrapethissite.com/pages/forms/?page_num=1")

# add a delay to let the page finish loading
time.sleep(3)

# get page source
html = driver.page_source

# parse page source into BeautifulSoup object
page = BeautifulSoup(html, "html.parser")

# find all data rows in page
rows = page.find_all("tr", {"class": "team"})

# loop through each row
for row in rows:
    # find each data element in single row
    team = row.find("td", {"class": "name"})
    year = row.find("td", {"class": "year"})
    win = row.find("td", {"class": "wins"})
    loss = row.find("td", {"class": "losses"})

    # validate each element, if it exists extract the content inside and append it to the list, otherwise just append None
    # tips: you can encapsulate this code into a function to make the code more efficient
    if team != None:
        # extract content
        # .strip() for removing white-space
        content = team.get_text().strip()

        # append to list
        teams.append(content)
    else:
        teams.append(None)

    if year != None:
        years.append(year.get_text().strip())
    else:
        years.append(None)

    if win != None:
        wins.append(win.get_text().strip())
    else:
        wins.append(None)

    if loss != None:
        losses.append(loss.get_text().strip())
    else:
        losses.append(None)

# create an empty DataFrame
df = pd.DataFrame()

# populate the DataFrame with extracted data
df['Teams'] = teams
df['Year'] = years
df['Wins'] = wins
df['Losses'] = losses

# extract to CSV
df.to_csv('result.csv', index=False)
