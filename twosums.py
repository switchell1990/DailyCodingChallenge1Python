#Declare a function that will take in 2 values.
def pairSumK (num_lst, k):
    #Iterate through the number and if k - x then Return True else Return False.
  return any(map(lambda x: (k - x) in num_lst, num_lst))

print(pairSumK([10, 15, 3, 7], 17)) #Returns True
print(pairSumK([10, 15, 3, 7], 18)) #Returns True
print(pairSumK([10, 15, 3, 7], 19)) #Return False

print(pairSumK([], 0)) #Returns False
print(pairSumK([], 1)) #Returns False

print(pairSumK([5, 5], 10)) #Returns True
print(pairSumK([5], 10)) #Returns True

print(pairSumK([5, 0], 0)) #Returns True
print(pairSumK([5, 0], 5)) #Returns True
print(pairSumK([5, 0], 2)) #Returns Fals
