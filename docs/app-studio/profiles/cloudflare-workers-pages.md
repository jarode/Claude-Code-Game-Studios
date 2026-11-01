# Cloudflare Workers / Pages / D1 / Web Push
**Identify:** Wrangler version, `wrangler.toml` or `.jsonc`, routes, bindings, environment variables, D1 migrations, Pages build, queue/cron usage.
**Core checks:** request parsing, public/private API separation, CORS, auth context, anti-replay, request limits, retry/duplicate behavior, caching and previews.
**Safe commands:** use package-defined `npm run check` and `npm run build:pages-preview` where present. Local Wrangler requires isolated bindings and test data; never assume remote D1.
**Acceptance:** local Worker HTTP test + auth negative cases + build + preview smoke (with approved preview only), deployment deliberately separate.
**Release risks:** accidental Cloudflare production deploy, D1 remote mutation, shared preview/production secrets, sends from notification dispatcher.
