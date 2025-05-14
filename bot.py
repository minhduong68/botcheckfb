from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import re

# Thay BOT_TOKEN của bạn vào đây
BOT_TOKEN = "7459867855:AAGDdKuirFAm8T6HjLHbLXjRErH1fdSCrfM"

# Đặt nơi lưu trữ UID và tên
user_data = {}

# Lệnh /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Xin chào! Tôi là bot ẢO CÔNG TỬ - AKATSUKI TRICKER TEAM. Hãy gửi link Facebook để tôi lấy UID.")

# Lệnh /check (kiểm tra UID)
async def check_uid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 1:
        fb_link = context.args[0]
        user_id = get_uid_from_fb(fb_link)
        if user_id:
            await update.message.reply_text(f"UID của người dùng là: {user_id}")
            user_data[user_id] = {'status': 'live', 'name': 'Chưa đặt tên'}  # Thêm UID vào user_data
        else:
            await update.message.reply_text("Không thể lấy UID từ link Facebook này.")
    else:
        await update.message.reply_text("Vui lòng gửi link Facebook kèm theo lệnh: /check <facebook_link>")

# Lệnh /save (lưu UID và tên)
async def save_uid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 2:
        user_id = context.args[0]
        user_name = context.args[1]
        
        if user_id in user_data:
            user_data[user_id]['name'] = user_name
            await update.message.reply_text(f"UID {user_id} đã được lưu với tên: {user_name}")
        else:
            await update.message.reply_text(f"UID {user_id} chưa được kiểm tra. Vui lòng kiểm tra UID trước.")
    else:
        await update.message.reply_text("Vui lòng gửi lệnh: /save <uid> <name>")

# Lệnh /status (kiểm tra trạng thái sống chết của UID)
async def check_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 1:
        user_id = context.args[0]
        if user_id in user_data:
            status = user_data[user_id]['status']
            await update.message.reply_text(f"UID {user_id} hiện tại có trạng thái: {status}")
        else:
            await update.message.reply_text(f"UID {user_id} chưa được lưu trữ.")
    else:
        await update.message.reply_text("Vui lòng gửi lệnh: /status <uid>")

# Hàm để lấy UID từ link Facebook (bạn có thể thay thế với API hoặc logic khác)
def get_uid_from_fb(fb_link):
    # Sử dụng một regex để trích xuất UID từ link Facebook
    match = re.search(r"facebook.com\/(.*?)(?=\?|$)", fb_link)
    if match:
        return match.group(1)
    else:
        return None

# Khởi tạo bot với token
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Thêm handler cho các lệnh
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("check", check_uid))
app.add_handler(CommandHandler("save", save_uid))
app.add_handler(CommandHandler("status", check_status))

# Chạy bot
print("Bot đang chạy...")
app.run_polling()
