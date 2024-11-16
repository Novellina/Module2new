#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#primes = []
#not_primes = []
#or i in range(1, 11):
    #for j in range(1,11):
        #print ('{i}X{j}={i*j}')
import random
def lottery(mon, tue):
    tickets = [1,2,3,4,5,6,7,8,9,10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print (mon,tue)
    return win1, win2


win1, win2 = lottery ('mon', 'tue')
print(win1, win2)


