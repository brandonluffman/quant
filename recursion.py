# def factorial(n):

#     if n == 0 or n == 1:
#         return 1

#     else:
#         print('Here')
#         return n * factorial(n-1)
    
# print(factorial(5))

def sum_numbers(n):
    if n == 1:
        return 1
    
    else:
        print(n)
        return n + sum_numbers(n-1)
    

print(sum_numbers(5))    