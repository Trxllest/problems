import random

monkey = "methinks it is like a weasel"

#generates a string of random characters of len n
def gen_string(nlen):
    alphabet = 'abcdefghijclmnopqrstuvwxyz '
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
def generate(goal,n):
    target = goal
    current_phrase = gen_string(n)
    best_score = score(target,current_phrase)
    while best_score<1:
        if best_score == 0:
            break
        los = list(current_phrase)
        index = random.randint(0,(len(los)-1))
        los[index] = random.choice('abcdefghijclmnopqrstuvwxyz ')
        new_phrase = ''.join(map(str, los))
        new_phrase_score = score(target,new_phrase)
        if new_phrase_score > best_score:
            current_phrase = new_phrase
            best_score = new_phrase_score
        if best_score == 1:
            print('You did it ' + current_phrase)
            break
        else:
            print(f'trying again current score is {best_score}')
            
#stuck at 92.86%
generate(monkey,28)






    