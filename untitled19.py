import pandas as pd

comp_file = pd.read_csv('D:/fin tech/SEC/2023q4/sub_with_symbols.csv')

comp_file['stock_name'] = comp_file['instance'].str.extract(r'([a-zA-Z]+-)')
comp_file['stock_name']=comp_file['stock_name'].str.rstrip('-')

# Print the modified DataFrame
comp_file.to_csv('D:/fin tech/SEC/2023q4/sub_with_symbolsid.csv', index=False)

print(comp_file['stock_name'].head(100))    