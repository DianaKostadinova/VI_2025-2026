class Grad:
    def __init__(self,ime,temperatura,dozhd):
        self.ime = ime
        self.temperatura = temperatura
        self.dozhd = dozhd

    def print(self):
        return {self.ime,self.temperatura,self.dozhd}


data=""
hashmap={}
dozdlivi={}
niza=[]
while(data!="end"):
    data=input()
    if(data!="end"):
        data=data.split(" ")
        g=Grad(data[0],float(data[1]),data[2])

        if(hashmap.get(g.ime)):
            hashmap[g.ime]=hashmap[g.ime]+1
            for i in niza:
                if(g.ime==i.ime):
                    i.temperatura+=g.temperatura
        else:
          hashmap[g.ime]=1
          niza.append(g)
        if(g.dozhd=="yes"):
            if(dozdlivi.get(g.ime)):
             dozdlivi[g.ime]=dozdlivi[g.ime]+1;
            else:
                dozdlivi[g.ime]=1
        elif(dozdlivi.get(g.ime)==None):
            dozdlivi[g.ime]=0;
for i in niza:
    i.temperatura=float(i.temperatura)/hashmap[i.ime]
sorted_city = sorted(niza, key=lambda x: (-dozdlivi[x.ime], x.ime))
for i in sorted_city:
    print(i.ime,round(i.temperatura,2),dozdlivi.get(i.ime))

