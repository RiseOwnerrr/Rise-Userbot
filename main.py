import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import Message

# Aapki API details
API_ID = 27013344
API_HASH = "be5f160b65f07128459b4289c6e286ad"
STRING_SESSION = os.getenv("BQGcMOAAYe-p6fuwspYfKnPx1p3yZmjTrZ_tlf44K_aj9md4Indrqh2pi6MRBNNxRTdevZKFyBSeLsQSWjiXi8Jgy5jJe2b28QNoNxtMIU6zqHTAe2mpCk0VFr_A7XYeZlURkdMMdvr531Bstt4BVj6UxPzeAzD21WwZz6d-0FgjzInVYt0drZ3q118R8APFLb-DbKZCX0yQ-4AZM-clP5c9ynk5e3_3Oc7q07j0m5DlpYMKSssS6Fw_c7dFnHA6f72gVgAR4Suc7Gw_rphfi_l8YGfrYIHPRrq51_ASWESO6-6zP21TuEYKUDDkfudQv_eJL554OmUg7YtQEQ8nEtyS19WPUgAAAAIUWiufAA ( mera string session")

# Pyrogram Client initialize karna
app = Client(
    "rise_userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

# 1. MEMBER TAGGING FEATURE (.tagall)
@app.on_message(filters.command("tagall", prefixes=".") & filters.me)
async def tag_all(client: Client, message: Message):
    chat_id = message.chat.id
    args = message.text.split(maxsplit=1)
    custom_text = args[1] if len(args) > 1 else "Attention everyone! 🚨"
    
    try:
        await message.delete()
    except Exception:
        pass
    
    tag_text = f"{custom_text}\n\n"
    count = 0
    
    async for member in client.get_chat_members(chat_id):
        if member.user.is_bot or member.user.is_deleted:
            continue
            
        tag_text += f"[{member.user.first_name}](tg://user?id={member.user.id}) "
        count += 1
        
        if count >= 10:
            await client.send_message(chat_id, tag_text)
            tag_text = ""
            count = 0
            await asyncio.sleep(2)
            
    if tag_text.strip():
        await client.send_message(chat_id, tag_text)


# 2. BROADCASTING FEATURE (.broadcast)
@app.on_message(filters.command("broadcast", prefixes=".") & filters.me)
async def broadcast_msg(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit("❌ Kripya kisi message ko reply karke .broadcast command use karein!")
        return
    
    # Yahan apne target groups ki chat IDs (-100xxxxxxx) daal sakte hain
    target_chat_ids = [] 
    
    success = 0
    failed = 0
    status_msg = await message.edit("📢 Broadcast shuru ho raha hai...")
    
    for chat_id in target_chat_ids:
        try:
            await message.reply_to_message.copy(chat_id)
            success += 1
            await asyncio.sleep(1.5)
        except Exception as e:
            failed += 1
            
    await status_msg.edit(f"✅ **Broadcast Complete!**\n- Success: `{success}`\n- Failed: `{failed}`")


if __name__ == "__main__":
    print("Rise UserBot start ho raha hai...")
    app.run()
