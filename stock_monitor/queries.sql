--https://www.confluent.io/blog/how-real-time-materialized-views-work-with-ksqldb/
--https://docs.ksqldb.io/en/latest/developer-guide/ksqldb-reference/aggregate-functions/

--Create Stream
CREATE STREAM finnhub_trades_stream (
    symbol STRING,
    price DOUBLE,
    volume INT,
    timestamp STRING
) WITH (
    KAFKA_TOPIC='finnhub-trades',
    VALUE_FORMAT='JSON',
    PARTITIONS=1
);


--1) Promedio ponderado de precio de una unidad por cada uno de los símbolos procesados
CREATE TABLE avg_trades AS
SELECT symbol,
    AVG(price) AS avg
FROM finnhub_trades_stream --Stream
GROUP BY symbol
EMIT CHANGES;

select * from avg_trades;

--2) Transacciones procesadas por símbolo
CREATE TABLE count_trades AS
SELECT symbol,
    COUNT(symbol) AS avg
FROM finnhub_trades_stream --Stream
GROUP BY symbol
EMIT CHANGES;

select * from count_trades;

--3) Máximo precio registrado por símbolo
CREATE TABLE max_trades AS
SELECT symbol,
    MAX(price) AS avg
FROM finnhub_trades_stream --Stream
GROUP BY symbol
EMIT CHANGES;

select * from max_trades;


--4) Mínimo precio registrado por símbolo
CREATE TABLE min_trades AS
SELECT symbol,
    MIN(price) AS avg
FROM finnhub_trades_stream --Stream
GROUP BY symbol
EMIT CHANGES;

select * from min_trades;