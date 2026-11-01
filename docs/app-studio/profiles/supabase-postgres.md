# Supabase / PostgreSQL / Auth / Realtime
**Identify:** migrations, RLS, SQL functions, Auth hooks, Edge Functions, service-role boundaries, Realtime subscriptions and data retention.
**Core checks:** access matrix for anon/owner/other user/moderator/service role, migration ordering, foreign keys, unique constraints, security invoker/definer rationale and transaction atomicity.
**Safe commands:** run migrations against local or isolated test database only, with fixture rollback. Don't require production credentials or print secrets.
**Acceptance:** positive and negative RLS tests, concurrency/idempotency, safe migration plan, old-client compatibility and rollback/forward-fix notes.
**Release risks:** turning RLS off, exposing private views, unsafe SECURITY DEFINER, trigger bypasses, destructive migration or leaking sensitive records.
