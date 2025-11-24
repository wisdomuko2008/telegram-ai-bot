```python
import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

Add your API keys here
TELEGRAM_BOT_TOKEN = "8577644037:AAGbmvvsG6_vJlJK-SygM6bk86Ug3FpNveg"
OPENAI_API_KEY = "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"

Set your OpenAI API key
openai.api_key = OPENAI_API_KEY

Optional: For debugging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

Define response logic
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        reply = response['choices'][0]['message']['content']
    except Exception as e:
        reply = "Sorry, something went wrong."
        logging.error(e)

    await update.message.reply_text(reply)

Start the botasync def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your AI assistant 🤖. Ask me anything!")

if _name_ == "_main_":
    app = ApplicationBuilder().token(8577644037:AAGbmvvsG6_vJlJK-SygM6bk86Ug3FpNveg).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()
```
