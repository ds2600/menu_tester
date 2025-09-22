from netbox.plugins import PluginConfig

class MenuTesterConfig(PluginConfig):
    name = "menu_tester"
    verbose_name = "Menu Tester"
    description = "Simplest test plugin to show a menu item."
    version = "0.1.0"
    base_url = "menu-tester"
    default_settings = {
        'top_level_menu': True,
    }

    def ready(self):
        super().ready()


config = MenuTesterConfig
