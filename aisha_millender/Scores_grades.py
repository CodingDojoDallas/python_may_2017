

def scores_grades():
    import random
    for i in range(10):
        score = random.randint(60, 100)
        if 60 <= score <= 69:
            print "Score:", str(score) + ".", "Your grade is a D."
        elif 70 <= score <= 79:
            print "Score:", str(score) + ".", "Your grade is a C."
        elif 80 <= score <= 89:
            print "Score:", str(score) + ".", "Your grade is a B."
        else:
            print "Score:", str(score) + ".", "Your grade is a A."

    print "End of the program. Bye!"

scores_grades()