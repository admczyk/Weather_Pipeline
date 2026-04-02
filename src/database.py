import pandas as pd
from sqlalchemy import create_engine
import psycopg2

def create_database():
    engine = create_engine('postgresql+psycopg2://user:password@127.0.0.1:5432/weather_database')
    return engine

def load_data_to_database(df):
    engine = create_database()

    engine.connect()
    #df.to_sql("weather_data", engine, if_exists="replace", index=False)

def main():
    df = pd.read_csv("transformed_weather_past_data.csv", encoding="cp1250")
    # print(df.head())
    # print(df.dtypes)
    load_data_to_database(df)
    #print(create_database())
    pass

if __name__ == "__main__":
    main()