import requests
from bs4 import BeautifulSoup
import zipfile
import os
import pandas as pd
import glob
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

# URL of the website containing the table
url = "https://aqs.epa.gov/aqsweb/airdata/download_files.html#Meta"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table")

# Find all the last td elements in the table
last_td_elements = table.select("tr td:last-child")

link_list = []
# Iterate over the last td elements
for td in last_td_elements:
    # Find all the a tags within each last td
    a_tags = td.find_all("a")
    
    # Print the href attribute of each a tag
    for a in a_tags:
        link_list.append(a["href"])

# we only need the first 22 links so...

link_list = link_list[:43]
base_link = "https://aqs.epa.gov/aqsweb/airdata/"

for link in link_list:
    download_link = base_link + link

    # Send a GET request to the file URL
    response = requests.get(download_link)

    # Check the response status code
    if response.status_code == 200:
        # Get the file name from the URL
        file_name = download_link.split("/")[-1]
        # Save the file to disk
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(file_name+" File downloaded successfully.")
    else:
        print("Failed to download the file. Status code:", response.status_code)


# Extract the contents of the zip file
path = "D:\Desktop\Improv\Formal Coding\Jupyter Notebooks\Celebal\Group Project\dataset"
for file in link_list:
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(path)
        #  Before running Replace the path with your own path to the desired directory

    # Delete the zip file
    os.remove(file)

    print("Zip file extracted and deleted successfully.")

csv_files_directory = "D:\Desktop\Improv\Formal Coding\Jupyter Notebooks\Celebal\Group Project\dataset"

# Get a list of all CSV files in the directory
csv_files = glob.glob(csv_files_directory + "/*.csv")

# Initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Iterate over each CSV file and merge the data
for file in csv_files:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)
    
    # Append the DataFrame to the merged_data DataFrame
    merged_data = merged_data.append(df, ignore_index=True)
    os.remove(file)

# Path to the output merged CSV file
output_csv_file = str(csv_files_directory)+"/Dataset.csv"

# Save the merged data as a CSV file
merged_data.to_csv(output_csv_file, index=False)

print("CSV files merged successfully.")
