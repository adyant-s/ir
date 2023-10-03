# -*- coding: utf-8 -*-

import numpy as np

graph = {0:[1],1:[0,2],2:[1]}

size = len(graph)

arr = [[0 for i in range(size)] for j in range(size)] # inner bracket for column outer for row i - col j -row

arr

for i in range(0,size):
    list1 = graph[i]
    n = len(list1)
    prob=0
    if not (n==0):
      prob = 1 / n
    else:
      for j in range(0,size):
        arr[i][j] = 1 / size
    for j in range(0,size):
      if j in list1:
        arr[i][j] = prob

arr

S = np.array(arr)

Alpha = 0.5

G = S

G = ((1-Alpha) * S)
G = G + ((Alpha)/size)

G

Intial_arr = [1/size for i in range(size)]
Intial_vector = np.array(Intial_arr)

Intial_vector

Prev = Intial_vector
Page_rank = Intial_vector

while(1):

  flag = 0
  Prev = Page_rank
  Page_rank = np.matmul(Page_rank,G)

  print("Previous value is ",Prev)
  print("Current value is ",Page_rank)
  print("\n")

  for i in range(0,len(Prev)):
    if (Page_rank[i] - Prev[i] > 0.01):
      flag=1
      break

  if flag==0:
    break

