## Program Konversi Suhu (Celsius ke Fahrenheit)

def celsius_to_fahrenheit(celsius):
    """
    Mengonversi suhu dari Celsius ke Fahrenheit.
    Rumus: F = (C * 9/5) + 32
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """
    Mengonversi suhu dari Fahrenheit ke Celsius.
    Rumus: C = (F - 32) * 5/9
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Bagian utama program untuk input dan output
print("--- Konversi Suhu ---")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")

# Meminta pengguna memilih jenis konversi
pilihan = input("Masukkan pilihan (1 atau 2): ")

if pilihan == '1':
    # Konversi C ke F
    try:
        celsius_input = float(input("Masukkan suhu dalam Celsius (°C): "))
        hasil_fahrenheit = celsius_to_fahrenheit(celsius_input)
        print(f"Hasil konversi: {celsius_input}°C sama dengan {hasil_fahrenheit:.2f}°F")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

elif pilihan == '2':
    # Konversi F ke C
    try:
        fahrenheit_input = float(input("Masukkan suhu dalam Fahrenheit (°F): "))
        hasil_celsius = fahrenheit_to_celsius(fahrenheit_input)
        print(f"Hasil konversi: {fahrenheit_input}°F sama dengan {hasil_celsius:.2f}°C")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

else:
    print("Pilihan tidak valid.")