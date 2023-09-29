import platform
import dearpygui.dearpygui as dpg
import ctypes


def removeSystemDPI():
    ctypes.windll.shcore.SetProcessDpiAwareness(2)


def makeDpgChineseLocalize(font: str = r"C:\WINDOWS\FONTS\SIMHEI.TTF", font_size=16, dpi=150):
    if platform.system() == "Windows":
        removeSystemDPI()

    with dpg.font_registry():
        with dpg.font(font, font_size * dpi // 100) as font1:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
        dpg.bind_font(font1)
    dpg.set_global_font_scale(1)


def bind_item_handler(target_tag: str | int, callback, user_data, add_item_handler):
    with dpg.item_handler_registry() as handler:
        add_item_handler(callback=callback, user_data=user_data)
    dpg.bind_item_handler_registry(target_tag, handler)


def bind_item_activated_handler(item: str | int, callback, userdata: any = None):
    bind_item_handler(item, callback, userdata, dpg.add_item_activated_handler)


def bind_item_active_handler(item: str | int, callback, userdata: any = None):
    bind_item_handler(item, callback, userdata, dpg.add_item_active_handler)


def bind_item_clicked_handler(item: str | int, callback, userdata: any = None):
    bind_item_handler(item, callback, userdata, dpg.add_item_clicked_handler)


def bind_item_deactivated_handler(item: str | int, callback, userdata: any = None):
    bind_item_handler(item, callback, userdata,
                      dpg.add_item_deactivated_handler)


def bind_item_deactivated_after_edit_handler(item: str | int, callback, userdata: any = None):
    bind_item_handler(item, callback, userdata,
                      dpg.add_item_deactivated_after_edit_handler)


def bind_item_double_clicked_handler(item: str | int, callback, userdata: any = None):
    bind_item_handler(item, callback, userdata, dpg.add_item_double_clicked_handler)


def bind_item_edited_handler(item: str | int, callback, userdata: any = None):
    bind_item_handler(item, callback, userdata, dpg.add_item_edited_handler)


def bind_item_focus_handler(item: str | int, callback, userdata: any = None):
    bind_item_handler(item, callback, userdata, dpg.add_item_focus_handler)


def bind_item_hover_handler(item: str | int, callback, userdata: any = None):
    bind_item_handler(item, callback, userdata, dpg.add_item_hover_handler)


def bind_item_resize_handler(item: str | int, callback, userdata: any = None):
    bind_item_handler(item, callback, userdata, dpg.add_item_resize_handler)


def bind_item_toggled_open_handler(item: str | int, callback, userdata: any = None):
    bind_item_handler(item, callback, userdata, dpg.add_item_toggled_open_handler)


def bind_item_visible_handler(item: str | int, callback, userdata: any = None):
    bind_item_handler(item, callback, userdata, dpg.add_item_visible_handler)
