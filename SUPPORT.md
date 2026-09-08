# Support And Troubleshooting

Use the matching Apify Actor page for the current input schema, pricing, and
run controls. The [Arclay data catalog](https://arclay.tn/automation-data)
contains buyer-focused guides and links to every public Actor.

## First run checklist

1. Start with a small `maxResults` or equivalent limit.
2. Use the field names shown in the current Actor input form.
3. Keep country codes uppercase and CPV values numeric where the form requests
   them.
4. Inspect the run log and dataset output before scheduling recurring runs.
5. Verify important decisions against each row's official source link.

## No rows returned

An empty dataset can be a valid result when the selected source, date range,
country, keyword, or sector has no matching records. Broaden one filter at a
time, use a recent bounded period where supported, and retry with a small limit.
Do not assume an empty result means the source is unavailable.

## Run failure

Check the Actor's current input schema and log first. Avoid copying old saved
inputs after a schema change. For a reproducible report, keep the Actor URL,
input JSON without tokens, run ID, timestamp, and the first error message.
Never post tokens, credentials, or customer data in an issue or message.

## Output and integration

The public examples cover Python, Node.js, pandas, DuckDB, CRM mapping, and
JSON/CSV/Parquet exports. Start with one successful run, confirm field quality,
then create a recurring task in Apify.

## Scope

Arclay Actors provide normalized public-source records and source links. They
do not guarantee eligibility, legal or compliance advice, complete coverage,
or a particular number of matching rows. Pricing and source availability can
change; confirm the live Apify listing before a large run.
