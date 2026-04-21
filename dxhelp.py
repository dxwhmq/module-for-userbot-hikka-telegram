# meta developer: @dxwhmq
# scope: hikka_only

from .. import loader, utils

@loader.tds
class dxwhmqHelpMod(loader.Module):
    """dhelp"""
    strings = {"name": "dxwhmqHelp"}

    @loader.command()
    async def dhelp(self, message):
        """blockquote help"""
        all_modules = self._client.loader.modules
        header = "<b>✧ dxwhmq_systems ✧</b>\n\n"
        
        items = []
        for mod in all_modules:
            mod_name = getattr(mod, "strings", {}).get("name", mod.__class__.__name__)
            commands = list(getattr(mod, "commands", {}).keys())
            
            if commands:
                cmd_list = ", ".join(commands)
                items.append(f"▫️ <b>{mod_name}</b>: ( <code>{cmd_list}</code> )")
            else:
                items.append(f"▫️ <b>{mod_name}</b>")

        content = "\n".join(sorted(items))
        await utils.answer(message, f"<blockquote>{header}{content}</blockquote>")
        
