Image Hoster Bot for Telegram
Introduction
📸 Capture, Upload, Share! The Image Hoster Bot for Telegram lets you upload images to Freeimage.host and get direct links right in your chat. Whether it’s a stunning photo, a hilarious meme, or a smooth animated GIF, this bot makes sharing effortless. With support for files up to 64MB and a backup channel for tracking uploads, it’s your go-to tool for image hosting on Telegram. 🚀
Features

⚡ Instant Uploading: Send an image and get a shareable link in seconds.
🌈 Multiple Formats: Supports JPG, PNG, BMP, GIF, and WEBP.
📏 Large File Support: Handles images up to 64MB.
🎬 Animated GIFs: Share animations without losing their charm.
📚 Backup Channel: Logs all uploads with user details for easy tracking.
🤝 User-Friendly Interface: Inline buttons for quick access to links and more bots.

Why Use This Bot?

Convenience: Upload and share images without leaving Telegram.
Speed: Fast uploads powered by Freeimage.host’s API.
Versatility: Perfect for photos, memes, or animated GIFs.
Reliability: All uploads are backed up in a dedicated channel for peace of mind.

How to Use

Start the bot by sending /start in a private chat with @ImageHosterBot.
Send an image (JPG, PNG, BMP, GIF, or WEBP).
Receive a message with a direct link to your uploaded image and inline buttons to:
Access the image link.
Explore more bots via a provided link.



Example Interaction:

You send a photo.
The bot replies:"Image uploaded successfully! 🎉"Image Link ⚡More Bots ✨

In Action
When you send an image, the bot processes it using the Freeimage.host API and responds with a direct link. Inline buttons make it easy to view the image or discover other bots. Behind the scenes, the bot logs the upload to a backup channel, including the user’s ID, username (if available), and the image link. This ensures you can track uploads or contact users if needed.
Technical Details
The bot is built with Python using the python-telegram-bot library (version 20.0+ for async support). It uses the Freeimage.host API to upload images asynchronously, ensuring smooth performance even with large files. The bot handles errors gracefully, notifying users if an upload fails.
Key Components



Component
Description



/start Command
Initiates the bot with a welcome message and inline button.


Image Handler
Processes sent images, uploads them, and returns links.


Backup Channel
Logs uploads with user details and links.


Inline Buttons
Provides quick access to image links and external resources.


Setting Up and Running
Want to run your own instance of the Image Hoster Bot? Follow these steps:

Clone the Repository:
git clone https://github.com/yourusername/image-host-bot.git


Install Dependencies:
pip install python-telegram-bot requests


Configure the Bot:

Get a Telegram Bot Token from @BotFather.

Obtain a Freeimage.host API key from Freeimage.host.

Update the imghost.py file with your credentials:
BOT_TOKEN = "your_bot_token_here"
API_KEY = "your_api_key_here"
BACKUP_CHANNEL_ID = "your_channel_id_here"
UPLOAD_URL = "https://freeimage.host/api/1/upload"




Run the Bot:
python imghost.py



Note: Ensure the backup channel ID is for a channel where the bot has permission to send messages.
Dependencies

python-telegram-bot (version 20.0 or later for async support)
requests

Contributing
Contributions are welcome! Feel free to submit pull requests or open issues on the GitHub repository to suggest improvements or report bugs.
License
This project is licensed under the MIT License - see the LICENSE.md file for details.
Contact
For questions or support, reach out via Telegram or check out more bots at More Bots.
