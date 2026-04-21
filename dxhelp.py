 # meta developer: @dxwhmq
# scope: hikka_only

from .. import loader, utils

@loader.tds
class dxwhmqHelpMod(loader.Module):
    """Стильный хелп в формате цитаты"""
    strings = {"name": "dxwhmqHelp"}

    @loader.command()
    async def dxhelp(self, message):
        """Выводит список всех модулей в формате blockquote"""
        all_modules = self.lookup("Loader").modules # Достаем список через загрузчик
        out = "✧ dxwhmq_systems ✧\n\n"
        
        mods = []
        for mod in all_modules:
            name = getattr(mod, "strings", {}).get("name", mod.__class__.__name__)
            mods.append(f"▫️ {name}")
        
        out += "\n".join(sorted(mods))
        
        # Оборачиваем в blockquote (цитату)
        await utils.answer(message, f"<blockquote>{out}</blockquote>")
        
