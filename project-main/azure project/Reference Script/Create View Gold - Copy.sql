---------------------------------
-- CREATE VIEW CALENDAR
--------------------------------
CREATE VIEW gold.calendar
AS
SELECT
    *
FROM
    OPENROWSET
        (
         BULK 'https://awstoragedatalake121.blob.core.windows.net/silver/AdventureWorks_Calendar/',
         FORMAT = 'PARQUET'
        ) as QUER1

---------------------------------
-- CREATE VIEW customer
--------------------------------
CREATE VIEW gold.customer
AS
SELECT
    *
FROM
    OPENROWSET
        (
         BULK 'https://awstoragedatalake121.blob.core.windows.net/silver/AdventureWorks_Customers/',
         FORMAT = 'PARQUET'
        ) as QUER1

---------------------------------
-- CREATE VIEW pro_cat
--------------------------------
CREATE VIEW gold.pro_cat
AS
SELECT
    *
FROM
    OPENROWSET
        (
         BULK 'https://awstoragedatalake121.blob.core.windows.net/silver/AdventureWorks_Product_Subcategories/',
         FORMAT = 'PARQUET'
        ) as QUER1

---------------------------------
-- CREATE VIEW pro
--------------------------------
CREATE VIEW gold.pro
AS
SELECT
    *
FROM
    OPENROWSET
        (
         BULK 'https://awstoragedatalake121.blob.core.windows.net/silver/AdventureWorks_Products/',
         FORMAT = 'PARQUET'
        ) as QUER1

---------------------------------
-- CREATE VIEW return
--------------------------------
CREATE VIEW gold.return
AS
SELECT
    *
FROM
    OPENROWSET
        (
         BULK 'https://awstoragedatalake121.blob.core.windows.net/silver/AdventureWorks_Returns/',
         FORMAT = 'PARQUET'
        ) as QUER1

---------------------------------
-- CREATE VIEW sales
--------------------------------
CREATE VIEW gold.sales
AS
SELECT
    *
FROM
    OPENROWSET
        (
         BULK 'https://awstoragedatalake121.blob.core.windows.net/silver/AdventureWorks_Sales/',
         FORMAT = 'PARQUET'
        ) as QUER1

---------------------------------
-- CREATE VIEW ter
--------------------------------
CREATE VIEW gold.ter
AS
SELECT
    *
FROM
    OPENROWSET
        (
         BULK 'https://awstoragedatalake121.blob.core.windows.net/silver/AdventureWorks_Territories/',
         FORMAT = 'PARQUET'
        ) as QUER1