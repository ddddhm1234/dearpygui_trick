### Description
dearpygui_trick offers some tricks to make dearpygui better for use.

### Examples
* Localize
```
import dearpygui.dearpygui as dpg
import dearpygui_ext.utilities
import dearpygui_trick


def print_value(sender):
    print(sender)
    print(dpg.get_value(sender))

dpg.create_context()

dearpygui_trick.makeDpgChineseLocalize() # --> Chinese localize


```

* Bind item handler more quickly
```
    dearpygui_trick.bind_item_double_clicked_handler(input_txt1, print_value) --> bind item events in one-line code
```