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