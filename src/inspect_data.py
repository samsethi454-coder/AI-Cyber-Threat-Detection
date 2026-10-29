
from pathlib import Path
import pandas as pd

# Find the project folder and dataset
project_dir = Path(__file__).resolve().parent.parent
dataset_path = project_dir / "data" / "network_traffic_sample.csv"

# Load the CSV into a DataFrame
df = pd.read_csv(dataset_path)

print("=== FIRST FIVE ROWS ===")
print(df.head())

print("\n=== DATASET SHAPE ===")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n=== COLUMN INFORMATION ===")
df.info()

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== LABEL COUNTS ===")
print(df["label"].value_counts())

print("\n=== NUMERIC SUMMARY ===")
print(df.describe())
