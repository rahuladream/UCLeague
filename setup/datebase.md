# Database Setup



sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx


###### 
Database creation to configuration

```
CREATE DATABASE ucleague;
CREATE USER ucleague_usr WITH PASSWORD 'ucleague_pwsd';
ALTER ROLE ucleague_usr SET client_encoding TO 'utf8';
ALTER ROLE ucleague_usr SET default_transaction_isolation TO 'read committed';
ALTER ROLE ucleague_usr SET timezone TO 'Asia/Kolkata';
GRANT ALL PRIVILEGES ON DATABASE ucleague TO ucleague_usr;
```