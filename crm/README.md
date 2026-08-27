# CRM Import Mapping

Use this mapping when importing Actor output into HubSpot, Salesforce,
Pipedrive, Airtable, or a spreadsheet.

| Actor field | CRM field |
| --- | --- |
| `buyer_name` | Company name |
| `buyer_country` | Country |
| `title` | Deal name or opportunity name |
| `main_cpv` | Product category |
| `publication_date` | Lead source date |
| `deadline` | Close date or next action date |
| `estimated_value` | Deal value |
| `estimated_currency` | Currency |
| `source_url` | Source URL |
| `notice_id` | External ID |

## Import tips

- Use `notice_id` as the deduplication key.
- Assign owner by `buyer_country`, CPV prefix, or estimated value.
- Keep the official `source_url` so sales teams can verify the tender.
- Add a workflow rule for deadline reminders.
