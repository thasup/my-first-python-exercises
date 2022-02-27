# f= open("some_file.txt", 'r')
# file_data = f.read()
# f.close()

# print(file_data)

###########################################

# files = []
# for i in range(10000):
#     files.append(open('some_file.txt','r'))
#     print(i)

###########################################

# f = open('some_file_0.txt','w')
# f.write('Luda is the best amongst other girls!')
# f.close()

###########################################

with open('some_file_0.txt', 'r') as f:
    file_data = f.read()

print(file_data)