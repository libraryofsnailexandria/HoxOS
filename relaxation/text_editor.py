import dearpygui.dearpygui as dpg
import os

baseDir = os.path.join(os.path.dirname(__file__), "c")
if not os.path.exists(baseDir):
    os.makedirs(baseDir)
    print(f"Directory created at: {baseDir}")

currentPath = ""

def display_dir(sender, app_data, user_data):
    global currentPath
    currentPath = dpg.get_value("filepath")
    fullPath = os.path.normpath(os.path.join(baseDir, currentPath.strip("/")))
    if not fullPath.startswith(baseDir):
        fullPath = baseDir
    entriesList = []

    for entry in os.listdir(fullPath):
        entryPath = os.path.join (fullPath, entry)
        if os.path.isdir(entryPath):
            entriesList.append(entry + "/")
        else:
            entriesList.append(entry)

    entriesStr = "\n".join(entriesList)
    dpg.set_value("fileList", entriesStr)

def load_txt(sender, app_data, user_data):
    global currentPath
    directory = currentPath
    filename = dpg.get_value("fileOpen")
    full_path = os.path.join(baseDir, directory, filename)
    if os.path.exists(full_path) and full_path.endswith(".txt"):
        with open(full_path, "r") as file:
            textContent = file.read()
        dpg.set_value("editor_field", textContent)
    else:
        warning = "No file of that name in directory..."
        dpg.set_value("editor_field", warning)
        pass

def save_txt(sender, app_data, user_data):
    global currentPath
    directory = currentPath
    filename = dpg.get_value("fileOpen")
    full_path = os.path.join(baseDir, directory, filename)
    textContent = dpg.get_value("editor_field")
    if os.path.exists(full_path) and full_path.endswith(".txt"):
        try:
            with open(full_path, "w") as file:
                file.write(textContent)
            with dpg.window(label="Console Dialog", autosize=True, no_resize=True,):
                dpg.add_text(default_value="Content was saved sucessfuly")
        except:
            with dpg.window(label="Console Dialog", autosize=True, no_resize=True,):
                dpg.add_text(default_value="An error has occured...")
    else:
        try:
            newFile = os.path.join(baseDir, directory, filename)
            with open(newFile, "w") as file:
                file.write(textContent)
            with dpg.window(label="Console Dialog", autosize=True, no_resize=True,):
                dpg.add_text(default_value="New file was made")
        except:
            with dpg.window(label="Console Dialog", autosize=True, no_resize=True,):
                dpg.add_text(default_value="An error has occured...")
        

def load_file():
    if dpg.does_item_exist("Load File Window"):
        dpg.delete_item("Load File Window")
    with dpg.window(label="Load File", tag="Load File Window", autosize=False, no_resize=True):
        with dpg.group(horizontal=True):
            dpg.add_input_text(width=400, tag="filepath")
            dpg.add_button(width=100, label="open dir", callback=display_dir)
        with dpg.child_window(width=500, height=500):
            dpg.add_text(default_value="No files to load", tag="fileList")
        with dpg.group(horizontal=True):
            dpg.add_input_text(width=400, tag="fileOpen")
            dpg.add_button(width=100, label="open file", tag="opentxt", callback=load_txt)

def text_editor():    
    with dpg.window(label="Text Editor", autosize=True):
        with dpg.group(horizontal=True):
            dpg.add_button(label="Open", width=75, height=35, callback=load_file)
            dpg.add_button(label="Save", width=75, height=35, callback=save_txt)
        dpg.add_input_text(width= 600, height=800, multiline=True, tag="editor_field")
