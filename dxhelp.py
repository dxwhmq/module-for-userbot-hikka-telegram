 # meta developer: @dxwhmq
# scope: hikka_only

from .. import loader, utils

@loader.tds
class dxwhmqHelpMod(loader.Module):
    """Стильный хелп в формате цитаты"""
    strings = {"name": "dxwhmqHelp"}

    @loader.command()
    async def dxhelp(self, message):
        """Выводит модули и их команды в формате blockquote"""
        all_modules = self.lookup("Loader").modules
        header = "<b>✧ dxwhmq_systems ✧</b>\n\n"
        
        items = []
        for mod in all_modules:
            # Получаем имя модуля
            mod_name = getattr(mod, "strings", {}).get("name", mod.__class__.__name__)
            
            # Извлекаем список команд модуля
            commands = [cmd for cmd in dir(mod) if not cmd.startswith('_') and callable(getattr(mod, cmd)) and hasattr(getattr(mod, cmd), 'command')]
            
            if commands:
                cmd_list = ", ".join(commands)
                items.append(f"▫️ <b>{mod_name}</b>: ( <code>{cmd_list}</code> )")
            else:
                items.append(f"▫️ <b>{mod_name}</b>")

        content = "\n".join(sorted(items))
        final_text = f"<blockquote>{header}{content}</blockquote>"
        
        await utils.answer(message, final_text)
     
