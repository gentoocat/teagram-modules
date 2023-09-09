#                    _ _  __             _   __  __           _       _
#     /\            | | |/ /            | | |  \/  |         | |     | |
#    /  \   ___  ___| | ' / __ _ _______| | | \  / | ___   __| |_   _| | ___  ___
#   / /\ \ / __|/ _ \ |  < / _` |_  / _ \ | | |\/| |/ _ \ / _` | | | | |/ _ \/ __|
#  / ____ \\__ \  __/ | . \ (_| |/ /  __/ | | |  | | (_) | (_| | |_| | |  __/\__ \
# /_/    \_\___/\___|_|_|\_\__,_/___\___|_| |_|  |_|\___/ \__,_|\__,_|_|\___||___/

# 2023 Asel Kazel
#

from .. import loader, utils
import platform
import psutil

def bytes_to_megabytes(b: int) -> int:
    return round(b / 1024 / 1024, 1)

@loader.module("ServerInfo", "@UBteagram")
class ServerInfoMod(loader.Module):
    """Информация о сервере"""

    async def serverinfo_cmd(self, app, message):
        """Показывает информацию о сервере"""
        processor = str(platform.architecture()[0]).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        ram = bytes_to_megabytes(psutil.virtual_memory().total - psutil.virtual_memory().available)
        ram_load_mb = bytes_to_megabytes(psutil.virtual_memory().total)
        ram_load_procent = psutil.virtual_memory().percent
        plat = utils.get_platform()

        with open('/etc/os-release') as f:
            lines = f.readlines()
        distribution = ""
        for line in lines:
            if line.startswith('PRETTY_NAME='):
                distribution = line.split('=')[1].strip().strip('"')
                break

        await utils.answer(message, f"""<b>
<emoji id=5787237370709413702>⚙️</emoji> Информация о сервере

<emoji id=5235702276424737428>💎</emoji> Платформа: {plat}

Версия ОС: {platform.version()}
Система: {platform.system()} ({platform.release()})
Дистрибутив: {distribution}

<emoji id=5409076727341130651>🐍</emoji> Версия Python: {platform.python_version()}

<emoji id=5431449001532594346>⚡️</emoji> RAM: {ram}/{ram_load_mb} МБ ({ram_load_procent}%)

💾 Юб использует: {utils.get_ram()} МБ / CPU {utils.get_cpu()}%
</b>""")
