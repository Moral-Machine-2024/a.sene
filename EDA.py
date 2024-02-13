pip install pandas

import pandas as pd

# Define your filtering criteria
criteria1 = 'criteria_value_1'
criteria2 = 'criteria_value_2'
# Define the file path of your dataset
file_path = 'path_to_your_dataset.csv'

# Define chunk size (adjust according to your system's memory)
chunk_size = 1000000

# Initialize an empty list to store filtered chunks
filtered_chunks = []

# Iterate over the dataset in chunks
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    # Apply your filtering criteria
    filtered_chunk = chunk[(chunk['column1'] == criteria1) & (chunk['column2'] == criteria2)]
    # Append the filtered chunk to the list
    filtered_chunks.append(filtered_chunk)

# Concatenate all filtered chunks into a single DataFrame
filtered_data = pd.concat(filtered_chunks)

# Save the filtered dataset to a new file
filtered_data.to_csv('filtered_dataset.csv', index=False)
