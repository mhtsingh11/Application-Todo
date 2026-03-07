import funtions
import FreeSimpleGUI as sg


label = sg.Text("Type a member name")

input_box = sg.InputText(tooltip="Enter member")

button = sg.Button("Add")

window = sg.Window("My Members App", layout=[[label], [input_box, button]])
window.read()
window.close()