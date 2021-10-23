'https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/counting-frog-paths-1abd84d5/'

'''
There is a frog initially placed at the origin of the coordinate plane. In exactly  second, the frog can either move up  unit, move right  unit, or stay still. 
In other words, from position , the frog can spend  second to move to:

After  seconds, a villager who sees the frog reports that the frog lies on or inside a square of side-length  with coordinates , , , . 
Calculate how many points with integer coordinates on or inside this square could be the frog's position after exactly  seconds

'''



count = 0 #initilizing the cout woth 0

X,Y,s,T = map(int,input().split()) #taking single lined space input

for i in range(X,X+s+1): #first border
    for j in range(Y,Y+s+1): #second border

        if(i+j<=T): #if the frog is within the borders

            count+= 1 #increase the count

print(count) #printing the final count