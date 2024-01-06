# Helpers

Scripts that may help!

## Running Helper Scripts

To install Python packages, run:

```bash
poetry install
```

To download the Breakfast at the Frat dataset, run:

```bash
poetry run pythnon download_breakfast_dataset.py
```

**Note:** If you want to download the Best Buy dataset, change the Python file to `download_best_buy_dataset.py`.

To import/export the Breakfast at the Frat data to/from MySQL database, run:

```bash
poetry run python import_breakfast_dataset_to_mysql.py
```

## Installing MySQL Client on GitHub Codespaces (Ubuntu)

```bash
sudo apt update
sudo apt install mysql-client
```

## Running MySQL and Adminer with Docker

```bash
docker compose up
```

To connect to MySQL container on local machine via CLI, run the following command:

```bash
mysql -h 0.0.0.0 -u root -p
```

If you want to connect to the MySQL instance on the cloud, just change the IP `0.0.0.0` to the instance's public IP.
