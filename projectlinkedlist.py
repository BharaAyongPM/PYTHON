class node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self, newdata):
        self.data = newdata

    def setnext(self, newnext):
        self.next = newnext


class orderedlist:
    def __init__(self):
        self.head = None

    def show(self):
        current = self.head
        print("Head -> ", end="")
        while current != None:
            print(current.getdata(), end="-> ")
            current = current.getnext()
        print("None")

    def isempty(self):
        return self.head == None

    def add(self, item):
        temp = node(item)
        temp.setnext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getnext()
        return count

    def search(self):
        current = self.head
        s = int(input("masukkan data yang akan dicari : "))
        found = False
        while current != None and not found:
            if current.getdata() == s:
                found = True
            else:
                current = current.getnext()
        if found == True:
            print("Data ditemukan")
        else:
            print("Data tidak ditemukan")

    def remove(self):
        current = self.head
        s = int(input("masukkan data yang akan dihapus : "))
        previous = None
        found = False
        while not found and current != None:
            if current.getdata() == s:
                found = True
            else:
                previous = current
                current = current.getnext()
        if found == True:
            if previous == None:
                self.head = current.getnext()
            else:
                previous.setnext(current.getnext())
            print("Data sudah dihapus")
        else:
            print("Data yang akan dihapus tidak ditemukan")

    def ganjil(self, item):
        for i in range(len(item)):
            if item[i] % 2 == 1:
                ganjil.append(item[i])
        ol.sort(ganjil)
        print(ganjil)

    def genap(self, item):
        for i in range(len(item)):
            if item[i] % 2 == 0:
                genap.append(item[i])
        ol.sort(genap)
        print(genap)

    def sort(self, item):
        for x in range(len(item) - 1, 0, -1):
            for y in range(x):
                if item[y] > item[y + 1]:
                    item[y], item[y + 1] = item[y + 1], item[y]

    def tambah(self, item):
        pil = "y"
        while pil == "y":
            tam = int(input("masukkan data : "))
            lis.append(tam)
            pil = str(input("apakah anda mau memasukkan data lagi ? (y/n)"))
        ol.ganjil(lis)
        ol.genap(lis)
        genap.reverse()
        merge = ganjil + genap
        for i in merge:
            ol.add(i)


ol = orderedlist()
lis = [170411100001, 170411100002, 170411100003, 170411100004, 170411100005, 170411100006]
genap = []
ganjil = []
merge = ganjil + genap
ol.tambah(ol)
ol.show()
print("panjang datanya adalah", orderedlist.size(ol))
orderedlist.search(ol)
orderedlist.remove(ol)
ol.show()