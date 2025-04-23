# Telegram Bot

This project contains a Telegram bot implementation.

### Create your bot
1. Search for @botfather in Telegram
2. Start a conversation with BotFather by clicking on the Start button
3. Type `/newbot`, and follow the prompts to set up a new bot -> This will return you a <token> with the shape XXXX:XXXXXX
4. Start a conversation with the bot saying '/start'
4. Say something to your bot and visit this url: https://api.telegram.org/bot<token>/getUpdates -> There, you will find your <chat id> 

### Save the token and chat id
In this example project, I set them tb/local/telegram_bot_login.py as:
BOT_TOKEN=<token>
CHAT_ID=<chat id>

You can store and fetch them in another way, such as as environment variables.
