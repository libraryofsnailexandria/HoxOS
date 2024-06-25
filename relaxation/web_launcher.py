import webbrowser
import dearpygui.dearpygui as dpg

def launch_website(url):
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

def launch_custom_url(custom_url_id):
    url = dpg.get_value(custom_url_id)
    launch_website(url)

def web_launcher():
    with dpg.window(label="Web Launcher", autosize=True, pos=(300, 300)):
        with dpg.group(horizontal=True):
            custom_url_id = dpg.add_input_text(label="Custom URL", width=200)
            dpg.add_button(label="Launch", width=100, height=25, callback=lambda: launch_custom_url(custom_url_id))
        with dpg.group(horizontal=True):
            dpg.add_button(label="Google", width=100, height=100, callback=lambda: launch_website("https://www.google.com"))
            dpg.add_button(label="YouTube", width=100, height=100, callback=lambda: launch_website("https://www.youtube.com"))
        with dpg.group(horizontal=True):
            dpg.add_button(label="GGPT", width=100, height=100, callback=lambda: launch_website("https://google.com/"))
            dpg.add_button(label="Twitch Cap", width=100, height=100, callback=lambda: launch_website("https://www.twitch.tv/cirruslyb"))