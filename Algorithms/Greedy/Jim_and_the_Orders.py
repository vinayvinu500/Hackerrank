def jimOrders(od):
   arr = sorted([(i+1,sum(j)) for i,j in enumerate(od)],key=lambda x: x[1])
   return [i for i,j in arr]

print(jimOrders(orders))
