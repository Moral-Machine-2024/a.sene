
#1 Selecting relevant countries from bigger dataset 
import pandas as pd

# Selecting all african countries and putting it in an object
#I first tried to see which african countries were in the dataset, but that took too much time, instead
    # i chose to just put all possible african countries in my object, also avoiding missing cells. 
african_countries = { "DZA", "AGO", "BEN", "BWA", "BFA", "BDI", "CMR", "CPV", 
                       "CAF", "TCD", "COM", "COD", "DJI", "EGY", "GNQ", "ERI", 
                       "SWZ", "ETH", "GAB", "GMB", "GHA", "GIN", "GNB", "CIV", 
                       "KEN", "LSO", "LBR", "LBY", "MDG", "MWI", "MLI", "MRT", 
                       "MUS", "MYT", "MAR", "MOZ", "NAM", "NER", "NGA", "STP", 
                       "SEN", "SYC", "SLE", "SOM", "ZAF", "SSD", "SDN", "TZA", 
                       "TGO", "TUN", "UGA", "COD", "ZMB", "ZWE" }


african_countries_list = list(african_countries)

# Dataset
file_path = 'SharedResponses.csv'

# chunk size
chunk_size = 100000

# empty list to store filtered chunks
filtered_chunks = []

# Going over the dataset in chunks
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    # filtering criteria
    filtered_chunk = chunk[chunk['UserCountry3'].isin(african_countries_list)]
    # filtered chunk to the list
    filtered_chunks.append(filtered_chunk)

# Put all filtered chunks into a single DataFrame
filtered_data = pd.concat(filtered_chunks)

# Saving the filtered dataset into a new file
filtered_data.to_csv('african_countries_dataset.csv', index=False)

#Checking if my ew dataset is smaller, but big enough 
file_path = 'african_countries_dataset.csv'
african_countries_data = pd.read_csv(file_path)
num_rows = len(african_countries_data)
print("Number of rows in the dataset:", num_rows) #342081 rows

#2 Exploring my dataset

#seeing how the dataset looks like
african_countries_data = pd.read_csv(file_path)
print(african_countries_data)

pd.set_option('display.max_columns', None)
print(african_countries_data)


#I have worries about the representation, since this dataset is significantly smaller 
# Getting unique countries 
unique_countries = african_countries_data['UserCountry3'].unique()

for country in unique_countries:
    print(country)

#3 Representation of countries
# African countries
all_african_countries = ["DZA", "AGO", "BEN", "BWA", "BFA", "BDI", "CMR", "CPV", 
                         "CAF", "TCD", "COM", "COD", "DJI", "EGY", "GNQ", "ERI", 
                         "SWZ", "ETH", "GAB", "GMB", "GHA", "GIN", "GNB", "CIV", 
                         "KEN", "LSO", "LBR", "LBY", "MDG", "MWI", "MLI", "MRT", 
                         "MUS", "MYT", "MAR", "MOZ", "NAM", "NER", "NGA", "STP", 
                         "SEN", "SYC", "SLE", "SOM", "ZAF", "SSD", "SDN", "TZA", 
                         "TGO", "TUN", "UGA", "COD", "ZMB", "ZWE"]

# Unique countries in my dataset
countries_in_dataset = ["EGY", "ZAF", "MAR", "DZA", "NGA", "TUN", "TZA", "SDN", "KEN", "MUS", "AGO", 
                         "DJI", "SEN", "BFA", "GHA", "CPV", "MDG", "LBR", "NAM", "ETH", "ZMB", "LBY", 
                         "GAB", "MOZ", "MWI", "MYT", "CMR", "TGO", "ZWE", "BWA", "CIV", "COD", "SOM", 
                         "UGA", "GIN", "SYC", "MRT", "BDI", "SLE", "SSD", "BEN", "LSO", "GNB", "STP", 
                         "MLI", "NER", "CAF", "GMB", "SWZ", "COM", "GNQ", "TCD"]

# convert lists to sets for efficient comparison
all_african_countries_set = set(all_african_countries)
countries_in_dataset_set = set(countries_in_dataset)

# finding countries not represented in the dataset
countries_not_in_dataset = all_african_countries_set - countries_in_dataset_set

# print countries not represented in the dataset #the only country not represented is ERI (eritrea)
print("Countries not represented in the dataset:")
for country in countries_not_in_dataset:
    print(country)

#seeing the most frequent country and least frequent country 
country_counts = african_countries_data['UserCountry3'].value_counts()

# most frequent country and its count
most_frequent_country = country_counts.idxmax()
most_frequent_count = country_counts.max()

# the least frequent country and its count
least_frequent_country = country_counts.idxmin()
least_frequent_count = country_counts.min()

print("Most frequent country:", most_frequent_country, "with count:", most_frequent_count) #ZAF with 134069
print("Least frequent country:", least_frequent_country, "with count:", least_frequent_count) #CAF with 22



    




