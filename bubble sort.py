arr=[]
n=int(input("enter the no.of elements:"))
for i in range(n):
	arr.append(int(input(f"enter the element {i+1}:")))
print(f"array:{arr}")
for i in range(n):
	for j in range(i+1,n):
		if arr[i]>arr[j]:
			temp=arr[i]
			arr[i]=arr[j]
			arr[j]=temp
print("sorted array:",arr)

--------------------------------
OUTPUT:
mlm@mlm-H81:~/Desktop/dsml$ python3 bubble.py
enter the no.of elements:3
enter the element1:6
enter the element2:3
enter the element3:9
array:[6, 3, 9]
sorted array: [3, 6, 9]
