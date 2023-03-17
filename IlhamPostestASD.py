class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.get_next()

        return count

    def search(self, data):
        current = self.head
        found = False

        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()

        return found

    def delete(self, data):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def show_data(self):
        current_node = self.head
        print("Daftar yang pernah juara dunia di Indonesia : ")
        while current_node is not None:
            print(current_node.get_data())
            current_node = current_node.get_next()

    def main_menu(self):
        print("=========================================")
        print("Data yang pernah juara dunia di Indonesia")
        print("=========================================")
        print("    1.Tambahkan data yang juara dunia    ")
        print("     2. Hapus data yang juara dunia      ")
        print("      3. Cari data yang juara dunia      ")
        print("   4. Jumlah seluruh data juara dunia    ")
        print("  5. Tampilkan seluruh data juara dunia  ")
        print("                 6. Exit                 ")
        print("=========================================")
        pilihan = input("Silahkan masukkan pilihan anda: ")
        if pilihan == "1":
            obj = str(input("Masukkan data yang ingin anda tambahkan: "))
            self.insert(obj)
        elif pilihan == "2":
            obj = str(input("Masukkan data yang ingin anda hapus: "))
            self.delete(obj)
        elif pilihan == "3":
            obj = str(input("Masukkan data yang ingin anda cari: "))
            status = self.search(obj)
            if status:
                print("Data ditemukan pada list")
            else:
                print("Data tidak ditemukan")
        elif pilihan == "4":
            print("Jumlah seluruh data juara dunia adalah: " + str(self.size()))
        elif pilihan == "5":
            self.show_data()
        elif pilihan == "6":
            exit()
        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    l = LinkedList()
    while True:
        l.main_menu()
        ulang = input("Apakah anda ingin melanjutkan (y/t)? ")
        if ulang.lower() != 'y':
            break