import dearpygui.dearpygui as dpg

def generate_case_note():
    cid = dpg.get_value("CID")
    username = dpg.get_value("Username")
    issue = dpg.get_value("Issue")
    lpv = dpg.get_value("LPV")
    resolution = dpg.get_value("Resolution")
    case_note = f"Case ID: {cid}\n" \
                f"Username: {username}\n" \
                f"Issue: {issue}\n" \
                f"LPV: {lpv}\n" \
                f"Resolution: {resolution}"
    print(case_note)
    with dpg.window(label="Generated Case Note", width=300, height=500, no_resize=True, pos=(320, 320)):
        dpg.add_input_text(default_value=case_note, multiline=True, width=290, height=450)


def generator():
    with dpg.window(label="Case Notes", width=500, height=500, no_resize=True, pos=(300, 300)):
        label = dpg.add_text("Case Notes")
        with dpg.tooltip(parent=label):
            dpg.add_text("Fill in the respective fields\n"
                         "to generate a case note.")
        dpg.add_input_text(label="CID", width=400, tag="CID")  
        dpg.add_input_text(label="Username", width=400, tag="Username")  
        dpg.add_input_text(label="Issue", width=400, multiline=True, tag="Issue")
        dpg.add_input_text(label="LPV", width=400, tag="LPV")  
        dpg.add_input_text(label="Resolution", width=400, multiline=True, tag="Resolution") 
        dpg.add_button(label="Generate", width=300, height=50, callback=generate_case_note)