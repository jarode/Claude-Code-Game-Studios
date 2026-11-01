# Next.js / React / Node.js web applications
**Identify:** `package.json`, lockfile, Next App/Pages Router, server actions, auth middleware, runtime/node versions and existing test runners.
**Core checks:** safe auth/session boundaries; user-provided input validation; protected route/API behavior; SSR/hydration and mobile navigation; stable design.
**Safe commands:** `npm ci` (only in test checkout), `npm run lint`, `npm run typecheck`, `npm test`, `npm run build` only if scripts exist. Never assume commands exist; check scripts first.
**Acceptance:** type/build results, data-safe access, keyboard/focus, mobile screenshots and Playwright journeys where configured.
**Release risks:** client-exposed secrets, cached private data, redirect loops, missing loading/error states, SEO regression.
