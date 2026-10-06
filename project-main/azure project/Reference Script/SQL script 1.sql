CREATE DATABASE SCOPED CREDENTIAL credential_abhi
WITH IDENTITY = 'Managed Identity'

CREATE EXTERNAL data SOURCE Source_silver
WITH
(
    LOCATION = 'https://awstoragedatalake121.blob.core.windows.net/silver',
    CREDENTIAL = credential_abhi
)


CREATE EXTERNAL data SOURCE Source_gold
WITH
(
    LOCATION = 'https://awstoragedatalake121.blob.core.windows.net/gold',
    CREDENTIAL = credential_abhi
)

CREATE EXTERNAL FILE FORMAT format_parquet
WITH
(
    FORMAT_TYPE = PARQUET,
    DATA_COMPRESSION = 'org.apache.hadoop.io.compress.SnappyCodec'
)


-- CREATE EXTERNAL TABE EXTSALES

CREATE EXTERNAL TABLE gold.extsales
WITH
(
    LOCATION = 'extsales',
    DATA_SOURCE = Source_gold,
    FILE_FORMAT = format_parquet
)
AS
SELECT * FROM gold.sales

SELECT * FROM gold.extsales

