numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    is_primes = True
    for j in range(2,i):
        if i % j == 0:
            is_primes = False
            break
    if is_primes:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)

# import random
# def lottery(mon, tue):
#     tickets = [1,2,3,4,5,6,7,8,9,10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     print (mon,tue)
#     return win1, win2
#
#
# win1, win2 = lottery ('mon', 'tue')
# print(win1, win2)


