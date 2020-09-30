num_list = []
for i in range(5):
    num = input("Enter a number: ")
    num_list.append(num)
    
max_list = []

for i in num_list:
    if max_list == []:
        max_list.append(int(i))
    if int(i) > max_list[0]:
        max_list[0] = int(i)
            
print(max_list[0])    