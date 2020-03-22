import argparse
import pandas as pd


parser = argparse.ArgumentParser(description='Generate a new file from csv of products')
parser.add_argument('filename', help='filename of the csv to filter')

args = parser.parse_args()
csv_filename = args.filename

products_df = pd.read_csv(csv_filename)
filtered_products_df = products_df.dropna(subset=['Categories'])

new_filename = input('Enter the filename for the output: ')
filtered_products_df.to_csv(new_filename, index=False)
