import pandas as pd
import csv
import numpy as np
pd.set_option('display.max_rows', None)  # Show all rows

comp_file = pd.read_csv('D:/fin tech/SEC/2023q4/num.csv')

# comp_file.to_csv('D:/fin tech/SEC/2023q4/num.csv', index=False)
# comp_file['id'] = comp_file['adsh'].astype(str)+comp_file['tag'].astype(str) + (comp_file['version']).astype(str)

counts= comp_file['id'].value_counts()
highest_five = (counts)
print(highest_five)

# Step 1: Choose a specific 'id' from the 'highest_five' list




# # Find common values in the 'coreg' column
# common_coreg_values = filtered_df['coreg'].value_counts()

# Print the common coreg values

# filtered_rows = comp_file[comp_file['id'] == 32019323104]
# print(filtered_rows)
# print((filtered_rows['coreg'].unique()))
# print(len(filtered_rows['coreg']))

# see_coreg = comp_file['id']
# print(len(see_coreg))

