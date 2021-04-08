from VimPract import *


def main():
    fname, lname = input("Enter Your first then last name: ").split()
    print(fname, " ", lname)

    # create user object
    user = User(fname, lname)

    # create QuestionBank object
    qs = QuestionBank()


    for x in range(qs.getDictSize()):
        randQ = qs.getRandomQuestion()
        ans = input(randQ[0])
        res = qs.checkQuestionAnswer(randQ,ans)
        if(res):
            user.incrementScore()

    user.printUserDetails()


if __name__ == "__main__":
    main()