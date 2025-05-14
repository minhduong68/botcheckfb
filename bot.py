from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Thay TOKEN của bạn vào đây
BOT_TOKEN = "7459867855:AAGDdKuirFAm8T6HjLHbLXjRErH1fdSCrfM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Xin chào! Tôi là bot của bạn.")

async def check_uid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Ví dụ lệnh /check sẽ trả về UID của người dùng gửi
    user_id = update.message.from_user.id
    await update.message.reply_text(f"UID của bạn là: {user_id}")

# Khởi tạo bot với token
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Thêm handler cho các lệnh
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("check", check_uid))

# Chạy bot
print("Bot đang chạy...")
app.run_polling()
