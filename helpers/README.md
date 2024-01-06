# Helpers

Scripts that may help!

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
