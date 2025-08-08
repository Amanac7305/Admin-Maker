# Admin Maker Bot (Render-ready)

**Purpose:** Minimal Telegram bot that allows only the owner (ID: 7911959778) to run `/makeadmin` in a group.  
When the owner runs `/makeadmin` in a group where the bot has the **Promote Members** permission, the bot will promote the owner with all possible admin rights the bot itself has.

## Files
- `main.py` - Bot code
- `requirements.txt` - Python dependencies

## How to deploy on Render
1. Push these files to a new GitHub repository.
2. On Render, create **New → Web Service** and connect your repo.
3. Set the Environment Variable:
   - `BOT_TOKEN` = `<your-telegram-bot-token>`
4. Use the Start Command:
   ```bash
   python main.py
