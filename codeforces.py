#Watermelong problem
# Conditions to check. Both of the individual ones must be greater than 2
# Therefore the sum >= 4
def watermelon():
    weight = int(input())
    if weight % 2 == 0:
        print ("YES")
    else:
        print("NO")

# watermelon()

#Insomnia Cure
#To get the total dragons, you have 4 subsets. Want to calculate the size of their union
def insomnia():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    dragons = [0] * (d + 1)
    for i in range(k, d + 1, k):
        dragons[i] = 1
    if l % k != 0:
        for i in range(l, d + 1, l):
            dragons[i] = 1
    if m % k != 0 and m % l != 0:
        for i in range(m, d + 1, m):
            dragons[i] = 1
    if n % k != 0 and n % l != 0 and n % m != 0:
        for i in range(n, d + 1, n):
            dragons[i] = 1
    print(sum(dragons))
# insomnia()

def team():
    problems = int(input())
    count = 0
    for i in range(problems):
        string = input()
        if string == "1 1 0" or string == "1 0 1" or string == "0 1 1" or string == "1 1 1":
            count += 1
    print(count)

team()
