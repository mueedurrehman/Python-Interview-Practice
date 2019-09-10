def jumpingOnClouds(c):
    min_jumps = 0
    current_position = 0
    length = len(c)
    while current_position < length - 1:
        print(current_position)
        if current_position + 2 == length or c[current_position + 2] == 1 :
            current_position += 1
            min_jumps += 1
        else:
            current_position +=2
            min_jumps += 1
    return min_jumps

# print(jumpingOnClouds([0,0,1,0,0,1,0]))

# l1 = []
# l1[3] = 5
#
# print(l1)

def droppedRequests(requestTime):
    if requestTime == []:
        return 0
    times = [0] * max(requestTime)
    # Get all times at an index
    dropped = 0
    for index, element in enumerate(requestTime):
        times[element - 1] += 1
    # Checking 1s drop
    for i in range(len(times)):
        in_one = times[i]
        if in_one > 3:
            dropped += in_one - 3
    start = 0
    end = 0
    cur_sum = 0
    window_size = 10
    temp = times.copy()
    while end < len(temp):
        nxt = temp[end]
        cur_sum += nxt
        window_end = end - start + 1 == window_size or end == len(times) - 1
        if cur_sum > 20 and not window_end:
            cur_drop = cur_sum - 20
            cur_sum = 20
            temp[end] = temp[end] - cur_drop
            dropped += cur_drop
        elif window_end:
            if cur_sum > 20:
                cur_drop = cur_sum - 20
                dropped += cur_sum - 20
                cur_sum = 20
                temp[end] = temp[end] - cur_drop
            remove = temp[start]
            cur_sum -= remove
            start += 1
        end += 1
    start = 0
    end = 0
    cur_sum = 0
    window_size = 60
    temp = times.copy()
    while end < len(temp):
        nxt = temp[end]
        cur_sum += nxt
        window_end = end - start + 1 == window_size or end == len(times) - 1
        if cur_sum > 60 and not window_end:
            cur_drop = cur_sum - 60
            cur_sum = 60
            temp[end] = temp[end] - cur_drop
            dropped += cur_drop
        elif window_end:
            if cur_sum > 60:
                cur_drop = cur_sum - 60
                dropped += cur_sum - 60
                cur_sum = 60
                temp[end] = temp[end] - cur_drop
            remove = temp[start]
            cur_sum -= remove
            start += 1
        end += 1
    return dropped

#Should have answer 67
l2 = [1,1,1,1,2,2,2,3,3,3,3,4,5,5,5,6,6,6,6,7,7,7,8,8,8,8,9,9,9,9,9,10,10,11,11,11,11,11,11,12,12,12,12,12,12,12,13,13,13,13,14,14,14,14,14,16,16,16,16,16,16,17,17,17,18,18,18,18,18,18,18,18,19,19,19,19,19,19,19,20,20,20,20,20]
l1  = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7]
# print(droppedRequests(l2))
# print(droppedRequests([1,1,1,1,2,2,2,3,3,3,4,4,4,11,11,11,6,6,6,5,5,5]))

#Broadway Technology HackerRank
def smallestString(weight):
    multiplier = 3
    weights = [1] * 26
    alphabet = []
    for letter in range(65, 91):
        alphabet.append(chr(letter))
    #populated the weights
    for i in range(1, len(weights)):
        weights[i] = multiplier * weights[i - 1]
        multiplier += 1
    remainingWeight = weight
    string = ""
    start = 25
    while remainingWeight > 0:
        for i in range(start, -1, - 1):
            if remainingWeight / weights[i] >= 1:
                divisor = weights[i]
                quotient = remainingWeight // divisor
                string = string + (quotient * alphabet[i])
                remainingWeight = remainingWeight % divisor
                start = i - 1
                break
    return string[::-1]


# print(range(0,26,-1))

