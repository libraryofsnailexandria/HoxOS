import dearpygui.dearpygui as dpg
import os
import case_note as cn
import web_launcher as wl
import text_editor as te

baseDir = os.path.join(os.path.dirname(__file__), "c")
if not os.path.exists(baseDir):
    os.makedirs(baseDir)
    print(f"Directory created at: {baseDir}")


def quit_app():
    dpg.stop_dearpygui()


dpg.create_context()
dpg.create_viewport(title='HoxOS', width=1920, height=1080)

with dpg.window(label="Menu Bar", no_title_bar=True, no_resize=True, no_move=True, autosize=False, width=1920, height=100, pos=(0, 0)):
    with dpg.group(horizontal=True):
        dpg.add_button(label="QUIT",width=100, height=25, callback=quit_app)
        dpg.add_button(label="Case Notes", width=100, height=25,  callback=cn.generator)
    with dpg.group(horizontal=True):
        dpg.add_button(label="Web Launcher", width=100, height=25, callback=wl.web_launcher)
        dpg.add_button(label="Text Editor", width=100, height=25, callback=te.text_editor)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.maximize_viewport()
dpg.toggle_viewport_fullscreen()
dpg.start_dearpygui()
dpg.destroy_context()