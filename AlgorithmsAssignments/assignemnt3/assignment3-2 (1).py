import math
import numpy as np
import sys


distdelta=-1

filename = sys.argv[-1]
with open(filename, 'r') as f:
     M = [[float(num) for num in line.split(',')] for line in f]

#Random matrix generation
#M = np.random.uniform(low=1/4, high=4, size=(4,4))

#Matrix taken from input file
print("")
print("")
print("Given Input Matrix, M : " )
print(str(M))


Wbackup = [1, 1, 1, 1] 

#print("Matrix W: " + str(Wbackup)) 
dup = []
for k in M:
    for i in k:
        dup.append(i)

largest=max(dup)
smallest=min(dup)
wsize = len(Wbackup)
#print(wsize)
i = 0


def distance(M,N):
  m=0
  n=0
  distanceCalc = 0;
  for m in range(3):
    for n in range(3):
      distanceCalc += abs(M[m][n] - N[m][n])
      n += 1
    m += 1
  return distanceCalc


distanceDelta = -1
origDistanceResults = 0
aDistanceResults = 0
bDistanceResults = 0

def generateconsistentmatrix(W):
  #print("wbackup cons", str(W))
  
  i=0
  j=0
  consistentMatrix = np.zeros((len(W),len(W)))

  for i in range(len(W)):
    for j in range(len(W)):
      consistentMatrix[i][j] = W[i]/W[j]
      j+=1
    i+=1
  #print("matrix cons", str(consistentMatrix))
  return consistentMatrix


i=0
#print("Ceil", math.ceil(largest/smallest))

while (i < math.ceil(largest/smallest)+10):
  distanceDelta = -1
  #print("wbackupinfirstwhile", Wbackup )
  j=0
  while (j < len(Wbackup)):
    W = Wbackup
    Morig = generateconsistentmatrix(W)
    origDistanceResults = distance(M, Morig)
    #print("original distance", origDistanceResults)

    W = Wbackup
    W[j] = 2*W[j]
    Ma = generateconsistentmatrix(W);
    aDistanceResults = distance(M, Ma)

    W = Wbackup
    W[j] = W[j]/2
    Mb = generateconsistentmatrix(W);
    bDistanceResults = distance(M, Mb)

    distanceResults = 0;
    if aDistanceResults < bDistanceResults:
      distanceResults = aDistanceResults
      Wbackup[j] =  Wbackup[j]*2

    if bDistanceResults < origDistanceResults:
      distanceResults = bDistanceResults
      Wbackup[j] = Wbackup[j]/2
    else:
      distanceResults = origDistanceResults
      Wbackup[j] = Wbackup[j]

    if distanceDelta < 0 or distanceResults < distanceDelta:
      distanceDelta = distanceResults

    j+=1
  i+=1
  



Morig = generateconsistentmatrix(Wbackup)
dis = distance(M, Morig)
print("")
print("minimum distance: " )
print(dis)
print("")
print("Approximated consistent M' matrix: " )
print(str(Morig))