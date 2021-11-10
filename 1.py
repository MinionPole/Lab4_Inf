ind = 0

def prefspace_cnt(s):
    ret = 0
    for i in range (0, len(s)):
        if(s[i] == ' '):
            ret = ret + 1
        else:
            return ret

def space_defis_str(s):
    for cnt in range (0, len(s)):
        if(not(s[cnt] == ' ' or s[cnt] == '-' or s[cnt] == '\t')):
            return False
    return True

def space_defis_symb(s):
    defi = -1
    for f in range(0, len(s)):
        if(s[f] == '-'):
            defi = f
    return defi

def print_before_two(s):
    flag = False
    for f in range(0, s.find(":")):
        if(s[f] != ' ' and flag == False):
            flag = True
            print('"', end = "")
        print(s[f], end = "")
    print('"', end = "")
            
def parser(start, ende):
    ind = start
    cnt = 0
    while(ind < ende):
        if(cnt != 0):
            print(",", end = "\n")
        if(a[ind].find(':') != -1 and a[ind].find(':') == len(a[ind]) - 1):
            print_before_two(a[ind])
            print(':', end = "")
            print('[')
            
            if(space_defis_str(a[ind + 1])):
                ar = []
                ende2 = ende
                for f in range(ind + 1, ende):
                    if(prefspace_cnt(a[f]) < prefspace_cnt(a[ind + 1])):
                        ende2 = f
                        break

                
                for f in range(ind + 1, ende2):
                    if(a[f] == a[ind + 1] and prefspace_cnt(a[f]) >= prefspace_cnt(a[ind + 1])):
                        ar.append(f)
                ar.append(ende2)



                
                for f in range(0, len(ar) - 1):
                    print('{')
                    parser(ar[f] + 1, ar[f + 1]);
                    if(f != len(ar) - 2):
                        print('},')
                    else:
                        print('}')
                ind = ende2
            else:
                cnt2 = 0
                ind2 = ind + 1
                while(ind2 < ende and space_defis_symb(a[ind2]) != -1):
                    if(cnt2 != 0):
                        print(", ", end = "")
                    for f in range(space_defis_symb(a[ind2]) + 1, len(a[ind2])):
                        print(a[ind2][f], end = "")
                    cnt2 = cnt2 + 1
                    ind2 = ind2 + 1
                ind = ind2
                

                
            print(']')
        else:
            print_before_two(a[ind])
            print(':', end = "")
            x = a[ind].find(':')
            flag = False
            for f in range(x + 1, len(a[ind])):
                if(a[ind][f] == ' '):
                    continue
                if(a[ind][f] == '"'):
                    flag = True
                    break
                else:
                    break
            if(not(flag)):
                print('"', end = "")
            for f in range(x + 1, len(a[ind])):
                print(a[ind][f], end = "")
            if(not(flag)):
                print('"', end = "")
            ind = ind + 1
                
                    
        cnt = cnt + 1


fin = open('data2.txt', encoding='utf-8')
a = fin.readlines()

for b in range(0, len(a)):
    if(a[b][len(a[b])- 1] == '\n'):
        a[b] = a[b][:len(a[b])- 1]

#for b in range(0, len(a)):
#    print(a[b])



print('{')


parser(0, len(a))


print('}')





