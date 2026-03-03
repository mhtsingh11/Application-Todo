import funtions
import FreeSimpleGUI


label = FreeSimpleGUI.Text("Type a member name")

input_box = FreeSimpleGUI.InputText(tooltip="Enter member")

button = FreeSimpleGUI.Button("Add")

window = FreeSimpleGUI.Window("My Members App", layout=[[label], [input_box, button]])
window.read()
window.close()