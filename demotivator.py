#                    _ _  __             _   __  __           _       _
#     /\            | | |/ /            | | |  \/  |         | |     | |
#    /  \   ___  ___| | ' / __ _ _______| | | \  / | ___   __| |_   _| | ___  ___
#   / /\ \ / __|/ _ \ |  < / _` |_  / _ \ | | |\/| |/ _ \ / _` | | | | |/ _ \/ __|
#  / ____ \\__ \  __/ | . \ (_| |/ /  __/ | | |  | | (_) | (_| | |_| | |  __/\__ \
# /_/    \_\___/\___|_|_|\_\__,_/___\___|_| |_|  |_|\___/ \__,_|\__,_|_|\___||___/

# 2023 Asel Kazel
#

from .. import loader
import asyncio

@loader.module("Demotivator", "@gentoocat")
class DemotivatorMod(loader.Module):
    """Делает demotivator"""

    async def demotivator_cmd(self, app, message):
        """Создание демотиватора"""
        username_dem = "@super_rjaka_demotivator_bot"
        await message.edit("<b><emoji id=5325731315004218660>🔄</emoji> Создание демотиватора...</b>")
        if message.reply_to_message.photo:
            await app.unblock_user(username_dem)
            try:
               capt = ' '.join(message.text.split(" ")[1:])
            except:
                prefix = self.db.get("teagram.loader", "prefixes", ["."])[0]
                return await message.edit(f"<b><emoji id=5440381017384822513>❌</emoji> Должно быть <code>{prefix}demotivator текст_который_будет_снизу</code></b>")
            if not capt:
                prefix = self.db.get("teagram.loader", "prefixes", ["."])[0]
                return await message.edit(f"<b><emoji id=5440381017384822513>❌</emoji> Должно быть <code>{prefix}demotivator текст_который_будет_снизу</code></b>")
            await app.send_message(chat_id=username_dem, text="/start")
            await asyncio.sleep(1)
            await app.send_photo(
                chat_id=username_dem,
                photo=message.reply_to_message.photo.file_id,
                caption=capt
            )
            photo = False

            while not photo:
                try:
                    await asyncio.sleep(4)
                    h = app.get_chat_history(username_dem, limit=1)
                    async for iii in h:
                        await app.send_photo(chat_id=message.chat.id, photo=iii.photo.file_id)
                        break
                    async for i in app.get_chat_history(username_dem, limit=4):
                        await i.delete()
                    photo = True
                    await message.delete()
                except Exception as f:
                    await message.edit(str(f))
                    await asyncio.sleep(2)
        else:
            return await message.edit(f"<b><emoji id=5440381017384822513>❌</emoji> Должно быть ответом на фото</b>")
