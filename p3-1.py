
filename = 'p3-input.txt'
#filename = 'p3-input-easy.txt'

def test():
    rucksacks = []
    with open(filename, "r") as f:
        for row in f:
            c1 = []
            c2 = []
            cSize = len(row.strip())/2
            cnt = 0
            for i in row.strip():
                if cnt < cSize:
                    c1.append(i)
                else:
                    c2.append(i)
                cnt += 1
            rucksacks.append([c1,c2])
    
    score = 0
    #[abcdefghijklmnopqrst
    for r in rucksacks:
        print (r[0])
        print (r[1])
        for i in r[0]:
            if (i in r[1]):
                print (i)
                print (ord(i))
                a = ord(i)
                s = 0
                if a> 96:
                    s = a - 96
                else:
                    s = a - 65 + 27
                print (s)
                score += s
                break
            

        print ("final score: " + str(score))
    
if __name__ == "__main__":
    test()
