class CustomData:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        if not isinstance(other, CustomData):
            return NotImplemented
        return self.value == other.value
    
    def __bool__(self):
        return bool(self.value)
