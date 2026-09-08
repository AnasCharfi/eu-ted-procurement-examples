# Arclay EU Data API Use Cases

Five practical starting points for teams evaluating Arclay's public-data
Actors on Apify. Each workflow is bounded, source-linked, and intended for a
small validation run before recurring monitoring.

## Procurement Lead Generation

**Who:** public-sector sales, bid teams, and tender consultants.

**Start:** run the [TED Procurement Intelligence Actor](https://apify.com/arclay-tn/eu-ted-procurement-intelligence)
with a country such as `FRA` or `DEU`, CPV `72`, and `maxResults: 100`.

**Output:** buyer, country, CPV, notice title, value, stage, dates, official
source URL, and quality metadata for CRM or BI workflows.

## Buyer and Supplier Account Mapping

**Who:** market-entry teams, account researchers, and procurement analysts.

**Start:** use the [Buyer and Supplier Intelligence Actor](https://apify.com/arclay-tn/eu-procurement-buyer-supplier-intelligence)
with one country and a narrow sector or CPV filter.

**Output:** normalized organization and relationship records for account
mapping, territory research, and supplier discovery.

## Grant and Funding Pipeline Discovery

**Who:** grant writers, proposal teams, and innovation consultancies.

**Start:** query the [Funding Calls Intelligence Actor](https://apify.com/arclay-tn/eu-funding-calls-intelligence)
with a focused term such as `digital` and `openOnly: true`.

**Output:** opportunity title, programme, status, dates, topic text, source
link, and retrieval metadata for a proposal pipeline.

## Product Safety Monitoring

**Who:** compliance, marketplace, and product teams.

**Start:** run the [Product Safety Recall Intelligence Actor](https://apify.com/arclay-tn/eu-product-safety-recall-intelligence)
with a narrow keyword such as `battery`.

**Output:** Safety Gate alert fields, product and risk details, dates, source
link, and normalized collection metadata for review workflows.

## Industrial and ESG Market Analysis

**Who:** industrial suppliers, ESG analysts, and market-intelligence teams.

**Start:** use the [Industrial Facility Intelligence Actor](https://apify.com/arclay-tn/eu-industrial-facility-intelligence)
with one country and reporting year.

**Output:** facility identity, location, activity, reporting fields, source
references, and retrieval metadata for territory or ESG analysis.

## Integration path

1. Run one small query and inspect the source links.
2. Export JSON, CSV, or Parquet from Apify.
3. Use the [Python and Node examples](../README.md#examples) for automation.
4. Map the stable fields into a CRM, warehouse, spreadsheet, or DuckDB model.
5. Schedule a recurring task only after checking row quality and unit cost.

Prices and coverage vary by Actor and live source availability. These Actors
provide public-source data, not legal, compliance, eligibility, or complete-
coverage guarantees. Verify material decisions against the linked source
notice or record.
