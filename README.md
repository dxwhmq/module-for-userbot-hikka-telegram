# meta developer: @dxwhmq
# scope: hikka_only

from .. import loader, utils

loader.tds
class dxwhmqHelpMod(loader.Module):
    """Стильный хелп в формате цитаты (blockquote)"""
    strings = {"name": "dxwhmqHelp"}

    async def helpcmd(self, message):
        """Выводит список всех модулей в формате blockquote"""
        all_modules = self.all_modules
        out = "✧ dxwhmq_systems ✧\n\n"
        
        mods = []
        for mod in all_modules:
            try:
                # Берем имя модуля из его строк
                name = mod.strings.get('name', mod.__class__.__name__)
                mods.append(f"▫️ {name}")
            except:
                continue
        
        out += "\n".join(sorted(mods))
        
        # Оборачиваем в blockquote для эффекта цитаты
        # Используем HTML парс-мод, чтобы телега поняла тег
        await utils.answer(message, f"<blockquote>{out}</blockquote>")
        
