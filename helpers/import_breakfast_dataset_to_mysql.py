import configparser

import pandas as pd
import sqlalchemy
from sqlalchemy import text


CONFIG_FILE = "local.conf"
# CONFIG_FILE = "production.conf"

parser = configparser.ConfigParser()
parser.read(CONFIG_FILE)

database = parser.get("mysql_config", "database")
user = parser.get("mysql_config", "username")
password = parser.get("mysql_config", "password")
host = parser.get("mysql_config", "host")
port = parser.get("mysql_config", "port")

uri = f"mysql+pymysql://{user}:{password}@{host}/{database}"
engine = sqlalchemy.create_engine(uri)

# Test SQL command
# df = pd.read_sql("show tables", engine)
# print(df.head(3))

tables = {
    "products": """
        CREATE TABLE IF NOT EXISTS products (
            upc           VARCHAR(300),
            description   VARCHAR(300),
            manufacturer  VARCHAR(100),
            category      VARCHAR(100),
            sub_category  VARCHAR(100),
            product_size  VARCHAR(100)
        )
    """,
    "stores": """
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
    """,
    "transactions": """
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
    """,
}
for k, v in tables.items():
    with engine.connect() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS {k}"))
        conn.execute(text(v))
        print(f"Created {k} table successfully")

    # Import
    df = pd.read_csv(f"breakfast_{k}.csv")
    df.to_sql(k, con=uri, if_exists="replace", index=False)
    print(f"Imported {k} data successfully")

    # Export
    # df = pd.read_sql(f"select * from {k}", engine)
    # df.to_csv(f"breakfast_{k}_export.csv", index=False)
