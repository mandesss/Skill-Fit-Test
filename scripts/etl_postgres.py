import pandas as pd
from sqlalchemy import create_engine
import os

# Configurations
DB_USER = os.getenv("DB_USER", "postgres")  # Replace with your PostgreSQL username
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin")  # Replace with your PostgreSQL password
DB_HOST = os.getenv("DB_HOST", "localhost")  # Replace with your PostgreSQL host
DB_PORT = os.getenv("DB_PORT", "5432")  # Replace with your PostgreSQL port
DB_NAME = os.getenv("DB_NAME", "transaksi_sembako")  # Replace with your PostgreSQL database name

# File paths
DATA_DIR = "data/cleaned"
PENJUALAN_FILE = os.path.join(DATA_DIR, "penjualan_cleaned.csv")
PEMBELIAN_FILE = os.path.join(DATA_DIR, "pemasukan_cleaned.csv")

# Database connection URI
DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def load_data_to_postgres(file_path, table_name, engine):
    try:
        print(f"Loading {file_path} into {table_name}...")
        # Read the cleaned CSV file
        df = pd.read_csv(file_path)
        
        # Convert 'tanggal' column to datetime
        if 'tanggal' in df.columns:
            df['tanggal'] = pd.to_datetime(df['tanggal'], errors='coerce', format='%Y-%m-%d')
        
        # Upload to PostgreSQL
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data successfully loaded into table {table_name}.")
    except Exception as e:
        print(f"Error while loading {file_path} into {table_name}: {e}")


def main():
    print("Starting ETL process...")

    # Connect to the database
    engine = create_engine(DATABASE_URI)
    
    try:
        # Test connection
        with engine.connect() as connection:
            print("Connected to the database successfully!")

        # Load datasets into PostgreSQL
        load_data_to_postgres(PENJUALAN_FILE, "penjualan", engine)
        load_data_to_postgres(PEMBELIAN_FILE, "pemasukan", engine)

        print("ETL process completed successfully!")
    except Exception as e:
        print(f"Database connection error: {e}")
    finally:
        engine.dispose()

if __name__ == "__main__":
    main()
