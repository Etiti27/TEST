from ast import While


number_of_trial=0
secret_number=7
count_limit=3
while number_of_trial<count_limit:
    guess= int(input('guess the secret number'))
    number_of_trial+=1
    if guess==secret_number:
        print('you won!')
        break