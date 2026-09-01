# Arclay EU Public Data Actors: Examples

Public examples for using Arclay's
[EU TED Tenders & Procurement Leads](https://apify.com/arclay-tn/eu-ted-procurement-intelligence)
and related public-data Actors on Apify.

This repository contains usage examples only. It does not include the private
Actor implementation.
See [SECURITY.md](SECURITY.md) for token and issue-reporting guidance.

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

| Workflow | Listing | Introductory price |
| --- | --- | ---: |
| EU tender discovery and lead generation | [TED Procurement Intelligence](https://apify.com/arclay-tn/eu-ted-procurement-intelligence) | $1.90 / 1,000 rows |
| Buyer and supplier account intelligence | [Buyer & Supplier Intelligence](https://apify.com/arclay-tn/eu-procurement-buyer-supplier-intelligence) | $1.90 / 1,000 rows |
| Grants and proposal pipeline discovery | [Funding Calls Intelligence](https://apify.com/arclay-tn/eu-funding-calls-intelligence) | $1.90 / 1,000 rows |
| Recall and marketplace safety workflows | [Product Safety Recall Intelligence](https://apify.com/arclay-tn/eu-product-safety-recall-intelligence) | $1.90 / 1,000 rows |
| Industrial and ESG market analysis | [Industrial Facility Intelligence](https://apify.com/arclay-tn/eu-industrial-facility-intelligence) | $2.50 / 1,000 rows |

Prices are introductory and may change; confirm the live Store listing before
placing a large run.

## Quick start

Install the Python examples' dependencies:

```powershell
python -m pip install -r requirements.txt
```

For the Node.js examples, install the pinned dependency:

```powershell
npm install
```

Set your Apify token in the environment. Never commit the token:

```powershell
$env:APIFY_TOKEN = "your-apify-token"
```

Run a catalog Actor with the generic API example:

```powershell
python examples/run_catalog_actor.py `
  arclay-tn/eu-funding-calls-intelligence `
  '{"text":"digital","maxResults":10}'
```

1. Open the Actor on Apify Store.
2. For TED searches, leave dates blank for the last seven completed UTC days, or provide a date range of up to 31 days.
3. Match filters to the linked Actor schema: buyer country, CPV prefix, procurement stage, minimum value, funding text, safety keyword, or industrial country/year/activity.
4. Run the Actor and export results as JSON, CSV, Excel, or Parquet.

## Examples

- [Run the Actor with Python](examples/python_fetch_dataset.py)
- [Run any public Arclay Actor with Python](examples/run_catalog_actor.py)
- [Run the Actor with Node.js](examples/node_run_actor.mjs)
- [Run any public Arclay Actor with Node.js](examples/run_catalog_actor.mjs)
- [Analyze dataset rows with pandas](notebooks/procurement_leads_analysis.ipynb)
- [Query Parquet exports with DuckDB](notebooks/duckdb_parquet.ipynb)
- [CRM import mapping](crm/README.md)

Ready-made inputs for the additional Actors are in
[`examples/inputs/`](examples/inputs/). Pass any JSON file's contents to the
generic Python or Node runner after checking the linked Actor's current schema.
The Industrial example uses `NO` and reporting year `2001`, a verified
non-empty slice of the current EEA layer; availability varies by country and
year.

| File | Actor | Purpose |
| --- | --- | --- |
| `buyer-supplier-france.json` | Buyer & Supplier Intelligence | French buyer and supplier organizations |
| `funding-digital.json` | Funding Calls Intelligence | Open digital funding opportunities |
| `industrial-norway.json` | Industrial Facility Intelligence | Verified EEA facility-reporting sample |
| `safety-battery.json` | Product Safety Recall Intelligence | Battery-related Safety Gate alerts |

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

For a quick TED smoke test, dates may be omitted. The Actor then uses the last
seven completed UTC days and keeps the request bounded:

```json
{
  "country": "FRA",
  "cpv": "72",
  "maxResults": 100,
  "includeParquet": false
}
```

Funding uses `text`, `recordTypes`, `openOnly`, and `maxResults`; it does not use
TED date, country, or CPV fields. Safety requires a keyword. Industrial filters
use `countryCode`, `reportingYear`, `sectorCode`, and `maxFacilities`.

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
