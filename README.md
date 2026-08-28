# EU TED Tenders & Procurement Leads Examples

Public examples for using the
[EU TED Tenders & Procurement Leads](https://apify.com/arclay-tn/eu-ted-procurement-intelligence)
Apify Actor.

This repository contains usage examples only. It does not include the private
Actor implementation.

## What the Actor does

The Actor turns official EU Tenders Electronic Daily notices into normalized,
privacy-safe EU tender and procurement lead data with buyer, country, CPV,
value, dates, source links, quality reports, and optional Parquet exports.

## Other public Arclay data Actors

- [EU Procurement Buyer & Supplier Intelligence](https://apify.com/arclay-tn/eu-procurement-buyer-supplier-intelligence)
  - normalized buyer and supplier intelligence for public-sector sales.
- [EU Funding Calls Intelligence](https://apify.com/arclay-tn/eu-funding-calls-intelligence)
  - official grant and tender opportunity rows for proposal pipelines.
- [EU Product Safety Recall Intelligence](https://apify.com/arclay-tn/eu-product-safety-recall-intelligence)
  - official Safety Gate alerts for recall and marketplace workflows.
- [EU Industrial Facility Intelligence](https://apify.com/arclay-tn/eu-industrial-facility-intelligence)
  - public industrial facility and reporting records from the EEA.

Each listing has its own input schema, output contract, and current pricing.
The examples repository contains usage material only; Actor implementations
remain private.

## Quick start

1. Open the Actor on Apify Store.
2. Choose a date range of up to 31 days.
3. Optionally filter by buyer country, CPV prefix, procurement stage, or minimum value.
4. Run the Actor and export results as JSON, CSV, Excel, or Parquet.

## Examples

- [Run the Actor with Python](examples/python_fetch_dataset.py)
- [Run the Actor with Node.js](examples/node_run_actor.mjs)
- [Analyze dataset rows with pandas](notebooks/procurement_leads_analysis.ipynb)
- [Query Parquet exports with DuckDB](notebooks/duckdb_parquet.ipynb)
- [CRM import mapping](crm/README.md)

## Example input

```json
{
  "dateFrom": "2025-08-01",
  "dateTo": "2025-08-07",
  "country": "FRA",
  "maxResults": 100,
  "includeParquet": true,
  "includeLots": true
}
```

## High-value awards input

```json
{
  "dateFrom": "2025-08-01",
  "dateTo": "2025-08-31",
  "procurementStage": "result",
  "minEstimatedValue": 1000000,
  "maxResults": 100,
  "includeParquet": true
}
```

## Useful filters

| Use case | Country | CPV | Stage | Min value |
| --- | --- | --- | --- | --- |
| France public tenders | `FRA` | leave blank | leave blank | leave blank |
| Germany IT procurement | `DEU` | `72*` | leave blank | leave blank |
| Construction tenders | leave blank | `45*` | leave blank | leave blank |
| Healthcare notices | leave blank | `33*` | leave blank | leave blank |
| Software and IT services | leave blank | `72*` | leave blank | leave blank |
| High-value EU awards | leave blank | leave blank | `result` | `1000000` |
| Poland tenders | `POL` | leave blank | leave blank | leave blank |

## Pricing examples

The Actor is priced from $1.90 per 1,000 results on Apify. For example, 100
results costs about $0.19 before any Apify account usage limits or platform
changes. Always check the live Apify Store listing for current price.

## Output mapping

Typical fields include notice ID, publication date, buyer name, buyer country,
notice title, main CPV, estimated value, currency, procurement stage, amendment
flags, and official source URL.

## License

Examples are provided under the MIT License.
