# class queue:
#     def __init__(self):
#             self.items = []
#     # isEmpty memeriksa apakah antrian kosong atau tidak untuk mencegah error saat menghapus data dari antrian kosong
#     def isEmpty(self):
#         return len(self.items) == 0
#     # Enqueue (append): menambahkan elemen ke bagian belakang antrian
#     def enqueue(self, item):
#         self.items.append(item)
#         print("Data", item, "telah ditambahkan ke dalam antrian.")
#     # Dequeue (pop): menghapus dan mengembalikan elemen dari bagian depan antrian
#     def dequeue(self):
#         if not self.isEmpty():
#             removed_item = self.items.pop(0)
#             print("Data", removed_item, "telah dihapus dari antrian.")
#             return removed_item
#         return "Queue kosong tidak ada data yang dapat dihapus."
#     # peek: Melihat elemen pertama antriian tanpa menghapusnya
#     def peek(self):
#         if not self.isEmpty():
#             return self.items[0]
#         return "Queue kosong tidak ada data yang dapat ditampilkan."
#     # size: Mengembalikan jumlah elemen dalam antrian
#     def size(self):
#         return len(self.items)



# q = queue()
# q.enqueue("Data 1")
# q.enqueue("Data 2")
# q.enqueue("Data 3")

# print("Data pada Queue:", q.items)
# print("elemen pertama pada Queue:", q.peek())
# print("Jumlah elemen pada Queue:", q.size())
# print("Menghapus elemen dari Queue:", q.dequeue())
# print("Data pada Queue setelah penghapusan:", q.items)
# print("Jumlah elemen pada Queue setelah penghapusan:", q.size())

# Queue menggunakan collections.deque
from collections import deque

antrean = deque()
antrean.append("Pasien A")
antrean.append("Pasien B")
antrean.append("Pasien C")

print("Antrean sebelum deque: ", antrean)

# Dequeue (menghapus elemen dari depan antrean)
print("sedang dilayani: ", antrean.popleft())
print("Antrean setelah deque: ", antrean)

import queue

pq = queue.PriorityQueue()
# menambahkan elemen ke dalam antrean prioritas
pq.put((2, "Tugas 2"))
pq.put((1, "Tugas 1"))
pq.put((3, "Tugas 3"))

# mengambil elemen dari antrean prioritas
tugas_teratas = pq.get()
print("Tugas dengan prioritas tertinggi:", tugas_teratas[1])
