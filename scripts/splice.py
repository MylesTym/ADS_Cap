# Splice a CSV file to only the first x rows
import pandas as pd

def splice_csv(input_path, output_path, num_rows):
	"""
	Reads a CSV from input_path, writes the first num_rows rows to output_path.
	"""
	df = pd.read_csv(input_path)
	df.head(num_rows).to_csv(output_path, index=False)


splice_csv('data/clean_data.csv', 'data/splice_data01.csv', 10000)
