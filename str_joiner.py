class StringJoiner:
    def __init__(self):
        self.items = []
        
    def append(self, item):
        if item is not None:
            self.items.append(str(item))
            
    def join(self, delimiter=''):
        return delimiter.join(self.items)

target_list = [1, 2, 3, None, 5, None, 7]
sj = StringJoiner()
for item in target_list:
    sj.append(item)
result = sj.join('&')
print(result)
