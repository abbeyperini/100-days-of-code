class Sort():
    def __init__(self):
        self.items = []

    def bubble_sort(self):
        for j in range(len(self.items)):
            swapped = False
            for i in range(0, len(self.items)):
                if i + 1 < len(self.items):
                    first = self.items[i]
                    second = self.items[i + 1]
                    if first > second:
                        self.items[i] = second
                        self.items[i + 1] = first
                    swapped = True
            
            if swapped == False:
                break

sort = Sort()
sort.items = [1, 5, 4, 2, 8]
sort.bubble_sort()
print(sort.items)