# Perplexity Explorer 2.0

A lightweight web app that lets you calculate token probabilities and perplexity for any sentence using HuggingFace Transformers in the browser. It also stores a history of calculations locally so you can build larger datasets.

## Project structure
```
├─ index.html      # Main UI and JavaScript logic
├─ style.css       # Styling for a clean, responsive layout
├─ serve.py        # Simple Python HTTP server (CORS enabled) for local testing
├─ README.md       # This file (instructions)
└─ .gitignore      # Ignored files
```

## Quick local test
```bash
# 1️⃣ Ensure you have Python 3 installed
python3 --version

# 2️⃣ Start the local server
python3 serve.py
```
Open a browser and navigate to `http://localhost:8000`. The app will load and you can start exploring.

## Adding the project to GitHub
1. **Create a new GitHub repository** (via the web UI or `gh` CLI).
2. In this folder, initialise a git repository and push:
```bash
# Initialise git (if not already)
git init
# Add all files
git add .
# Commit
git commit -m "Initial commit – Perplexity Explorer 2.0"
# Add remote (replace <USERNAME>/<REPO> with your repo URL)
git remote add origin https://github.com/<USERNAME>/<REPO>.git
# Push to GitHub
git branch -M main
git push -u origin main
```
> **Tip:** If you have the `gh` CLI installed you can also run `gh repo create <REPO> --public --source=. --remote=origin --push` to create and push in one step.

## Deploying to Vercel
There are two straightforward ways:

### 1️⃣ Deploy directly from GitHub (recommended)
1. Go to the **Vercel dashboard** → **New Project**.
2. Connect your GitHub account and select the repository you just pushed.
3. Vercel automatically detects a static site and sets the build output directory to the project root.
4. Click **Deploy** – Vercel will build and host the site at `https://<project>.vercel.app`.

### 2️⃣ Deploy via the Vercel CLI
```bash
# Install the Vercel CLI globally (requires Node.js)
npm i -g vercel

# Login to your Vercel account
vercel login

# From the project directory, run:
vercel
```
Follow the prompts (project name, scope, link to existing project or create a new one). Vercel will upload the files and give you a live URL.

## Notes & recommendations
- The app loads the model from the HuggingFace CDN, so an internet connection is required the first time a model is used.
- History is stored in the browser’s `localStorage`; it persists per‑domain (e.g., Vercel deployment) but is not shared across domains.
- If you want to add a **dark‑mode toggle**, update `style.css` with a `.dark` class and toggle it via JavaScript.
- For larger datasets you may later add a backend API to store results server‑side.

---
*Feel free to open an issue or PR if you’d like to improve the UI or add new features!*