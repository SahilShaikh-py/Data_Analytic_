# 🚀 Vibe Coding Stage 4: Git Version Control & Vercel Deployment

Deploying your code into production gives employers and clients tangible proof of your ability to ship software. This guide covers managing your repository with Git and deploying your web app to **Vercel** with zero downtime.

---

## 📌 1. Git Repository Hygiene & Best Practices

### 1. Initialize & Configure Remote
```bash
# Verify git status
git status

# Stage all files
git add .

# Create meaningful, imperative commit messages
git commit -m "feat: complete initial Vibe Coding analytics web application"

# Ensure branch is named 'main'
git branch -M main

# Set remote origin URL
git remote add origin https://github.com/SahilShaikh-py/Data_Analytic_.git

# Push code to GitHub
git push -u origin main
```

### 2. Safeguarding Environment Variables (`.gitignore`)
Never push sensitive API credentials to public repositories!
- Store secrets inside a local `.env` file:
  ```env
  GEMINI_API_KEY=AIzaSyD-YourSecretApiKeyHere
  PORT=5000
  DATABASE_URL=sqlite:///production_analytics.db
  ```
- Verify `.env` is listed inside your `.gitignore` file.

---

## 📌 2. Step-by-Step Frontend Deployment on Vercel

Vercel provides instant global serverless edge hosting with automated continuous deployment (CD) on every `git push`.

### Deployment Steps:
1. **Sign In:** Go to [https://vercel.com/](https://vercel.com/) and sign in with your GitHub account.
2. **Import Repository:**
   - Click **Add New...** ➡️ **Project**.
   - Select your GitHub repository: `SahilShaikh-py/Data_Analytic_`.
3. **Configure Project Root:**
   - In the **Root Directory** field, click **Edit** and select the folder:
     `06_Vibe_Coding_Sprint/vibe_ai_app`.
4. **Environment Variables:**
   - Expand the **Environment Variables** section.
   - Add your key-value pairs:
     - Key: `GEMINI_API_KEY` | Value: `[Your Key]`
5. **Click Deploy:** Vercel automatically compiles the assets and assigns a live production URL:
   `https://datasense-ai-analytics.vercel.app`

### 3. Verifying the Live Deployment
- Check that the page loads with clean HTTPS security.
- Test interactive clicks on buttons, sample questions, and responsive mobile resizing.
- Verify API network calls in the browser DevTools `Network` tab.
