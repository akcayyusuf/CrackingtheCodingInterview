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
    def finalize():
        for n in range(len(coef)):
            final.append(str1[sum(coef[0:n+1])-1])
            final.append(str(coef[n]))
        print(''.join(final))
    i=0
    coef = []
    final=[]
    while i<len(str1)-1:
        coef.append(1)
        while str1[i]==str1[i+1]:
            coef[-1]=coef[-1]+1
            i=i+1
            if i ==len(str1)-1:
                finalize()
                return
        i=i+1
    if str1[i - 1] != str1[i] and i == len(str1)-1 :
        coef.append(1)

    finalize()




#compString(input())




