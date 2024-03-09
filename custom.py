class CustomCollection:
    def __init__(self, data):
        self.data = data
    
    def __iter__(self):
        for item in self.data:
            yield item


