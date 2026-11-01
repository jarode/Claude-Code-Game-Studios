# Bitrix24 / n8n / external business integrations
**Identify:** owner system, Bitrix REST scopes, OAuth/token refresh, n8n workflow JSON, webhook delivery contract, rate limits and mapping of IDs/fields.
**Core checks:** trigger dedupe, idempotent writes, retries/backoff, failed jobs, partial updates, pagination and sensitive fields.
**Safe commands:** test against fixtures, read-only API requests or a sanctioned sandbox; never fire customer emails, invoice changes or real HR updates as a test.
**Acceptance:** schema contract validation, fixture-based tests of duplicate/missing/failure events, reconciliation and manual owner signoff for production actions.
**Release risks:** accidentally logging PII, incorrect account mapping, replaying a webhook, credentials in exported workflow JSON and repeated billing/notifications.
