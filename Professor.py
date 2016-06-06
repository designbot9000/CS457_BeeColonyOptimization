class Professor:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __str__(self):
        return self.name

    def get_rating(self):
        return self.rating

Montgomery = Professor("Montgomery", 4.5)
Andonie = Professor("Andonie", 2.5)
Kovalerchuk = Professor("Kovalerchuk", 2.6)
Davendra = Professor("Davendra", 4)
Vajda = Professor("Vajda", 3.3)
HarperL = Professor("HarperL", 3.1)
HarperJ = Professor("HarperJ", 3.8)
Guerinoni = Professor("Guerinoni", 3.9)
Abdulwahid = Professor("Abdul-Wahid", 3.1)
Harrison = Professor("Harrison", 4.5)
Lulofs = Professor("Lulofs", 2.3)
Salter = Professor("Salter", 2.3)
Schwing = Professor("Schwing", 3.8)
Popescu = Professor("Popescu", 1.5)
Grecos = Professor("Grecos", 3)
Zeljkovic = Professor("Zaljkovic", 3)
Jagodzinski = Professor("Jagodzinski", 4.9)
Johnson = Professor("Johnson", 3.8)
Anvik = Professor("Anvik", 2.7)
unknown = Professor("Unknown", 3)
