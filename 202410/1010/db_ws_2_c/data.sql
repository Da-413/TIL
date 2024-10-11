-- Active: 1728543455492@@127.0.0.1@3306
SELECT "BillingCountry", sum("Total") FROM invoices GROUP BY "BillingCountry";

SELECT strftime('%Y', "InvoiceDate"), sum("Total") FROM invoices GROUP BY strftime('%Y', "InvoiceDate");

SELECT "BillingState", sum("Total") FROM invoices WHERE "BillingCountry" = 'USA' and "InvoiceDate" > '2010-01-01' GROUP BY "BillingState"

SELECT "BillingCountry", max("Total") FROM invoices WHERE "BillingCountry" = 'Germany' OR "BillingCountry" = 'France' GROUP BY "BillingCountry";