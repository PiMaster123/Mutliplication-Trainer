import random

score = 0

questions = int(input("How many multiplication questions do you want? "))
quantity = int(input("How many numbers do you want to multiply? "))

nums = []


def randomNumbers(amount):
    rNum = []

    if amount >= 7:
        upper = 5
    elif amount >= 5:
        upper = 7
    else:
        upper = 9

    for _ in range(amount):
        rNum.append(random.randint(2, upper))

    return rNum


def askQuestion(numbers):
    print(' * '.join(list(map(str, numbers))))


for i in range(questions):
    print("Question " + str(i + 1) + ":")
    nums = randomNumbers(quantity)

    correct_answer = 1
    for number in nums:
        correct_answer *= number

    askQuestion(nums)

    user_answer = int(input("What is the product? "))

    if user_answer == correct_answer:
        print("Correct!\n ")
        score += 1
    else:
        print(f"Wrong. The correct answer is {correct_answer}. \n ")

print(f'Your final score is {score}/{questions}!')
