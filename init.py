import logging
import ast
import json
from weakref import ref
from bs4 import BeautifulSoup
#import session
import requests
import pandas as pd
import numpy as np
import re
null = None
def main(param ) :
    # req_body = json.loads(param)
    # #req.get_json()
    
    # # Extract the JSON string from the 'param' key (or based on your structure)
    # json_data = req_body.get('param')

    # # Convert JSON data back to a DataFrame
    # df = pd.read_json(json.dumps(json_data), orient='columns')
    df=pd.DataFrame(param["data"])
    logging.info("5555555555")

   
    def scrape_the_price(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
        try:
            page = requests.get(url, headers=headers)
            if page.status_code == 200:
                soup = BeautifulSoup(page.text, 'html.parser')
                convert_tag = soup.find('div', class_='YMlKec fxKbKc')
                convert = convert_tag.get_text(strip=True).replace('$', '')
                return float(convert)
            else:
                return None
        except Exception as e:
            logging.error(f"Error scraping {url}: {e}")
            return None


    def convert_to_gb(value):
        value = str(value)
        if isinstance(value, str):
            value = value.replace(',', '')
            value = value.upper()
            if 'GB' in value:
                try:
                    return float(value.replace('GB', ''))
                except ValueError:
                    return np.nan
            elif 'MB' in value:
                try:
                    return float(value.replace('MB', '')) / 1024 
                except ValueError:
                    return np.nan
            elif 'TB' in value:
                try:
                    return float(value.replace('TB', '')) * 1024 
                except ValueError:
                    return np.nan
            elif 'LESS THAN' in value:
                return np.nan 
            else:
                return np.nan 
        elif isinstance(value, (int, float)):
            return float(value) 
        else:
            return np.nan
    def convert_screen_size(value):
        value = str(value)
        value = value.upper()
        if 'INCHES' in value:
            value = value.replace('INCHES','')
            return float(value)
        elif 'INCH' in value:
            value = value.replace('INCH','')
            return float(value)
        else:
            return None
    def convert_resolution(value):
        value = str(value)
        if value and isinstance(value, str):
            try:
                width, height = value.lower().split('x')
                width = float(width)
                height = float(height)
                return width, height
            except ValueError:
                return None, None
        else:
            return None, None
    def find_color_in_title(title):
        allcolors = [
       "Navy Blue","Light Blue","Titanium Grey", "Titanium Black","Wave Green","Emerald Green","Titanium Silver",
        "Midnight Blue", "Creamy", "Blue Black","Lilac","Carbon Grey", "Bronze", "Copper", "Champagne", "Beige", "Onyx Black", "Midnight Black","Cobalt Violet",
        "Turquoise", "Teal", "Mint Green", "Phantom Black", "Lime Green","Rose Red","Light Violet","Waterfall Blue","Peach"
        "Space Gray", "Awesome Graphite", "Iceblue", "Matte Black", "Phantom Black", "Phantom Silver", "Marble Grey", "Awesome Ice Blue", "Awesome Navy","Navy Black"
        "Mystic Green", "Cosmic Gray", "Phantomx Black", "Awesome Lemon","Silver Shadow", "Light Green", "Mint","Charcoal",
        "Navy","Chartreuse","Awesome Lilac","Awesome Lime","Gradient Purple", "Gradient Blue", "Gradient Red","Gradient Pink", "Marble White", "Graphite","Violet","Personality Yellow"
        "Opal White", "Crystal Blue", "Ice Blue", " Dark Blue","Blue","Black", "White", "Gray", "Silver", "Gold", "Red","Yellow", "Green"
    ]
        for color in allcolors:
            if color.lower() in title.lower():
                return color
        return None
    def find_strg_in_title(title):
        capacity_sizes =["1TB","512GB", "256GB", "128GB", "64GB", "32GB", "16GB", "8GB"]
        if title:
            title_lower = title.lower()
            # Check for keywords related to RAM
            
            if 'capacity' in title_lower  :
                for capacity in capacity_sizes:
                    if re.search(r'\b' + re.escape(capacity.lower()) + r'\b', title_lower, re.IGNORECASE):
                        return capacity
        return None
    def find_ram_in_title(title):
        ram_sizes = ["1GB","2GB", "3GB","4GB","6GB","8GB","12GB","16GB"]
        if title:
            title_lower = title.lower()
            # Check for keywords related to RAM
            if 'ram' in title_lower or 'memory' in title_lower:
                for ram in ram_sizes:
                    if re.search(r'\b' + re.escape(ram.lower()) + r'\b', title_lower, re.IGNORECASE):
                        return ram
        return None
    df_nl=df
    df_nl.columns = [col.lower() for col in df_nl.columns]
    df_nl['CPU'] = df_nl.apply(lambda row: find_cpu_in_title(row['title']) or row['cpu'], axis=1)
    df_nl['color'] = df_nl.apply(lambda row: find_color_in_title(row['title']) or row['color'], axis=1)
    df_nl['Capacity'] = df_nl.apply(lambda row: find_strg_in_title(row['title']) or row['capacity'], axis=1)
    df_nl['RAM'] = df_nl.apply(lambda row: find_ram_in_title(row['title']) or row['ram'], axis=1)
    dfm = list(df_nl['model'].unique())
    df_nl['Model'] = df_nl.apply(lambda row: find_model_in_title(row['title'], dfm) or row['model'], axis=1)
    df_nl['ram'] = df_nl['ram'].fillna(df_nl['RAM'])
    df_nl['capacity'] = df_nl['capacity'].fillna(df_nl['Capacity'])
    df_nl['model']= df_nl['model'].fillna(df_nl['Model'])
    df_nl=df_nl.drop(['Capacity','RAM','Model'], axis=1)
    df_nl['capacity'] = df_nl['capacity'].apply(convert_to_gb)
    df_nl['ram'] = df_nl['ram'].apply(convert_to_gb)
    df_nl['Display size'] = df_nl['Display size'].apply(convert_screen_size)
    df_nl[['width resolution', 'height resolution']] = df_nl['resolution'].apply(convert_resolution).apply(pd.Series)
    df_nl['price'] = df_nl['price'].apply(convert_price_before).apply(lambda x: change_price_to_USD(x, EUR_USD))
    df_nl['rate'] = df_nl['rate'].apply(convert_rate)
    df_nl['currancy'] = df_nl['currancy'].apply(change_to_USD)
     
    df2 =pd.DataFrame(df_nl)  
    df2=df2.to_json(orient='columns')     
    return df2
    #return df_nl.to_dict(orient='list')