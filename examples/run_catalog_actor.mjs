// Run any public Arclay Actor and print a sample of its dataset rows.
// npm install
// APIFY_TOKEN=... node examples/run_catalog_actor.mjs \
//   arclay-tn/eu-funding-calls-intelligence '{"searchQuery":"digital","maxItems":10}'

import { ApifyClient } from "apify-client";

const [actorId, inputJson] = process.argv.slice(2);
if (!actorId || !inputJson) {
  throw new Error("Usage: node examples/run_catalog_actor.mjs ACTOR_ID INPUT_JSON");
}

const input = JSON.parse(inputJson);
if (!input || typeof input !== "object" || Array.isArray(input)) {
  throw new Error("INPUT_JSON must decode to a JSON object");
}

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor(actorId).call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(JSON.stringify(items.slice(0, 10), null, 2));
