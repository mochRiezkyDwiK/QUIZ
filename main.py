import threading
import math
import time
import random

# Inisialisasi sesuai variabel di Slide
W = 100            # Total Work (Slide 181)
p = 4              # Number of Processors (Slide 181)
min_chunk = 1      # Minimum Chunk Size
remaining_work = W
lock = threading.Lock()

def worker(processor_id):
    global remaining_work
    tasks_done = 0
    
    while True:
        with lock:
            if remaining_work <= 0:
                break
            
            # Rumus Guided Scheduling dari Slide 21
            # Chunk = max(Remaining Work / p, Min Chunk)
            chunk_size = max(math.ceil(remaining_work / p), min_chunk)
            remaining_work -= chunk_size
            current_batch = chunk_size
            
        # Simulasi pengerjaan tugas
        tasks_done += current_batch
        print(f"[Processor P{processor_id}] Mengambil {current_batch} tugas. Sisa antrean: {remaining_work}")
        
        # Simulasi durasi pengerjaan (beban kerja bervariasi)
        time.sleep(random.uniform(0.1, 0.3)) 

    print(f"--- P{processor_id} Selesai. Total dikerjakan: {tasks_done} tugas ---")

# Menjalankan p threads (Processor)
threads = []
print(f"Memulai Load Balancing dengan {p} Processor untuk {W} Tugas...\n")

for i in range(p):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nSukses: Semua tugas terdistribusi merata (Balanced Completion)!")