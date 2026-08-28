"""Run any public Arclay Actor and print a sample of its dataset rows.

Usage:
    python examples/run_catalog_actor.py \
        arclay-tn/eu-funding-calls-intelligence \
        '{"searchQuery":"digital","maxItems":10}'

Set APIFY_TOKEN in the environment before running.
"""

from __future__ import annotations

import argparse
import json
import os

from apify_client import ApifyClient


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("actor_id", help="Apify username/actor-name")
    parser.add_argument("input_json", help="Actor input as a JSON object")
    args = parser.parse_args()

    run_input = json.loads(args.input_json)
    if not isinstance(run_input, dict):
        raise ValueError("input_json must decode to a JSON object")

    client = ApifyClient(os.environ["APIFY_TOKEN"])
    run = client.actor(args.actor_id).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    print(json.dumps(items[:10], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
