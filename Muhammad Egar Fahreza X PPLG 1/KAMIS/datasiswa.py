import PySimpleGUI as sg

layout = [
    [sg.Text("DATA SISWA BARU", font=("Helvetica", 20), justification="center", size=(30, 1), background_color="#ADEAEA")],
    [sg.Text("Nama Lengkap", size=(20, 1)), sg.Input(key="-NAMA-", size=(30, 1))],
    [sg.Text("Tanggal Lahir", size=(20, 1)), sg.Input(key="-TANGGAL_LAHIR-", size=(30, 1))],
    [sg.Text("Asal Sekolah", size=(20, 1)), sg.Input(key="-ASAL_SEKOLAH-", size=(30, 1))],
    [sg.Text("NISN", size=(20, 1)), sg.Input(key="-NISN-", size=(30, 1))],
    [sg.Text("Nama Ayah", size=(20, 1)), sg.Input(key="-NAMA_AYAH-", size=(30, 1))],
    [sg.Text("Nama Ibu", size=(20, 1)), sg.Input(key="-NAMA_IBU-", size=(30, 1))],
    [sg.Text("Nomor Telepon / HP", size=(20, 1)), sg.Input(key="-NO_HP-", size=(30, 1))],
    [sg.Text("Alamat", size=(20, 1)), sg.Multiline(key="-ALAMAT-", size=(30, 3))],
    [sg.Button("Hapus", button_color=("white", "#FF5733")), sg.Button("Simpan", button_color=("white", "#4CAF50"))],
]

window = sg.Window("Form Data Siswa Baru", layout, background_color="#ADEAEA")

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break


    if event == "Hapus":
        # Menghapus semua input
        for key in values:
            window[key].update("")

    # Jika tombol "Simpan" ditekan
    if event == "Simpan":
        # Validasi data
        if all(values[key] for key in values):
            # Simpan data ke file atau tampilkan popup
            sg.popup("Data berhasil disimpan!", title="Informasi")
        else:
            sg.popup_error("Harap isi semua data!", title="Error")

# Menutup window
window.close()
