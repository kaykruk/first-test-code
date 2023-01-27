import time

user = ['Emeka', 'Norah', 'KRUK', 'Chisom']
atm_pin = [1234, 1010, 1357, 2468]
acc_balance = [30000, 15000, 40000, 6000]
trials = 3
print('Welcome to KRUK Bank')
time.sleep(1)
atm = input('Please insert your ATM card...')
pin = int(input('Please enter your 4 digit pin: '))
time.sleep(1)


while trials != 0:
    if pin in atm_pin:
        index = atm_pin.index(pin) 
        print('Welcome', user[index])
        print('1 Balance Inquiry    2 Withdrawal\n3 Airtime Recharge   4 Change Pin')
        options = str(input('select an option: '))

        if options == '1':
            print('Loading Balance Inquiry...')
            time.sleep(1)
            account_prompt = input('1 Savings\n2 Current\n3 Credit\n: ')
            print('Your Account Balance is $' + str(acc_balance[index]))
            time.sleep(1)

        if options == '2':
            print('Loading Cash Withdrawal...')
            time.sleep(1)
            withdraw = int(input('How much do you want to withdraw?: '))
            account_prompt = input('1 Savings\n2 Current\n3 Credit\n: ')
            if withdraw >= acc_balance[index]:
                print("Insufficient Funds")
            else:
                time.sleep(1)
                print('you have withdrawn $' + str(withdraw), 'from your account')
                acc_balance[index] -= withdraw
                time.sleep(1)
                print('Your Account Balance is $' + str(acc_balance[index]))
                time.sleep(1)

        if options == '3':
            print('Loading Airtime Recharge...')
            time.sleep(1)
            network = (input('Network: '))
            time.sleep(0.5)
            account_prompt = input('1 Savings\n2 Current\n3 Credit\n: ')
            time.sleep(0.5)
            amount = int(input('How much do you want to recharge?: '))
            time.sleep(0.5)
            number = int(input('Enter your phone Number: '))
            print('You have Recharged', number, 'with', amount)
            time.sleep(0.5)
            acc_balance[index] -= amount
            print('Your Account Balance is $' + str(acc_balance[index]))

        if options == '4':
            pin_change = int(input('Enter a new pin: '))
            if pin_change == str(atm_pin[index]):
                print('You cannot use an old Pin')
            else:
                print('Pin changed successfully')

    else:
        trials -= 1
        print('Wrong Pin, you have', trials, 'Trials Left!')
    finish = input('Do you want to perform another transaction? Y/N: ')
    if finish == 'Y' or finish == 'y':
        continue
    else:
        print('Thank you for banking with us')
        break
