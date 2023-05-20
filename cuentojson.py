import requests
import PySimpleGUI as sg

def count_records(url):
    # Realizar la solicitud GET
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Cargar la respuesta en formato JSON
        data = response.json()

        # Contar la cantidad de registros
        num_registros = len(data)

        # Mostrar el resultado en un pop-up
        sg.popup(f"La cantidad de registros es: {num_registros}")
    else:
        sg.popup_error("Error en la solicitud, El codigo de error es:",response.status_code)

def main():
    # Diseño de la ventana
    layout = [
        [sg.Text("Ingrese la URL del servicio GET: "), sg.InputText(key="-URL-")],
        [sg.Button("Contar Registros"), sg.Button("Salir")]
    ]

    # Crear la ventana
    window = sg.Window("Contador de Registros de un Json", layout)

    # Bucle de eventos
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Salir":
            break

        if event == "Contar Registros":
            url = values["-URL-"]
            count_records(url)

    # Cerrar la ventana
    window.close()

if __name__ == "__main__":
    main()
