nums=[]

for i in range(1,11):
    nums.append(i)

extracted_nums=[]

for i in range(5):
    extracted_nums.append(nums[i])

reversed_nums=[]
for i in range(4,-1,-1):
    reversed_nums.append(extracted_nums[i])

print("Original list: ", nums)
print("Extracted first five elements: ", extracted_nums)
print("Reversed extracted elements: ", reversed_nums)