import multiprocessing
import time
import os

def enkripsi_pesan(pesan, shift):
    print(f"[TASK 1] Enkripsi berjalan pada PID: {os.getpid()}")
    hasil = ""
    for char in pesan:
        hasil += chr((ord(char) + shift))
    time.sleep(1.5)  
    print(f"[HASIL 1] Pesan Terenkripsi: {hasil}")

def filter_data_sensor(data_list):
    print(f"[TASK 2] Filtering berjalan pada PID: {os.getpid()}")
    filtered = [x for x in data_list if x > 10]
    time.sleep(2)  
    print(f"[HASIL 2] Data Sensor Setelah Filter: {filtered}")

if __name__ == "__main__":
    print(f"--- MEMULAI KUIS PARALLEL COMPUTING - NRP 152024133 --- ")
    
    pesan_rahasia = "PARALLEL_ITENAS"
    data_suhu = [5, 12, 8, 25, 30, 7, 40]

    proses_A = multiprocessing.Process(target=enkripsi_pesan, args=(pesan_rahasia, 3))
    proses_B = multiprocessing.Process(target=filter_data_sensor, args=(data_suhu,))

    proses_A.start()
    proses_B.start()

    proses_A.join()
    proses_B.join()

    print("--- SEMUA TUGAS BERBEDA SELESAI DIEKSEKUSI ---")