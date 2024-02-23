#! ./venv/bin/python
import csv
import random
from datetime import datetime

import sys

def generate_fake_data(num_files, num_columns, save_location):
    # Generate and save the files
    for file_num in range(1, num_files + 1):
        # Define the file path
        file_path = f'{save_location}/data{file_num}.csv'

        # Generate the header row
        header = ['timestamp']
        for i in range(1, num_columns + 1):
            header.append(f'column{i}')

        # Generate the data rows
        data = []
        for _ in range(10):  # Generate 10 rows of data
            row = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
            for _ in range(num_columns):
                row.append(str(random.randint(1, 100)))
            data.append(row)

        # Write the data to the CSV file
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(data)
        except Exception as e:
            print(f'Error writing to file: {file_path}')
            print(e)


if __name__ == '__main__':
    # Get the number of files to create from command line argument
    num_files = int(sys.argv[1])

    # Get the number of columns to create from command line argument
    num_columns = int(sys.argv[2])

    # Get the location to save the files from command line argument
    save_location = sys.argv[3]

    generate_fake_data(num_files, num_columns, save_location)