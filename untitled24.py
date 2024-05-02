import pandas as pd
import csv
import numpy as np
pd.set_option('display.max_rows', None)  # Show all rows

comp_file = pd.read_csv('D:/fin tech/SEC/2023q4/tsla.csv')

print((comp_file['coreg'].value_counts().head(20)))