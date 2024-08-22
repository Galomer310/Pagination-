class Pagination:
    def __init__(self, items, pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.currentPage = 1

    def getVisibleItems(self):
        start_index = (self.currentPage - 1) * self.pageSize
        end_index = min(start_index + self.pageSize, len(self.items))
        return self.items[start_index:end_index]

    def prevPage(self):
        if self.currentPage * self.pageSize < len(self.items):
            self.currentPage -= 1
        return self.getVisibleItems()

    def nextPage(self):
        if self.currentPage * self.pageSize < len(self.items):
            self.currentPage += 1
            return self.getVisibleItems()

    def firstPage(self):
        start_index = 0
        end_index = min(start_index + self.pageSize, len(self.items))
        return self.items[start_index:end_index]

    def lastPage(self):
        self.currentPage = (len(self.items) - 1) // self.pageSize + 1
        return self.getVisibleItems()

    def goToPage(self, pageNum):
        start_index = (pageNum - 1) * self.pageSize
        end_index = min(start_index + self.pageSize, len(self.items))
        return self.items[start_index:end_index]

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
print(p.getVisibleItems())
print(p.nextPage())
print(p.nextPage())
print(p.prevPage())
print((p.firstPage()))
print(p.lastPage())
print(p.goToPage(6))