########################### METHOD 1 ###########################

input_list = input().split(']')

for i in range(len(input_list)):

    index_input_list = input_list[i].find('[')
    
    input_list[i] = input_list[i][index_input_list+1:]
    
filtered_list = [item for item in input_list if item != '']

list_results = []
for i in range(len(filtered_list)):
    for j in range(len(filtered_list[i])):
        list_results.append(filtered_list[i][j])

filtered_list_results = [item for item in list_results if item != ',']

integer_list = [int(num) for num in filtered_list_results]

integer_list.sort()
print(integer_list)

########################### METHOD 2 ###########################
# input_list = input().split(']')
# filtered_list = [item[item.rfind('[')+1:] for item in input_list if '[' in item]

# integer_list = [int(num) for item in filtered_list for num in item.split(',')]

# integer_list.sort()
# print(integer_list)