import PySimpleGUI as sg


layout = [
    [sg.Text("Harga:"), sg.Input(key="-HARGA-", size=(20, 1))],
    [sg.Text("Kuantitas:"), sg.Input(key="-KUANTITAS-", size=(20, 1))],
    [sg.Button("Hitung Total")],
    [sg.Text("Total: ", size=(10, 1)), sg.Text("Rp.0.00", key="-TOTAL-")],
]


window = sg.Window("Kalkulator Total Harga", layout)


while True:
    event, values = window.read()
    
    
    if event == sg.WINDOW_CLOSED:
        break

    
    if event == "Hitung Total":
        try:
         
            harga = float(values["-HARGA-"])
            kuantitas = int(values["-KUANTITAS-"])
            
        
            total = harga * kuantitas
            
         
            window["-TOTAL-"].update(f"Rp.{total:,.2f}")
        except ValueError:
            
            sg.popup_error("Masukkan angka yang valid untuk Harga dan Kuantitas!")


window.close()
