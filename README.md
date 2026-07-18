# Virtual Bookshelf

A SvelteKit app for managing bookshelves, book loans, and user accounts with Drizzle ORM and Better Auth.

## Quick start

### Prerequisites

- Node.js 20+ and npm
- Git

### Linux / macOS

```bash
git clone <your-repo-url>
cd "Virtual Bookshelf"
npm install
cp .env.example .env
nano .env
```

Set these values in the .env file:

```env
DATABASE_URL=local.db
ORIGIN=http://localhost:5173
BETTER_AUTH_SECRET=replace-with-a-long-random-string
```

Then run:

```bash
npm run auth:schema
npm run db:push
npm run dev
```

Open http://localhost:5173 in your browser.

(Or start the server and open the app in a new browser tab: `npm run dev -- --open`)

### Windows (PowerShell)

```powershell
git clone <your-repo-url>
cd "Virtual Bookshelf"
npm install
Copy-Item .env.example .env
notepad .env
```

Set the same values in the .env file:

```env
DATABASE_URL=local.db
ORIGIN=http://localhost:5173
BETTER_AUTH_SECRET=replace-with-a-long-random-string
```

Then run:

```powershell
npm run auth:schema
npm run db:push
npm run dev
```

Open http://localhost:5173 in your browser.

(Or start the server and open the app in a new browser tab: `npm run dev -- --open`)

## Development commands

- `npm run dev` — start the local development server
- `npm run check` — run type and Svelte checks
- `npm run lint` — check formatting and lint issues
- `npm run build` — create a production build
- `npm run preview` — preview the production build
- `npm run db:studio` — open Drizzle Studio for the database

## Notes

- The default setup uses a local SQLite database file.
- Keep your `.env` file local and do not commit it.
- If you change the database schema, run `npm run db:push` again.

> **_What's next?_** 🧩 Add-on steps
>
> - drizzle:
>   - Check DATABASE_URL in .env and adjust it to your needs
>   - Run npm run db:push to update your database schema
> - better-auth:
>   - Run npm run auth:schema to generate the auth schema
>   - Run npm run db:push to update your database
>   - Check ORIGIN & BETTER_AUTH_SECRET in .env and adjust it to your needs
>   - Visit /demo/better-auth route to view the demo
>
> Stuck? Visit us at https://svelte.dev/chat
