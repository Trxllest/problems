'''
How does it work?
1. Start with an empty or random solution. This is called our best solution
2. Make a copy of the solution and mutate it slightly
3. Evaluate the new solution. If it's better than the best solution, we replace the best solution with this one
4. Go to step two and repeat
So basically to evolve a solution to a problem, you need to write three functions.
1. Create a random solution
2. Evaluate a solution and return a score
3. Mutate a solution in a random way
'''
#Infinite Monkey Problem 

import random

monkey = "methinks it is like a weasel"

#generates a string of random characters of len n
def gen_string(nlen):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    phrase = ''
    for i in range(nlen):
        phrase += random.choice(alphabet)
    return phrase

def score(goal,phrase):
    similar = 0
    for i in range(len(goal)):
        if goal[i] == phrase[i]:
            similar += 1
    print(phrase)
    return similar / len(phrase)

#generates strings until score = 100%
## takes forever never reaches 100%
"""def gen_goal(goal='a',n=1):
    best_score = 0.0
    while best_score < 1:
        current_string = gen_string(n)
        current_score = score(goal,current_string)
        if current_score > best_score:
            best_score = current_score
            print(current_string)
        else:
            print(best_score)"""

#gen_goal(monkey,28)

### Keeps the best iteration
def generate():
    target = input('Type a phrase with no punctuation and only letters please! ')
    n = len(target)
    current_phrase = gen_string(n)
    best_score = score(target,current_phrase)
    attempts = 0
    while best_score<1:
        """if best_score == 0:
            current_phrase = gen_string(n)
            best_score = score(target,current_phrase)"""
        los = list(current_phrase)
        index = random.randint(0,(len(los)-1))
        los[index] = random.choice('abcdefghijklmnopqrstuvwxyz ') ## Previous issue was i forgot 'K' in alphabet
        new_phrase = ''.join(map(str, los))
        new_phrase_score = score(target,new_phrase)
        if new_phrase_score > best_score:
            current_phrase = new_phrase
            best_score = new_phrase_score
        if best_score == 1:
            print('You did it ' + current_phrase + f'...on attempt:{attempts}')
            break
        else:
            print(f'trying again current score is {best_score} attempt:{attempts}')
            attempts += 1
            
#stuck at 92.86% ## Finally Fixed it
generate()



    