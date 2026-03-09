import funtions
import FreeSimpleGUI as sg


label = sg.Text("Type a member name")

input_box = sg.InputText(tooltip="Enter member", key = "Member")

button = sg.Button("Add")

window = sg.Window("My Members App",
                   layout=[[label], [input_box, button]],
                   font=("Helvetica", 12))

while True:
    event, value = window.read()
    print(event)
    print(value)
    if (event == "Add"):
        members= funtions.read_lines_members_file()
        new_member = value["Member"]
        members.append(new_member + "\n")
        funtions.write_lines_members_file(members)
    if event == sg.WINDOW_CLOSED:
        break

window.close()