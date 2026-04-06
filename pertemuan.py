import threading
import queue
import time
import random

# Antrean tugas (Shared Queue) sesuai karakteristik Dynamic Load Balancing [cite: 150]
task_queue = queue.Queue()
for i in range(1, 13): # Misal ada 12 tugas
    task_queue.put(f"Tugas-{i}")

def worker(worker_id):
    while not task_queue.empty():
        try:
            # Processor "pull" work dari antrean [cite: 150]
            task = task_queue.get_block(timeout=1)
            
            # Simulasi durasi kerja yang bervariasi (irregular tasks) [cite: 160]
            duration = random.uniform(0.5, 2.0)
            print(f"[Worker {worker_id}] Mengambil {task} (Estimasi: {duration:.1f}s)")
            
            time.sleep(duration) 
            print(f"[Worker {worker_id}] SELESAI {task}.")
            
            task_queue.task_done()
        except queue.Empty:
            break

# Simulasi 3 Processor (P0, P1, P2) [cite: 155-157]
threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nSemua tugas selesai dengan distribusi dinamis yang seimbang!")