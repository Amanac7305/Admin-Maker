# Admin Maker Bot

## Features
- Sirf OWNER_ID (apni Telegram numeric ID) se /makeadmin command chal sakta hai.
- Bot khud ko group me admin bana dega jab tu command dega (agar bot ko "Add Admins" rights mil jaaye).
- Security: Kisi aur ko admin nahi banayega.

## Deploy Kaise Kare (Render pe):

1. **Repo Structure:**
   - `bot.py` (main code)
   - `requirements.txt` (yahi file)
   - `README.md` (ye file)

2. **Render.com pe:**
   - New Web Service create kar, Python select kar.
   - Apna GitHub repo link de.
   - Environment Variables set kar:
     - `BOT_TOKEN` = Apne Telegram bot ka token
     - `OWNER_ID` = Apni Telegram numeric ID (ya default code me hi daal sakte ho)

3. **Bot ko Group me Add Kar:**
   - Bot ko group me daal.
   - Bot ko “Add Admins” permission de.

4. **Use:**
   - Group me `/makeadmin` likh.
   - Sirf OWNER_ID user ke liye kaam karega.
   - Admin rights mil jayenge!

## Note

- Bot ko admin bana ke "Add Admins" rights zaroor de.
- Owner ID change karna ho to environment variable ya code me update kar sakte ho.

---

## English Guide

- Only the OWNER_ID can use /makeadmin and get admin rights.
- Must give bot "Add Admins" permission in your group.
- Deploy on Render with your bot token and owner id as environment variables.
