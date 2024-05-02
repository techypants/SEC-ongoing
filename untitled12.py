import pandas as pd
import csv
import numpy as np
pd.set_option('display.max_rows', None)  # Show all rows

comp_file = pd.read_csv('D:/fin tech/SEC/2022q4/output.csv')

# comp_file.to_csv('D:/fin tech/SEC/2023q4/num.csv', index=False)
comp_file['id'] = comp_file['adsh'].astype(str)+comp_file['tag'].astype(str) + (comp_file['version']).astype(str)


# counts= comp_file['id'].value_counts()
# print(counts.head())


# print(merged_column.head(100))

def remove_leading_zeros(s):
    return str(int(s))

# Remove dashes and leading zeros
# comp_file['id'] = comp_file['adsh'].apply(lambda x: ''.join(map(remove_leading_zeros, x.split('-'))))

comp_file.to_csv('D:/fin tech/SEC/2022q4/num.csv', index=False)
# Print the modified DataFrame
print(comp_file.head())



# Remove dashes and leading zeros
# comp_file['id'] = comp_file['adsh'].str.replace('-', '').str.lstrip('0')

# # Print the modified DataFrame
# print(comp_file.head())



#---------------------------------------------------

