# meta developer: @dxwhmq
# scope: hikka_only

from .. import loader, utils

@loader.tds
class dxwhmqHelpMod(loader.Module):
    """Стильный хелп в формате цитаты"""
    strings = {"name": "dxwhmqHelp"}

    @loader.command()
    async def dhelp(self, message):
        """Выводит модули и их команды в формате blockquote"""
        # Обращаемся напрямую к списку загруженных модулей
        all_modules = self._loader.modules
        
        header = "<b>✧ dxwhmq_systems ✧</b>\n\n"
        
        items = []
        for mod in all_modules:
            mod_name = getattr(mod, "strings", {}).get("name", mod.__class__.__name__)
            
            # Получаем команды через словарь commands модуля
            commands = []
            if hasattr(mod, "commands"):
                commands = list(mod.commands.keys())
            
            if commands:
                cmd_list = ", ".join(commands)
                items.append(f"▫️ <b>{mod_name}</b>: ( <code>{cmd_list}</code> )")
            else:
                items.append(f"▫️ <b>{mod_name}</b>")

        content = "\n".join(sorted(items))
        final_text = f"<blockquote>{header}{content}</blockquote>"
        
        await utils.answer(message, final_text)
     
