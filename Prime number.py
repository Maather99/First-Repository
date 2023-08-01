print("Number | Prime Status")
print("--------------------")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num//2)+1):
        if(num % i == 0):
            return False
    return True
for num in range(1,31):
    print(f" {num}     | {is_prime( num)}")
