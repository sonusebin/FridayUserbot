from telethon.events import ChatAction
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from fridaybot import bot, sclient
from fridaybot.Configs import Config

"""Bans Spammers/Scammer At time Of Arrival 
If You Add Him The Bot Won't Restrict."""

json_codes = {
    'nsX01': 'Pornography - High Risk',
    'nsX02': 'Spammer - High Risk',
    'nsX03': 'Spam Adding Users - High Risk',
    'nsX04': 'Raid Participants - High Risk',
    'nsX05': 'Licence violation - Low Risk',
    'nsX06': 'Spam Bot - High Risk',
    'nsX07': 'Flood - High Risk',
    'nsX08': 'Malware - High Risk',
    'nsX09': 'PM Spam - High Risk',
    'nsX10': 'Power Misuser - Medium Risk',
    'nsX11': 'Multiple Risks - Extreme Risk',
    'nsX12': 'Scam - Extreme Risk'
}

@borg.on(ChatAction)
async def ok(event):
    juser = await event.get_user()
    if Config.ANTISPAM_FEATURE != "ENABLE":
        return
    if event.user_joined:
        hmmyep = await borg.get_permissions(event.chat_id, bot.uid)
        if not hmmyep.is_admin:
            return
        user = sclient.is_banned(juser.id)
        if user:
            await event.reply(
                f"**#FRIDAY ANTISPAM** \n**Detected Malicious User.** \n**User-ID :** `{juser.id}`  \n**Reason :** `{user.ban_code} - {user.reason}`"
            )
            try:
                await borg.edit_permissions(
                    event.chat_id, juser.id, view_messages=False
                )
            except:
                pass
        else:
            pass

@borg.on(ChatAction)
async def ok(event):
    noobie = await event.get_user()
    juser = await event.client(GetFullUserRequest(noobie.id))
    if Config.ANTISPAM_FEATURE != "ENABLE":
        return
    if event.user_joined:
        if "@date4ubot" in juser.user.about:
            hmm = sclient.ban(juser.user.id, 'nsX06')
            await borg.send_message(-1001300453052, f"Banned : {juser.user.id} \nReason : nsX06")
            await borg.send_message("nospamplusfed", f"/fban {juser.user.id} nsX06 // {json_codes['nsX06']}")
            hmmyep = await borg.get_permissions(event.chat_id, bot.uid)
            if not hmmyep.is_admin:
                return
            await event.reply('`SpamBot Detected In This Chat !`')
            try:
                await borg.edit_permissions(
                        event.chat_id, juser.user.id, view_messages=False
                    )
            except:
                pass
    else:
        pass
    
@borg.on(events.NewMessage)
async def ok(event):
    juser = await event.client(GetFullUserRequest(event.sender_id))
    if Config.ANTISPAM_FEATURE != "ENABLE":
        return
    if "@date4ubot" in juser.user.about:
            hmm = sclient.ban(juser.user.id, 'nsX06')
            await borg.send_message(-1001300453052, f"Banned : {juser.user.id} \nReason : nsX06")
            await borg.send_message("nospamplusfed", f"/fban {juser.user.id} nsX06 // {json_codes['nsX06']}")
            hmmyep = await borg.get_permissions(event.chat_id, bot.uid)
            if not hmmyep.is_admin:
                return
            await event.reply('`SpamBot Detected In This Chat !`')
            try:
                await borg.edit_permissions(
                        event.chat_id, juser.user.id, view_messages=False
                    )
            except:
                pass
    else:
        pass

    
@borg.on(ChatAction)
async def dnamg(event):
    okbruh = await borg.get_me()
    if event.user_added == okbruh.id:
        event.chat_id
        lolll = await event.get_added_by()
        added_bys = lolll.id
        lolchat = await event.get_chat()
        if lolchat.username:
            is_pvt = False
            lmao_info = lolchat.username
        else:
            is_pvt = True
            lmao_info = lolchat.id
        try:
            await event.reply(
                "**Wait, How Dare You Add Me To This Group, Without My Permission, Never Mind You Are Gonna Get Reported Lol !**"
            )
        except:
            pass
        await borg.kick_participant(event.chat_id, okbruh.id)
        await borg.send_message(
            Config.PRIVATE_GROUP_ID,
            f"**WARNING - SPAM ADDING** \nUSER : `{added_bys}` \nCHAT : `{lmao_info}` \nGROUP PRIVATE : `{is_pvt}` \n**You May Report This At @SpamWatch Or @NospamPlusChat.**",
        )
