#                    _ _  __             _   __  __           _       _
#     /\            | | |/ /            | | |  \/  |         | |     | |
#    /  \   ___  ___| | ' / __ _ _______| | | \  / | ___   __| |_   _| | ___  ___
#   / /\ \ / __|/ _ \ |  < / _` |_  / _ \ | | |\/| |/ _ \ / _` | | | | |/ _ \/ __|
#  / ____ \\__ \  __/ | . \ (_| |/ /  __/ | | |  | | (_) | (_| | |_| | |  __/\__ \
# /_/    \_\___/\___|_|_|\_\__,_/___\___|_| |_|  |_|\___/ \__,_|\__,_|_|\___||___/

# 2023 Asel Kazel
#

from .. import loader, utils

@loader.module("Webshot", "@UBteagram")
class StatsMod(loader.Module):

    async def webshot_cmd(self, app, message):
        prefix = self.db.get("teagram.loader", "prefixes", ["."])[0]
        try:
            user_link = ' '.join(message.text.split(" ")[1:])
        except:
            return await message.edit(f"<b><emoji id=5440381017384822513>❌</emoji> Должно быть <code>{prefix}webshot [ссылка]</code></b>")
        if not user_link:
            return await message.edit(f"<b><emoji id=5440381017384822513>❌</emoji> Должно быть <code>{prefix}webshot [ссылка]</code></b>")
        await message.edit("<b><emoji id=5258205968025525531>📸</emoji> Делаю скриншот...</b>")
        try:
            full_link = f"https://mini.s-shot.ru/1920x1080/JPEG/1024/Z100/?{user_link}"
            await app.send_photo(message.chat.id, full_link, caption=f"<b>Screenshot of the page ⟶</b> {user_link}")
        except Exception:
            full_link = f"https://webshot.deam.io/{user_link}/?width=1920&height=1080?delay=2000?type=png"
            await app.send_photo(message.chat.id, full_link, caption=f"<b>Screenshot of the page ⟶</b> {user_link}")
        return await message.delete()
