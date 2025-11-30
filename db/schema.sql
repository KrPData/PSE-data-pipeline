CREATE SCHEMA IF NOT EXISTS market_data;
SET search_path TO market_data;
--
DROP TABLE IF EXISTS
    staging_mb_podst_cena, staging_mb_podst_wielkosc, staging_mb_uzup_cena,
    staging_mb_uzup_wielkosc, staging_nierynkowe_red, staging_zap_gen,
    mb_podst_cena, mb_podst_wielkosc, mb_uzup_cena, mb_uzup_wielkosc, nierynkowe_red, zap_gen;

-- staging tables

CREATE TABLE IF NOT EXISTS staging_mb_podst_cena (
    datetime TIMESTAMP,
    nazwa_mocy TEXT,
    cena_pln_Mwh NUMERIC
);

CREATE TABLE IF NOT EXISTS staging_mb_podst_wielkosc (
    datetime TIMESTAMP,
    nazwa_mocy TEXT,
    wielkosc_MWh NUMERIC
);

CREATE TABLE IF NOT EXISTS staging_mb_uzup_cena (
    datetime TIMESTAMP,
    nazwa_mocy TEXT,
    cena_pln_Mwh NUMERIC
);

CREATE TABLE IF NOT EXISTS staging_mb_uzup_wielkosc (
    datetime TIMESTAMP,
    nazwa_mocy TEXT,
    wielkosc_MWh NUMERIC
);

CREATE TABLE IF NOT EXISTS staging_nierynkowe_red (
    datetime TIMESTAMP,
    generacja_typ TEXT,
    wielkosc_MWh NUMERIC
);

CREATE TABLE IF NOT EXISTS staging_zap_gen (
    datetime TIMESTAMP,
    generacja_typ TEXT,
    wielkosc_MWh NUMERIC
);

----------------------------------------------------------

CREATE TABLE IF NOT EXISTS mb_podst_cena (
    datetime TIMESTAMP NOT NULL,
    nazwa_mocy TEXT NOT NULL,
    cena_pln_Mwh NUMERIC NOT NULL,
    PRIMARY KEY (datetime, nazwa_mocy)
);

CREATE TABLE IF NOT EXISTS mb_podst_wielkosc (
    datetime TIMESTAMP NOT NULL,
    nazwa_mocy TEXT NOT NULL,
    wielkosc_MWh NUMERIC NOT NULL,
    PRIMARY KEY (datetime, nazwa_mocy)
);

CREATE TABLE IF NOT EXISTS mb_uzup_cena (
    datetime TIMESTAMP NOT NULL,
    nazwa_mocy TEXT NOT NULL,
    cena_pln_Mwh NUMERIC NOT NULL,
    PRIMARY KEY (datetime, nazwa_mocy)
);

CREATE TABLE IF NOT EXISTS mb_uzup_wielkosc (
    datetime TIMESTAMP NOT NULL,
    nazwa_mocy TEXT NOT NULL,
    wielkosc_MWh NUMERIC NOT NULL,
    PRIMARY KEY (datetime, nazwa_mocy)
);

CREATE TABLE IF NOT EXISTS nierynkowe_red (
    datetime TIMESTAMP NOT NULL,
    generacja_typ TEXT,
    wielkosc_MWh NUMERIC,
    PRIMARY KEY (datetime, generacja_typ)
);

CREATE TABLE IF NOT EXISTS zap_gen (
    datetime TIMESTAMP NOT NULL,
    generacja_typ TEXT,
    wielkosc_MWh NUMERIC,
    PRIMARY KEY (datetime, generacja_typ)
);

---------------- initally created staging tables ----------------------

COPY staging_mb_podst_cena
FROM 'C:\Users\krzys\Desktop\szkolenia\ETL projekty\dane rynkowe PSE\cleared data\mb_podst_cena.csv'
DELIMITER ','
CSV HEADER;

COPY staging_mb_podst_wielkosc
FROM 'C:\Users\krzys\Desktop\szkolenia\ETL projekty\dane rynkowe PSE\cleared data\mb_podst_wielkosc.csv'
DELIMITER ','
CSV HEADER;

COPY staging_mb_uzup_cena
FROM 'C:\Users\krzys\Desktop\szkolenia\ETL projekty\dane rynkowe PSE\cleared data\mb_uzup_cena.csv'
DELIMITER ','
CSV HEADER;

COPY staging_mb_uzup_wielkosc
FROM 'C:\Users\krzys\Desktop\szkolenia\ETL projekty\dane rynkowe PSE\cleared data\mb_uzup_wielkosc.csv'
DELIMITER ','
CSV HEADER;

COPY staging_nierynkowe_red
FROM 'C:\Users\krzys\Desktop\szkolenia\ETL projekty\dane rynkowe PSE\cleared data\nierynkowe_red.csv'
DELIMITER ','
CSV HEADER;

COPY staging_zap_gen
FROM 'C:\Users\krzys\Desktop\szkolenia\ETL projekty\dane rynkowe PSE\cleared data\zap_gen_kse_15min.csv'
DELIMITER ','
CSV HEADER;




