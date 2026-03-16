# Reflection

A social self-awareness platform for Princeton students: anonymous feedback and AI-powered insights for personal growth and emotional intelligence.

## Features

- **Princeton CAS authentication** — Only verified Princeton students can sign in
- **Onboarding** — Profile photo, name, class year, residential college, major
- **Browse** — Discover students with search and filters (major, year, college)
- **Profiles** — Public reflection summary, anonymous reviews, star ratings
- **Write reviews** — Anonymous, AI-moderated comments
- **Private growth insights** — AI-generated feedback and resource links (visible only to the profile owner)

## Tech stack

- **Backend:** Node.js, Express, SQLite (better-sqlite3), Princeton CAS, OpenAI for moderation and reflections
- **Frontend:** React 18, TypeScript, Vite, Tailwind CSS, Framer Motion, React Router

## Setup

1. **Clone and install**

   ```bash
   cd reflection
   npm install
   cd client && npm install && cd ..
   ```

2. **Environment**

   Copy `.env.example` to `.env` and set:

   - `SESSION_SECRET` — Random string for session signing
   - `OPENAI_API_KEY` — For AI moderation and reflection/growth summaries (optional; without it, moderation passes and placeholders are used)
   - `BASE_URL` — Frontend URL (e.g. `http://localhost:5173` for dev)
   - `API_URL` — Backend URL (e.g. `http://localhost:3001` for dev)

3. **Database**

   ```bash
   npm run db:init
   ```

4. **Run**

   ```bash
   npm run dev
   ```

   - Frontend: http://localhost:5173  
   - API: http://localhost:3001  

   Log in via **Sign in with Princeton CAS** (requires Princeton NetID).

## Deploy frontend on Vercel

1. Push the repo to GitHub (e.g. `akuei-codes/reflection`).
2. Go to [vercel.com](https://vercel.com) and sign in (e.g. with GitHub).
3. **Add New Project** → **Import** your `reflection` repo.
4. Leave **Root Directory** as `.` (repo root). Vercel will use `vercel.json`: build `client`, output `client/dist`.
5. (Optional) Add **Environment Variable**: `VITE_API_URL` = your backend URL (e.g. `https://your-api.railway.app`) once the API is deployed. Leave blank to get a frontend-only preview.
6. Click **Deploy**. Your app will be at **https://&lt;project-name&gt;.vercel.app** (or your custom domain).

To deploy the **backend** (required for login and data), use [Railway](https://railway.app), [Render](https://render.com), or another Node host. Set `BASE_URL` to your Vercel URL and `API_URL` to the backend URL, then set `VITE_API_URL` on Vercel to that same backend URL.

## Production

- Set `NODE_ENV=production`
- Set `BASE_URL` and `API_URL` to your deployed frontend and API URLs
- Ensure the CAS callback URL is reachable by Princeton’s CAS server (e.g. `https://your-api.com/api/auth/cas/callback`)
- Serve the built client: `npm run build` then serve the `client/dist` folder from your frontend host
- Use a strong `SESSION_SECRET` and secure cookies (HTTPS)

## Design

- **Colors:** Primary indigo (#4F46E5), secondary lavender (#C7D2FE), accent emerald (#10B981), background #FAFAFA, text #111827
- **UI:** Card-based layout, 20–24px rounded corners, soft shadows, Framer Motion for transitions and hover states

## License

Private / educational use.
