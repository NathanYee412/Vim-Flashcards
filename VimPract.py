import random


print("Hello World! This is Vim practice")

# Jump to the beginning of a word w
# Jump to the beginning of each string W 

# Append after cursur a
# Append after whole line A 

# Append to a new line under current line o
# Append to a new line above current line O

class User:
    def __init__(self, fName, lName):
        self.firstName = fName
        self.lastName = lName
        self.score = 0

    def incrementScore(self):
        self.score += 1
    
    def getScore(self):
        return self.score


class QuestionBank:
    def __init__(self):
        self.questions = {
            "Append to a new line under current line":"o",
            "Append to a new live above current line":"O",
            "Insert text after cursor":"a",
            "Insert text at the end of the line":"A"
            
        }

    def getRandomQuestion(self):
        var = []
        random.choice(list(self.questions.items()))


    def checkQuestionAnswer(self, question, userAnswer):
        for key, value in question.items():
            if(question[key] == userAnswer or value == userAnswer):
                return True
            else:
                return False
        

# Testing QuestionBank Class

test = QuestionBank()

randQ = test.getRandomQuestion()

if(test.checkQuestionAnswer(randQ, "o")):
    print("correct answer")
else:
    print("wrong answer")

# print(res)
