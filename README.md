# Image Hoster Bot

![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)<br> A Telegram bot to upload images to Freeimage.host and get shareable links instantly. Supports JPG, PNG, BMP, GIF, WEBP (up to 64MB), including animated GIFs, with a backup channel for tracking uploads.

## ✨ Features

- Upload images and get direct links in seconds
- Supports multiple formats and animated GIFs
- Logs uploads to a backup channel
- Inline buttons for easy navigation

## 🚀 Usage

1. Start `@ImageHosterBot` with `/start`
2. Send an image
3. Get a shareable link with inline buttons

## 🛠️ Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/ZenSlashBS/Image-Hoster-Telegram-Bot.git
   ```

2. Install dependencies:

   ```bash
   pip install python-telegram-bot requests asycnio
   ```

3. Configure `imghost.py` with the following variables:

   - `BOT_TOKEN`: Your Telegram Bot Token from @BotFather
   - `API_KEY`: Your Freeimage.host API key from Freeimage.host
   - `BACKUP_CHANNEL_ID`: The Telegram channel ID (e.g., `-1001234567890`) where uploads are logged; ensure the bot has permission to send messages
   - `UPLOAD_URL`: The Freeimage.host API endpoint (default: `https://freeimage.host/api/1/upload`)

4. Run the bot:

   ```bash
   python imghost.py
   ```

## 📋 Dependencies

- python-telegram-bot
- requests
- asyinco

## 🤝 Contributing

Submit pull requests or issues on GitHub.

## 📜 License

This tool is not licensed.

## 📬 Contact

Check out more bots at t.me/xiebocbobcohoce/10.
