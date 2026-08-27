"""Run EU TED Procurement Intelligence and fetch dataset rows.

Set APIFY_TOKEN before running:

    pip install apify-client pandas
    python examples/python_fetch_dataset.py
"""

from __future__ import annotations

import os

import pandas as pd
from apify_client import ApifyClient


ACTOR_ID = "arclay-tn/eu-ted-procurement-intelligence"


def main() -> None:
    token = os.environ["APIFY_TOKEN"]
    client = ApifyClient(token)

    run_input = {
        "dateFrom": "2025-08-01",
        "dateTo": "2025-08-07",
        "country": "FRA",
        "maxResults": 100,
        "includeParquet": True,
        "includeLots": True,
    }

    run = client.actor(ACTOR_ID).call(run_input=run_input)
    dataset_id = run["defaultDatasetId"]
    rows = list(client.dataset(dataset_id).iterate_items())

    df = pd.DataFrame(rows)
    print(df.head())
    df.to_csv("ted_procurement_leads.csv", index=False)


if __name__ == "__main__":
    main()
