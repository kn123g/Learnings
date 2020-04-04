''' Constructor in Inheritance '''
class SkyBird:
    def __init__(self):
        print("SkyBird")
class LandBird:
    def __init__(self):
        print("LAndBird")
class Bird(SkyBird,LandBird):
    def __init__(self):
        super().__init__()
        print("Bird")
obj = Bird()
