
filename = 'p3-input.txt'
#filename = 'p3-input-easy.txt'

def test():
    groups = []
    cnt = 1
    g = []
    score = 0
    with open(filename, "r") as f:
        for row in f:
            if (cnt > 3):
                cnt = 1
                groups.append(g)
                g = []
            
            g.append(row.strip())
            cnt += 1
        groups.append(g)
        print (groups)
        #quit()
        for g in groups:
            print (g)
            for i in g[0]:
                if (i in g[1]):
                    if (i in g[2]):
                        print ("In all 3!! " + i)
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
