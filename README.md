# EU TED Procurement Intelligence Examples

Public examples for using the
[EU TED Procurement Intelligence](https://apify.com/arclay-tn/eu-ted-procurement-intelligence)
Apify Actor.

This repository contains usage examples only. It does not include the private
Actor implementation.

## What the Actor does

The Actor turns official EU Tenders Electronic Daily notices into normalized,
privacy-safe procurement lead data with buyer, country, CPV, value, dates,
source links, quality reports, and optional Parquet exports.

## Quick start

1. Open the Actor on Apify Store.
2. Choose a date range of up to 31 days.
3. Optionally filter by buyer country or CPV prefix.
4. Run the Actor and export results as JSON, CSV, Excel, or Parquet.

## Examples

- [Run the Actor with Python](examples/python_fetch_dataset.py)
- [Run the Actor with Node.js](examples/node_run_actor.mjs)
- [Analyze dataset rows with pandas](notebooks/procurement_leads_analysis.ipynb)
- [Query Parquet exports with DuckDB](notebooks/duckdb_parquet.ipynb)
- [CRM import mapping](crm/README.md)
- [Launch kit and ready-to-share copy](marketing/launch-kit.md)
- [Customer-dense channel plan](marketing/channel-plan.md)

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

## Useful filters

| Use case | Country | CPV |
| --- | --- | --- |
| France public tenders | `FRA` | leave blank |
| Germany IT procurement | `DEU` | `72*` |
| Construction tenders | leave blank | `45*` |
| Healthcare notices | leave blank | `33*` |
| Poland tenders | `POL` | leave blank |

## Output mapping

Typical fields include notice ID, publication date, buyer name, buyer country,
notice title, main CPV, estimated value, currency, procurement stage, amendment
flags, and official source URL.

## License

Examples are provided under the MIT License.
