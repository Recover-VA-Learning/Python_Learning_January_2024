## Homework Exercise

You have been given a dataset named `reading_medium.csv` which contains information about reading medium usage. Your task is to perform the following tasks using Pandas:

1. Load the dataset into a Pandas DataFrame.
2. Display the first 5 rows of the DataFrame.
3. Calculate the average usage time for medium.
4. Give some other insights about the dataset, std, min, max, etc.
5. Filter the dataset to only include the rows where the `book` reading is above 150.
More difficult:
6. Create a new column named "not_tracked" which is calculated as (total_time - (aggregated time of other tracked activities)).
7. Find the medium with the highest use-time percentage.
8. Save the updated DataFrame to a new CSV file named `reading_medium_updated.csv`.