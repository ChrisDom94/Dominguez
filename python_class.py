class Golf:
    'Golf scoring class'
    results = " "

    def __init__(self, hole, score, par):
        self.hole = hole
        self.par = par
    def evaluateAndDisplayScore(self, hole, score):
        if (score > self.par):
            Golf.results = "Over Par"
        elif (score < self.par):
            Golf.results = "Under Par"
        else:
            Golf.results = "At Par"
        print("You scored", Golf.results, "on hole #", hole, "with a par of", self.par)

score = 0

hole1=Golf(1, score, 3)
hole2=Golf(2, score, 4)
hole3=Golf(3, score, 5)

enterHole = int(input("Enter the hole number: "))
score = int(input("Enter your score: "))

if enterHole == 1:
    hole1.evaluateAndDisplayScore(enterHole, score)
if enterHole == 2:
    hole2.evaluateAndDisplayScore(enterHole, score)
if enterHole == 3:
    hole3.evaluateAndDisplayScore(enterHole, score)
