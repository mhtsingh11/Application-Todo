import funtions
import FreeSimpleGUI as sg


label = sg.Text("Type a member name")

input_box = sg.InputText(tooltip="Enter member", key = "Member")

button = sg.Button("Add")

window = sg.Window("My Members App",
                   layout=[[label], [input_box, button]],
                   font=("Helvetica", 12))

event = window.read()
print(event)
window.close()