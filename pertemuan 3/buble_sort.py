data= [5,3,4,]

print("data awal", data)
print()
n= len(data)

for i in range(n-1):
   print(f"iterasi ke-{i+1}:")
   for j in range(n-i-1):
       print(f" Bandingkan {data[i]} dan {data[i+1]}, end "" ")
       if data[j]>data[j+1]:
          data[j],data[j+1] = data[j+1], data[j ]

print("data setelah diurutkan dengan buble sort", data)

