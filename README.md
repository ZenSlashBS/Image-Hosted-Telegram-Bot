Image Hoster Bot 📸


A sleek Telegram bot that uploads images to Freeimage.host and delivers shareable links in a snap! Supports JPG, PNG, BMP, GIF, and WEBP (up to 64MB), including animated GIFs, with a backup channel to track uploads.
✨ Features

⚡ Upload images and get direct links instantly
🖼️ Supports JPG, PNG, BMP, GIF, WEBP, and animated GIFs
📜 Logs uploads to a backup channel for tracking
🔘 Inline buttons for seamless navigation

🚀 Usage

Start @ImageHosterBot with /start
Send an image
Receive a shareable link with inline buttons

🛠️ Setup

Clone the repo:
git clone https://github.com/ZenSlashBS/Image-Hoster-Telegram-Bot.git


Install dependencies:
pip install python-telegram-bot requests


Configure imghost.py with these variables:

BOT_TOKEN: Get your Telegram Bot Token from @BotFather
API_KEY: Obtain your Freeimage.host API key from Freeimage.host
BACKUP_CHANNEL_ID: Telegram channel ID (e.g., -1001234567890) for logging uploads; ensure bot has send message permissions
UPLOAD_URL: Freeimage.host API endpoint (default: https://freeimage.host/api/1/upload)


Run the bot:
python imghost.py



📋 Dependencies

python-telegram-bot (v20.0+)
requests

🤝 Contributing
Got ideas? Submit pull requests or open issues on GitHub.
📜 License
This project is unlicensed.
📬 Contact
Explore more bots at t.me/xiebocbobcohoce/10.

⭐ Star the repo if you find it useful! ⭐
