-- Active: 1728545113569@@127.0.0.1@3306
SELECT invoiceid, invoicedate from invoices;

SELECT * FROM invoices WHERE BillingCountry = 'USA' AND Total > 10;

SELECT * FROM invoices WHERE BillingCity = 'London' OR BillingCity = 'Berlin';

SELECT * FROM invoices ORDER BY Total DESC LIMIT 1;

SELECT * FROM invoices WHERE InvoiceDate > '2013-03-31' and Total > 3;

SELECT * FROM invoices WHERE BillingCountry = 'USA' and BillingState = 'CA' and Total > 10;

SELECT * FROM invoices WHERE BillingCountry = 'Canada' and BillingState = 'ON' and BillingCity = 'Toronto';

SELECT * FROM invoices WHERE "InvoiceDate" < '2023-01-01' and ("Total" >= 50 or "BillingCountry" = 'Brazil');