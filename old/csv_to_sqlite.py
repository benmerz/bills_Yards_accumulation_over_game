import pandas as pd
import sqlite3

# File paths
csv_file = 'BUF_Bills_2024.csv'
db_file = 'BUF_Bills_2024.db'
table_name = 'bills_stats'

# Read CSV into DataFrame
df = pd.read_csv(csv_file)

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect(db_file)

# Write the DataFrame to SQLite
df.to_sql(table_name, conn, if_exists='replace', index=False)

print(f"CSV data from '{csv_file}' has been written to '{db_file}' in table '{table_name}'.")

# Close the connection
conn.close()
