import os
from telegram import Update, ChatAdministratorRights
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ========================
# CONFIG
# ========================
OWNER_ID = 7911959778  # Sirf ye ID /makeadmin use kar sakti hai
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Render me Environment Variable set kare

if not BOT_TOKEN:
    raise Exception("Please set BOT_TOKEN environment variable before running the bot.")

# ========================
# /makeadmin Command
# ========================
async def make_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type not in ["group", "supergroup"]:
        await update.message.reply_text("⚠️ Ye command sirf group me kaam karta hai.")
        return

    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    if user_id != OWNER_ID:
        await update.message.reply_text("❌ Ye command sirf owner ke liye hai.")
        return

    bot_member = await context.bot.get_chat_member(chat_id, context.bot.id)
    if not bot_member.can_promote_members:
        await update.message.reply_text("❌ Bot ke paas Add Admins permission nahi hai. Bot ko promote rights do.")
        return

    try:
        rights = ChatAdministratorRights(
            is_anonymous=False,
            can_manage_chat=True,
            can_delete_messages=True,
            can_manage_video_chats=True,
            can_restrict_members=True,
            can_promote_members=True,
            can_change_info=True,
            can_invite_users=True,
            can_post_messages=True,
            can_edit_messages=True,
            can_pin_messages=True
        )
        await context.bot.promote_chat_member(chat_id, user_id, rights)
        await update.message.reply_text("✅ Ab tum admin ban gaye ho! 🎉")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {e}")

# ========================
# Start Command
# ========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Admin Maker Bot ready hai!\n"
        "Use /makeadmin in the group to promote yourself (owner only)."
    )

# ========================
# Main Function
# ========================
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("makeadmin", make_admin))

    print("✅ Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
