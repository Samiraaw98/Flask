# numbers =[24,56,3,89,78]
# print(f"[+] Given List{numbers}\n")

# m 

# Marks Solution 

def find_second(scores:list):
    scores.sort()
    scores.reverse()
    # print("List Start :")
    first = scores[0]
    for num in scores:
        if num != first:
            return num 
    

    
        # print(num , end = "")
        # print(',', end ='')
    # return scores[-2]


def solution2(scores:list):
    first = -101
    second = -101
    for num in scores:
        if num > first:
            second = first
            first = num
        if num > second and num != first:
            second = num 
    return  second
        

ls1 = [5,4,3,2,1]
ls2 = [-2,-5,0,5,20]
ls3 = [1,2,3,4,5,5]

print(find_second(ls1))
print(find_second(ls2))
print(find_second(ls3))

print(solution2(ls1))
print(solution2(ls2))
print(solution2(ls3))