# 🚀 Railway Deployment Guide

## Quick Deploy to Railway

### Method 1: GitHub Integration (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for Railway deployment"
   git push origin main
   ```

2. **Deploy on Railway**
   - Visit [railway.app](https://railway.app)
   - Click "Start a New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will auto-detect Flask and deploy!

### Method 2: Railway CLI

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login & Deploy**
   ```bash
   railway login
   railway init
   railway up
   ```

## Environment Variables

Set these in Railway dashboard:

- `FLASK_ENV=production`
- `SECRET_KEY=your-super-secret-key-here`

## Custom Domain (Optional)

1. Go to your Railway project
2. Click "Settings" → "Domains"
3. Add your custom domain
4. Update DNS records as shown

## Health Check

Your app includes a health check at `/` - Railway will automatically monitor it.

## Auto-Deploy

Railway automatically redeploys when you push to your connected GitHub branch.

---

**Your trading dashboard will be live at: `https://your-app-name.railway.app`**