CREATE USER log_user WITH PASSWORD 'password' CREATEDB;
CREATE DATABASE file_serverLog
    WITH
    OWNER = log_user
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
