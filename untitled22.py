import pandas as pd
import csv
import numpy as np
pd.set_option('display.max_rows', None)  # Show all rows

comp_file = pd.read_csv('D:/fin tech/SEC/2023q2/num.csv')

# Assuming 'adsh' and 'version' are columns in your DataFrame

# Create a DataFrame containing rows where 'adsh' is '1628280' and 'version' is '34847'
filtered_df = comp_file[(comp_file['adsh'] == 1193125) & (comp_file['version'] == 94075
)][['coreg','value','footnote']]
filtered_df['q4']='q2'
# Print the filtered DataFrame
print(filtered_df)
filtered_df.to_csv('D:/fin tech/SEC/2023q4/tsla.csv',mode='a',header=False, index=False)