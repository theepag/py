class Face:
    def __init__(self, eye_color, hair_color, skin_tone, facial_expression):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.skin_tone = skin_tone
        self.facial_expression = facial_expression

    def describe(self):
        print(f"Face Description:\n"
              f"Eye Color: {self.eye_color}\n"
              f"Hair Color: {self.hair_color}\n"
              f"Skin Tone: {self.skin_tone}\n"
              f"Facial Expression: {self.facial_expression}")

# Example usage
my_face = Face(eye_color="brown", hair_color="black", skin_tone="fair", facial_expression="smiling")
my_face.describe()








