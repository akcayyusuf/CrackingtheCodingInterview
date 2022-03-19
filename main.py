def isunique(mystr):

    for i in range(len(mystr)):
        for j in range(i+1,len(mystr)):
            if mystr[i]==mystr[j]:
                print("false")
                return

    print("true")
    return

#isunique(input())

def chkperm(str1,str2):

    str1=list(str1)
    str2=list(str2)

    print(str1)
    print(str2)
    for i in range(0,len(str1)):
        flag = False
        for j in range(0,len(str2)):
            if str1[i]==str2[j]:
                flag=True
                str2.pop(j)
                break
        if flag == False:
            print("NO MICKEY NO")
            break
    return

#chkperm(input(),input())

def oneAway(str1,str2):
    control=0
    if len(str1)<len(str2):
        str1,str2=str2,str1
    if len(str1)-len(str2)>1:
        print("NO")
        return
    elif len(str1)-len(str2)==0:
        control=0
    elif len(str1)-len(str2)==1:
        control=1

    for i in range(0,len(str2)):
        if str2[i] not in str1:
            control=control+1

    if control>1:
        print("NO")
        return
    else:
        print("YES")
        return

#oneAway(input(),input())

def compString(str1):
    str1=list(str1)
    str2=str1.copy()
    for i in range(0,len(str1)):
        coef=1
        while str1[i] ==str1[i+1]:
            coef=coef+1
            i=i+1
            str2.pop(i)
        str2.insert(i,coef)
    print(str2)


compString(input())




