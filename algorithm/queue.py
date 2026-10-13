class queue:
    def __init__(self):
            self.items = []
    # isEmpty memeriksa apakah antrian kosong atau tidak untuk mencegah error saat menghapus data dari antrian kosong
    def isEmpty(self):
        return len(self.items) == 0
    # Enqueue (append): menambahkan elemen ke bagian belakang antrian
    def enqueue(self, item):
        self.items.append(item)
        print("Data", item, "telah ditambahkan ke dalam antrian.")
    # Dequeue (pop): menghapus dan mengembalikan elemen dari bagian depan antrian
    def dequeue(self):
        if not self.isEmpty():
            removed_item = self.items.pop(0)
            print("Data", removed_item, "telah dihapus dari antrian.")
            return removed_item
        return "Queue kosong tidak ada data yang dapat dihapus."
    # peek: Melihat elemen pertama antriian tanpa menghapusnya
    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        return "Queue kosong tidak ada data yang dapat ditampilkan."
    # size: Mengembalikan jumlah elemen dalam antrian
    def size(self):
        return len(self.items)



q = queue()
q.enqueue("Data 1")
q.enqueue("Data 2")
q.enqueue("Data 3")

print("Data pada Queue:", q.items)
print("elemen pertama pada Queue:", q.peek())
print("Jumlah elemen pada Queue:", q.size())
print("Menghapus elemen dari Queue:", q.dequeue())
print("Data pada Queue setelah penghapusan:", q.items)
print("Jumlah elemen pada Queue setelah penghapusan:", q.size())