def smallestString2(weight):
    #The weights are essentially a multiple of the previous weights so I use a multiplier variable for quick calculations
    multiplier = 3
    weights = [1] #A has a weight of 1
    alphabets = []
    for letter in range(65, 91): #creating a list of alphabets for indexing later on
        alphabets.append(chr(letter))
    #populated the weights
    for i in range(1, 26): #populating the weights. Each weight is the previous weight times the multiplier
        weights.append(multiplier * weights[i - 1])
        multiplier += 1 #incrementing the multiplier so the next weight can be calculated
    string = "" #empty string to store the results of the greedy algorithm
    start = 25 #start from the highest weight and move downward till you find a weight[i] <= weight that is input
    for i in range(start, -1, - 1):
        if weight == 0: #if the weight has fallen to 0, break
            break
        elif weight / weights[i] >= 1: #if you have a weight that is <= your input weight
            divisor = weights[i] #store the divisor
            quotient = weight // divisor #calculate the quotient by integer division
            string = string + (quotient * alphabets[i]) #add the alphabet at that index a total of quotient times to the string being built
            weight = weight % divisor #the remainder of weight / divisor is the remaining weight
    return string[::-1] #reverse the string to get the lexicographically smallest and return it

# print(smallestString2(25))
#Akuna Data Infrastructure Developer HackerRank
class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

D = node("D")
G = node("G")
H = node("H")
E = node("E")
E.left = G
E.right = H
B = node("B")
B.left = D
B.right = E
I = node("I")
F = node("F")
F.left = I
C = node("C")
C.right = F
A = node("A")
A.left = B
A.right = C

def f(node):
    if node is None:
        return
    f(node.left)
    f(node.right)
    print(node.val)

# f(A)

def check_power_two(val):
    print("1")
    print(val | (val + 1) == val)
    print("2")
    print(val & (val + 1) == val)
    print("3")
    print(val & (val - 1) == 0)
    print("4")
    print(val | (val - 1) == 0)
    # print("5")
    # print(val >> 1 == val/2)
    # print("6")
    # print(((val >> 1) << 1) == val)

check_power_two(31)

# string = "0000016c052dcf41"
# print(int(string,16))
# print(len("0000016c052dcf410"))

#Got a list in hex, main function converted to a byte array. You had to parse the array and rebuild the DML Events
def convert_wal(s):
    results = []
    start = 0
    not_end = True
    #Note, I had to convert to hex to get it to work as the input really was a byte array.
    while (not_end):
        result = ""
        epoch_end = start + 16
        epoch = s[start: epoch_end]
        epoch = str(int(epoch, 16))
        result = result + epoch
        mid_start = epoch_end
        mid_end = epoch_end + 2
        mid = s[mid_start:mid_end]
        message = "INSERT"
        if mid == "01":
            message = "UPSERT"
        elif mid == "02":
            message = "DELETE"
        result = result + "|" + message
        key_length_start = mid_end
        key_length_end = mid_end + 4
        key_length = s[key_length_start:key_length_end]
        key_length = int(key_length,16)
        key_string_start = key_length_end
        key_string_end = key_string_start + (key_length * 2)
        key_string_ascii = s[key_string_start: key_string_end]
        key = ""
        for i in range(0,len(key_string_ascii),2):
            encoded = key_string_ascii[i:i+2]
            code = int(encoded, 16)
            char = chr(code)
            key = key + char
        result = result + "|" + key
        if message != "DELETE":
            value_length_start = key_string_end
            value_length_end = value_length_start + 4
            value_length = s[value_length_start:value_length_end]
            value_length = int(value_length, 16)
            value_string_start = value_length_end
            value_string_end = value_string_start + (value_length * 2)
            value_string_ascii = s[value_string_start: value_string_end]
            value = ""
            for i in range(0, len(value_string_ascii), 2):
                encoded = value_string_ascii[i:i + 2]
                code = int(encoded, 16)
                char = chr(code)
                value = value + char
            result = result + "|" + value
            start = value_string_end
        else:
            start = key_string_end
        results.append(result)
        if start == len(s):
            not_end = False
    # print(results)
    a = 1

# print(len("0000016c052dcf4102000f746573745f6b65795f313233383937"))
# convert_wal("0000016c052dcf4100000e746573745f6b65795f30393831320010746573745f76616c75655f31323837360000016c052dcf4102000f746573745f6b65795f313233383937")
# print(bytes.fromhex('deadbeef'))

# print(sorted(set([1,2,9,1,2,3,1,4,1,5,7])))