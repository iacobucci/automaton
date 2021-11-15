from math import *
from copy import copy,deepcopy

class Automaton():
    def __init__(self,bitlen,code = -1):
        self.code = 0

        if code == -1:
            for i in range(len(bitlen)):
                self.code += (0 if (bitlen[i] == "0") else 2**i)
            self.bitlen = int(log2(len(bitlen)))
        else:
            self.code = code
            self.bitlen = bitlen

        self.rule = {}

        for i in range(2**self.bitlen):
            self.rule[i] = (self.code // 2**i) % 2

        self.num = 0
        self.g = [[]]
        
    def start_grid(self,num):
        self.num = num
        self.g[0].append(1)
        for i in range(self.num-1):
            self.g[0].append(0)
    
    def update(self):
        lastrow = deepcopy(self.g[len(self.g)-1])
        lastrow = lastrow + lastrow[0:self.bitlen]

        temp = [[]]
        
        for i in range(self.num):
            n = 0
            for k in range(self.bitlen):
                n += lastrow[i+k] * (2 ** (self.bitlen - k - 1)) 
            temp[0].append(self.rule[n])
            
        # temp[0] = list(reversed(temp[0]))
        self.g += temp

    
    def save(self,name):
        with open(name,"w") as f:
            f.write("P1\n")
            f.write("%s %s\n" % (len(self.g[0]),len(self.g)))
            for i in self.g:
                for k in i:
                    f.write(str(k) + " ")
                f.write("\n")



    def __repr__(self):
        s = str(list(self.rule.values())) + "\n"
        for i in self.g:
            s+= str(i) + "\n"
        return s



def main():
    for n in range(256):
        a1 = Automaton(3,n)
        a1.start_grid(256)

        for i in range(256):
            a1.update()

        a1.save("%i.pnm" % n)

if __name__ == "__main__":
    main()
