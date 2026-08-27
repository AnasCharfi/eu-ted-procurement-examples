// Run EU TED Procurement Intelligence and print dataset rows.
//
// npm install apify-client
// APIFY_TOKEN=... node examples/node_run_actor.mjs

import { ApifyClient } from "apify-client";

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const actorId = "arclay-tn/eu-ted-procurement-intelligence";
const input = {
  dateFrom: "2025-08-01",
  dateTo: "2025-08-07",
  country: "DEU",
  cpv: "72*",
  maxResults: 100,
  includeParquet: true,
  includeLots: true,
};

const run = await client.actor(actorId).call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();

console.table(items.slice(0, 10));
