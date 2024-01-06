import configparser

import pandas as pd
import sqlalchemy
from sqlalchemy import text


# CONFIG_FILE = "local.conf"
CONFIG_FILE = "production.conf"

parser = configparser.ConfigParser()
parser.read(CONFIG_FILE)

database = parser.get("mysql_config", "database")
user = parser.get("mysql_config", "username")
password = parser.get("mysql_config", "password")
host = parser.get("mysql_config", "host")
port = parser.get("mysql_config", "port")

uri = f"mysql+pymysql://{user}:{password}@{host}/{database}"
engine = sqlalchemy.create_engine(uri)

with engine.connect() as connection:
    connection.execute(text("DROP TABLE IF EXISTS products"))
    connection.execute(
        text(
            """
            CREATE TABLE IF NOT EXISTS products (
                upc           VARCHAR(300),
                description   VARCHAR(300),
                manufacturer  VARCHAR(100),
                category      VARCHAR(100),
                sub_category  VARCHAR(100),
                product_size  VARCHAR(100)
            )
            """
        )
    )

    connection.execute(text("DROP TABLE IF EXISTS stores"))
    connection.execute(
        text(
            """
            CREATE TABLE IF NOT EXISTS stores (
                store_id                 VARCHAR(100),
                store_name               VARCHAR(100),
                address_city_name        VARCHAR(300),
                address_state_prov_code  VARCHAR(2),
                msa_code                 VARCHAR(100),
                seg_value_name           VARCHAR(100),
                parking_space_qty        VARCHAR(100),
                sales_area_size_num      VARCHAR(100),
                avg_weekly_baskets       VARCHAR(100)
            )
            """
        )
    )

    connection.execute(text("DROP TABLE IF EXISTS transactions"))
    connection.execute(
        text(
            """
            CREATE TABLE IF NOT EXISTS transactions (
                week_end_date VARCHAR(40),
                store_num     VARCHAR(100),
                upc           VARCHAR(100),
                units         VARCHAR(100),
                visits        VARCHAR(100),
                hhs           VARCHAR(100),
                spend         VARCHAR(100),
                price         VARCHAR(100),
                base_price    VARCHAR(100),
                feature       VARCHAR(100),
                display       VARCHAR(100),
                tpr_only      VARCHAR(100)
            )
            """
        )
    )

df = pd.read_sql("show tables", engine)
print(df.head(3))

df = pd.read_csv("breakfast_products.csv")
# print(df.head(3))
df.to_sql("products", con=uri, if_exists="replace", index=False)
df = pd.read_sql("select * from products", engine)
print(df.head(3))
df.to_csv("breakfast_products_export.csv", index=False)

df = pd.read_csv("breakfast_stores.csv")
# print(df.head(3))
df.to_sql("stores", con=uri, if_exists="replace", index=False)
df = pd.read_sql("select * from stores", engine)
print(df.head(3))
df.to_csv("breakfast_stores_export.csv", index=False)

df = pd.read_csv("breakfast_transactions.csv")
# print(df.head(3))
df.to_sql("transactions", con=uri, if_exists="replace", index=False)
df = pd.read_sql("select * from transactions", engine)
print(df.head(3))
df.to_csv("breakfast_transactions_export.csv", index=False)
