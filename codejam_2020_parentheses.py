def function(entrada,t):
    letters = len(entrada)
    entrada = entrada + '0'
    number = list(map(int, entrada))
    number.append(-1)
    word = ''
    count = 0
    #for first parentheses
    while count < number[0]:
        word = word + '('
        count += 1
    count = 0
    word = word + entrada[0]
    for i in range(letters):
        if number[i+1] > number[i]:
            re = number[i+1] - number[i]
            while count < re:
                word = word + '('
                count += 1
            word = word + entrada[i+1]
            count = 0
            continue
        elif number[i+1] < number[i]:
            re = number[i] - number[i+1]
            while count < re:
                word = word + ')'
                count += 1
            word = word + entrada[i+1]
            count = 0
            continue
        elif number[i+1] == number[i]:
            word = word + entrada[i+1]
    print("Case #{}: {}".format(t,word[0:-1]))



T=int(input().strip())
for _ in range(T):
    s=input()
    function(s,_+1)
