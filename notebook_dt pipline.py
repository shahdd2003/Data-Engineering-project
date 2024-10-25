from pyspark.sql import SparkSession
import json
import pandas as pd

# Initialize Spark session
spark = SparkSession.builder.appName("Read JSON from ADLS").getOrCreate()

# File path in Azure Data Lake (ADLS)
file_path = "abfss://###@######.dfs.core.windows.net/PData.json"


# Step 1: Read JSON file from Azure Data Lake Store (ADLS)
df = spark.read.option("multiline", "true").json(file_path)

# Step 2: Convert DataFrame to JSON string
json_data = df.toJSON().collect()[0]  # Collecting as a list and getting the first item

# Step 3: Parse JSON data using Python's json module
data = json.loads(json_data)

# Step 4: Extract the 'output' list
output_list = data.get('output', [])

df=pd.DataFrame(output_list)




# Assuming output_data[0] is a string representation of a dictionary:
data_dict = json.loads(output_list[0]) 

# Now, data_dict is a dictionary and can be used to create the DataFrame:
df = pd.DataFrame(data_dict) 

df.to_csv('abfss://####@#####.dfs.core.windows.net/PData.csv', index=False)