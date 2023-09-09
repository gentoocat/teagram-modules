#                    _ _  __             _   __  __           _       _
#     /\            | | |/ /            | | |  \/  |         | |     | |
#    /  \   ___  ___| | ' / __ _ _______| | | \  / | ___   __| |_   _| | ___  ___
#   / /\ \ / __|/ _ \ |  < / _` |_  / _ \ | | |\/| |/ _ \ / _` | | | | |/ _ \/ __|
#  / ____ \\__ \  __/ | . \ (_| |/ /  __/ | | |  | | (_) | (_| | |_| | |  __/\__ \
# /_/    \_\___/\___|_|_|\_\__,_/___\___|_| |_|  |_|\___/ \__,_|\__,_|_|\___||___/

# 2023 Asel Kazel
#

import os
import qrcode
from .. import loader

@loader.module("QRcode", "@gentoocat")
class QRcodeMod(loader.Module):
    """Делает QRcode"""

    async def qrcode_cmd(self, message):
        """Создание qrcode"""
        await message.edit("<b><emoji id=5325731315004218660>🔄</emoji> Создание QRcode...</b>")
        app = self.client
        try:
            txt = ' '.join(message.text.split(" ")[1:])
        except:
            prefix = self.db.get("teagram.loader", "prefixes", ["."])[0]
            return await message.edit(f"<b><emoji id=5440381017384822513>❌</emoji> Должно быть <code>{prefix}qrcode [text]</code></b>")
        if not txt:
            prefix = self.db.get("teagram.loader", "prefixes", ["."])[0]
            return await message.edit(f"<b><emoji id=5440381017384822513>❌</emoji> Должно быть <code>{prefix}qrcode [text]</code></b>")

        img = qrcode.make(txt)
        img.save('assets/code.png')

        with open('assets/code.png', 'rb') as photo:
           await utils.answer(message, photo, photo=True, caption=f'<b>Ваш QRcode с текстом <code>{txt}</code> создан</b>')
           return await message.delete()
