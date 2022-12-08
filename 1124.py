import sys
def sol(num) :
    answer = num
    my_li_cnt = 0
    sosu_cnt = 0
    while answer != 1 :
        for i in range(2,answer+1) :
            if answer % i == 0 :
                answer = answer // i
                my_li_cnt +=1
                if d[i] == True :
                    sosu_cnt +=1
                break
    if sosu_cnt == my_li_cnt and d[sosu_cnt] == True :
        return True
    else :
        return False

a,b = map(int,sys.stdin.readline().split())
d = [True for _ in range(100001)]
d[1] = False


for n in range(2,100000+1) :
    if d[n] :
        for k in range(n,100000+1) :
            if n * k > 100000 :
                break
            d[n*k] = False
    if n * (n+1) > 100000 : 
        break



answer_cnt = 0
for i in range(a,b+1) : 
    if i != 1 :
        if d[i] == False:
            if sol(i) :
                answer_cnt +=1


print(answer_cnt)