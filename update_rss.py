import requests
from bs4 import BeautifulSoup
from datetime import datetime
import xml.etree.ElementTree as ET

# URL for Kelowna hourly forecast
URL = "https://weather.gc.ca/forecast/hourly/bc-48_metric_e.html"

# Fetch the page
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract forecast data
forecast_items = soup.select('table.table.table-hover tr')
items = []

for row in forecast_items[1:]:  # Skip header
    cols = row.find_all('td')
    if len(cols) >= 4:
        time = cols[0].get_text(strip=True)
        temp = cols[1].get_text(strip=True)
        condition = cols[3].get_text(strip=True)
        items.append({
            'time': time,
            'temp': temp,
            'condition': condition
        })

# Create RSS XML
rss = ET.Element('rss', version='2.0')
channel = ET.SubElement(rss, 'channel')
ET.SubElement(channel, 'title').text = "Kelowna, BC - Hourly Weather Forecast"
ET.SubElement(channel, 'link').text = URL
ET.SubElement(channel, 'description').text = "Hourly weather updates for Kelowna, British Columbia from Environment Canada"
ET.SubElement(channel, 'language').text = "en-ca"
ET.SubElement(channel, 'lastBuildDate').text = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')

for item in items[:6]:  # Limit to next 6 hours
    entry = ET.SubElement(channel, 'item')
    ET.SubElement(entry, 'title').text = f"{item['time']}: {item['temp']} - {item['condition']}"
    ET.SubElement(entry, 'description').text = f"Temperature: {item['temp']}, Condition: {item['condition']}"
    ET.SubElement(entry, 'pubDate').text = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')
    ET.SubElement(entry, 'link').text = URL

# Write to XML file
tree = ET.ElementTree(rss)
tree.write("kelowna-weather.xml", encoding="utf-8", xml_declaration=True)
