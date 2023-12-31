# -*- coding: utf-8 -*-
"""MTP_PROJECT_batting_data_collection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RAyEJ947NVp-4TsB64vn_YsDwuP2wJv3
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
# import requests
# from bs4 import BeautifulSoup
import csv

import requests
from bs4 import BeautifulSoup
import csv

url = "https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;spanmax1=20+Sep+2023;spanmin1=20+Sep+2013;spanval1=span;template=results;type=batting"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

# Locate the table elements
tables = soup.find_all("table", class_="engineTable")

# Get the desired table (in this case, the third table)
desired_table = tables[2]

# Extract headers
headers = [header.text.strip() for header in desired_table.find_all("th")]

# Initialize a list to store the data
table_data = []

# Iterate through the rows (skip the first row as it contains headers)
for row in desired_table.find_all("tr")[1:]:
    # Extract the data from each cell (td) in the row
    row_data = [cell.text.strip() for cell in row.find_all("td")]
    # Append the row data to the table_data list
    table_data.append(row_data)

# Save the data to a CSV file with headers
csv_file_name = "cricket_data_with_headers.csv"
with open(csv_file_name, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Write the headers as the first row
    writer.writerow(headers)
    # Write the table data
    writer.writerows(table_data)

print(f"Data with headers has been saved to {csv_file_name}")

import requests
from bs4 import BeautifulSoup
import csv

table_data_list = []

# Initialize variables
for i in range(2, 24):
    base_url = f"https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;page={i};spanmax1=20+Sep+2023;spanmin1=20+Sep+2013;spanval1=span;template=results;type=batting"
    print(base_url)
    # Fetch the page content
    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Failed to fetch page {i}")
        break

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Locate and extract the desired table (table 2) on the page
    tables = soup.find_all("table", class_="engineTable")
    if len(tables) < 3:  # Ensure that table 2 exists on the page
        print(f"Table 2 not found on page {i}")
        continue

    desired_table = tables[2]

    # Extract rows and data from the desired table
    table_data = []

    # Iterate through the rows (skip the first row as it contains headers)
    for row in desired_table.find_all("tr")[1:]:
        # Extract the data from each cell (td) in the row
        row_data = [cell.text.strip() for cell in row.find_all("td")]
        # Append the row data to the table_data list
        table_data.append(row_data)

    # Append the table data to the main list
    table_data_list.extend(table_data)

    # Print a message for each successfully scraped page
    print(f"Scraped page {i}")

# Print the total number of scraped pages
print(f"Scraped a total of {len(range(2, 24))} pages.")

# Now, you can write the table data to a CSV file if needed
csv_file_name = "cricket_data.csv"
with open(csv_file_name, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(table_data_list)

print(f"Data has been saved to {csv_file_name}")

import csv

# Define the names of the input CSV files
csv_file1 = "cricket_data_with_headers.csv"
csv_file2 = "cricket_data.csv"

# Define the name of the output combined CSV file
combined_csv_file = "combined_cricket_data.csv"

# Initialize lists to store the data from each CSV file
data_from_csv1 = []
data_from_csv2 = []

# Read data from the first CSV file (cricket_data_with_headers.csv)
with open(csv_file1, mode='r', newline='') as file1:
    reader = csv.reader(file1)
    data_from_csv1 = list(reader)

# Read data from the second CSV file (cricket_data.csv)
with open(csv_file2, mode='r', newline='') as file2:
    reader = csv.reader(file2)
    data_from_csv2 = list(reader)

# Combine the data by concatenating the two lists
combined_data = data_from_csv1 + data_from_csv2

# Write the combined data to the output CSV file
with open(combined_csv_file, mode='w', newline='') as combined_file:
    writer = csv.writer(combined_file)
    writer.writerows(combined_data)

print(f"Combined data has been saved to {combined_csv_file}")

import pandas as pd

df = pd.read_csv(combined_csv_file)
df.head(20)

df.drop(df.columns[-1],axis=1,inplace =True)
df.head()

# Save the updated DataFrame to the same CSV file
df.to_csv(combined_csv_file, index=False)

print(f"Updated data with the last column dropped has been saved to {csv_file}")

# url="https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;spanmax1=20+Sep+2023;spanmin1=20+Sep+2013;spanval1=span;template=results;type=batting"

# r= requests.get(url)
# print(r) #r.text gives unstructed data

# soup = BeautifulSoup(r.text,"lxml")
# print(soup)

# print(soup.div)

# print(soup.div.ul) #to get all the ul tags

# print(soup.div.ul.a)

# print(soup.div.ul.p) #p,a,ul are tags

# #orange colour attributes class,id
# tag =soup.div
# print(tag.attrs)

# table = soup.find_all("table", class_="engineTable")
# print(table[2])