import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import requests
import asyncio

# Bot configuration
BOT_TOKEN = "7958062748:AAECnRLxaeUMvofwyWDSxIS6EIsJ7J4LrVA"
BACKUP_CHANNEL_ID = "-1002689983399"
API_KEY = "6d207e02198a847aa98d0a2a901485a5"
UPLOAD_URL = "https://freeimage.host/api/1/upload"

async def start(update, context):
    # Create inline button for More Bots
    keyboard = [
        [InlineKeyboardButton("More Bots ✨", url="https://t.me/xiebocbobcohoce/10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Hi! 📸 Send me an image (JPG, PNG, BMP, GIF, or WEBP, up to 64MB), and I'll upload it to Freeimage.host and give you the link! 😊",
        reply_markup=reply_markup
    )

async def handle_image(update, context):
    user = update.message.from_user
    user_id = user.id
    username = user.username or None
    
    # Get the largest available photo
    photo = update.message.photo[-1] if update.message.photo else None
    if not photo:
        await update.message.reply_text("Please send a valid image! 📷")
        return

    # Download the image
    file = await context.bot.get_file(photo.file_id)
    image_data = await file.download_as_bytearray()

    # Prepare the API request
    files = {"source": (f"image_{user_id}.jpg", image_data)}  # Unique filename per user
    params = {
        "key": API_KEY,
        "action": "upload",
        "format": "json"
    }

    try:
        # Make the API call to Freeimage.host
        response = requests.post(UPLOAD_URL, files=files, data=params)
        response.raise_for_status()
        result = response.json()

        if result.get("status_code") == 200:
            image_url = result["image"]["url"]
            # Create inline buttons for user message
            keyboard = [
                [
                    InlineKeyboardButton("Image Link ⚡", url=image_url),
                    InlineKeyboardButton("More Bots ✨", url="https://t.me/xiebocbobcohoce/10")
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Send the image URL to the user
            await update.message.reply_text(
                "Image uploaded successfully! 🎉",
                reply_markup=reply_markup
            )

            # Prepare backup channel message and buttons
            if username:
                backup_text = (
                    f"New image uploaded! 📸\n"
                    f"User ID: {user_id}\n"
                    f"Username: @{username}"
                )
                backup_keyboard = [
                    [
                        InlineKeyboardButton("Private Chat 💬", url=f"https://t.me/{username.lstrip('@')}"),
                        InlineKeyboardButton("Image Link 🖼️", url=image_url)
                    ]
                ]
            else:
                backup_text = (
                    f"New image uploaded! 📸\n"
                    f"User ID: {user_id}\n"
                    f"Username: No username"
                )
                backup_keyboard = [
                    [
                        InlineKeyboardButton("Image Link 🖼️", url=image_url)
                    ]
                ]
            backup_reply_markup = InlineKeyboardMarkup(backup_keyboard)

            # Send to backup channel
            await context.bot.send_message(
                chat_id=BACKUP_CHANNEL_ID,
                text=backup_text,
                reply_markup=backup_reply_markup
            )
        else:
            await update.message.reply_text("Failed to upload the image. 😔 Please try again!")
    except Exception as e:
        await update.message.reply_text(f"Oops, something went wrong! 😕 Error: {str(e)}")

def main():
    # Get or create the event loop
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # Initialize the bot with concurrency settings
    application = Application.builder().token(BOT_TOKEN).concurrent_updates(True).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, handle_image))

    # Run the bot
    try:
        loop.run_until_complete(application.run_polling())
    finally:
        # Ensure proper shutdown
        loop.run_until_complete(application.shutdown())
        if loop.is_running():
            loop.stop()
        if not loop.is_closed():
            loop.close()

if __name__ == "__main__":
    main()