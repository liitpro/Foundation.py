class Foundation:
    def __init__(self, length, width, depth):
        self.length = length
        self.width = width
        self.depth = depth
    
    def calculate_concrete_volume(self):
        volume = self.length * self.width * self.depth
        return volume
    
foundation1 = Foundation(10, 5, 2)
foundation2 = Foundation(8, 6, 1.5)

print(f"The volume of concrete needed for Foundation 1 is {foundation1.calculate_concrete_volume()} cubic meters.")
print(f"The volume of concrete needed for Foundation 2 is {foundation2.calculate_concrete_volume()} cubic meters.")
