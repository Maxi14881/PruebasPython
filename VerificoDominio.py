import requests
import PySimpleGUI as sg

def verificar_dominio(dominio):
    url = f"https://go-qa.finneg.com/api/1/domains/{dominio}/info"
    response = requests.get(url)
    if response.status_code == 200:
        sg.popup("El Dominio está en F4")
    else:
        sg.popup("El Dominio está en F3")

layout = [
    [sg.Text("Ingrese el dominio: "), sg.Input(key="-DOMINIO-")],
    [sg.Button("Verificar"), sg.Button("Salir")]
]

window = sg.Window("Verificación de Dominio", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Salir":
        break
    if event == "Verificar":
        dominio = values["-DOMINIO-"].upper()
        verificar_dominio(dominio)

window.close()



