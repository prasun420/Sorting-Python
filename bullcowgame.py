import random as rand
import emoji as emo

emo_cow = emo.emojize(emo.demojize('🐄'))
emo_bull = emo.emojize(emo.demojize('🐂'))
print('\n\033[1m' + ' --: Welcome to Cows (', emo_cow, ') and Bulls (', emo_bull, ') game :--' + '\033[0m')

rand_num = rand.randrange(1000, 9999, 1)
rand_num_list = list(str(rand_num).replace("", ""))

trial = 0
error_dig = 0
error_let = 0

while True:
    user_num = input('Guess the 4 digit number : ')
    user_num_list = list(str(user_num).replace("", ""))

    def if_contain_letter(x):
        for ele in x:
            if ele.isalpha():
                con = True
            else:
                con = False
        return con

    if len(user_num_list) != 4:
        print(' DIGIT no. Error : \n Your entered number does not contain 4 digits')
        error_dig += 1
        if error_dig > 3:
            print('*) WARNING !! What are you doing ? Too much errors ! Be careful !')

    if if_contain_letter(user_num_list):
        print('DIGIT type Error :\n inputted number contains letter ')
        error_let += 1

    if not if_contain_letter(user_num_list):
        if len(user_num_list) == 4:
            a = []
            b = []

            for i in range(len(user_num_list)):
                if rand_num_list[i] == user_num_list[i]:
                    a.append(user_num_list[i])

                if rand_num_list[i] != user_num_list[i]:
                    if user_num_list[i] in rand_num_list:
                        b.append(user_num_list[i])

            num_of_cow = len(a)
            num_of_bull = len(b)
            print(num_of_cow, ' cow (', emo_cow, ')')
            print(num_of_bull, ' bull (', emo_bull, ')')
            trial += 1

    if str(user_num) == str(rand_num):
        print('\n\033[1m' + '### Congratulations! , Well played ###' + '\033[0m')
        print('Trials = ', trial)
        print('Errors = ', error_dig + error_let)
        break
