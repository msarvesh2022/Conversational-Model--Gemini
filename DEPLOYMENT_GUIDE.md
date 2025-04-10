# Deploying Your Gemini AI Web App

This guide provides instructions for deploying your Streamlit Gemini AI app to various hosting platforms.

## Preparation

1. Your app is already deployment-ready with these files:
   - `app.py` - The main Streamlit application
   - `deployment-requirements.txt` - Minimal dependencies for deployment
   - `Procfile` - For Heroku deployment

2. For all deployment options, you'll need to set up the `GOOGLE_API_KEY` environment variable.

## Option 1: Streamlit Cloud (Easiest)

1. Create an account at [share.streamlit.io](https://share.streamlit.io/)
2. Connect your GitHub repository
3. Set up your deployment with:
   - Repository: Your repo containing the app
   - Branch: main (or your preferred branch)
   - Main file path: app.py
   - Advanced settings: Add your `GOOGLE_API_KEY` as a secret

## Option 2: Heroku

1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Login and create a new app:
   ```bash
   heroku login
   heroku create your-app-name
   ```
3. Set your API key:
   ```bash
   heroku config:set GOOGLE_API_KEY=your_api_key
   ```
4. Deploy your app:
   ```bash
   git push heroku main
   ```

## Option 3: Railway

1. Create an account at [Railway.app](https://railway.app/)
2. Start a new project and connect your GitHub repository
3. Add your `GOOGLE_API_KEY` as an environment variable
4. Deploy with the command: `streamlit run app.py`

## Option 4: Render

1. Create an account at [Render.com](https://render.com/)
2. Create a new Web Service and connect your repository
3. Configure as:
   - Build Command: `pip install -r deployment-requirements.txt`
   - Start Command: `streamlit run app.py`
4. Add `GOOGLE_API_KEY` to environment variables

## Security Considerations

- Never commit your `.env` file to version control
- Always use environment variables for API keys
- Consider setting up request rate limiting for production use 