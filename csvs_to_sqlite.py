import pandas as pd
import sqlite3

# File paths
bills_csv = 'BUF_Bills_2024.csv'
teams_csv = 'teams.csv'
db_file = 'bills_and_teams.db'

# Read CSVs into DataFrames
df_bills = pd.read_csv(bills_csv)
df_teams = pd.read_csv(teams_csv)

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect(db_file)

# Write the DataFrames to SQLite
df_bills.to_sql('bills_stats', conn, if_exists='replace', index=False)
df_teams.to_sql('teams', conn, if_exists='replace', index=False)

print(f"Tables 'bills_stats' and 'teams' have been written to '{db_file}'.")

# Close the connection
conn.close()
