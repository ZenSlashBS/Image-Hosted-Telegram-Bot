# Image Hoster Bot 📸

![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)<br>A Telegram bot that uploads images to Freeimage.host and delivers shareable links in a snap! Supports JPG, PNG, BMP, GIF, and WEBP (up to 64MB), including animated GIFs, with a backup channel to track uploads.

## ✨ Features

- ⚡ Upload images and get direct links instantly
- 🖼️ Supports JPG, PNG, BMP, GIF, WEBP, and animated GIFs
- 📜 Logs uploads to a backup channel for tracking
- 🔘 Inline buttons for seamless navigation

## 🚀 Usage

1. Start `@ImageHosterBot` with `/start`
2. Send an image
3. Receive a shareable link with inline buttons

## 🛠️ Setup

1. **Clone the repo**:

   ```bash
   git clone https://github.com/ZenSlashBS/Image-Hoster-Telegram-Bot.git
   ```

2. **Install dependencies**:\
   Create a `requirements.txt` file (included in the repo) and run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure** `imghost.py` with these variables:

   - `BOT_TOKEN`: Get your Telegram Bot Token from @BotFather
   - `API_KEY`: Obtain your Freeimage.host API key from Freeimage.host
   - `BACKUP_CHANNEL_ID`: Telegram channel ID (e.g., `-1001234567890`) for logging uploads; ensure bot has send message permissions
   - `UPLOAD_URL`: Freeimage.host API endpoint (default: `https://freeimage.host/api/1/upload`)

4. **Run the bot**:

   ```bash
   python imghost.py
   ```

## 📋 Dependencies

- python-telegram-bot (v20.0+)
- requests
- asyncio (built-in with Python 3.8+)

## 🤝 Contributing

Got ideas? Submit pull requests or open issues on GitHub.

## 📜 License

This project is unlicensed.

## 📬 Contact

Explore more bots at t.me/xiebocbobcohoce/10.

---

⭐ **Star the repo if you find it useful!** ⭐
