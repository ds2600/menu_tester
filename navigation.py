from netbox.plugins import PluginMenu, PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="plugins:menu_tester:github",
        link_text="GitHub",
    ),
)

menu = PluginMenu(
    label="Menu Tester",
    groups=(("External", menu_items),),
    icon_class="mdi mdi-open-in-new",
)
