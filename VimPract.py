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

    def printUserDetails(self):
        print(self.firstName, " ", self.lastName, "\n", "User Score: ", self.score)


class QuestionBank:
    def __init__(self):
        self.questions = {
            "Append to a new line under current line":"o",
            "Append to a new live above current line":"O",
            "Insert text after cursor":"a",
            "Insert text at the end of the line":"A"
            
        }

    # will convert question bank into a list then return random question 
    def getRandomQuestion(self):
        conversion = list(self.questions.items())
        random_entry = random.choice(conversion)
        return random_entry


    # Will check if second index is equal to user answer 
    def checkQuestionAnswer(self, question, userAnswer):
        if(question[1] == userAnswer):
            return True
        else:
            return False
            

    def getDictSize(self):
        return len(self.questions)







        

# Testing QuestionBank Class
"""
myTest = QuestionBank()
ques = myTest.getRandomQuestion()
print(ques[0])
ans = input("Enter your answer: ")
myTest.checkQuestionAnswer(ques, ans)
"""




