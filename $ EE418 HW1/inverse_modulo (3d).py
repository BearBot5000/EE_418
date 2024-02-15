import time

def modInverse(a, m):
  # Initialize the result to 1.
  result = 1
  # Loop through all numbers from 1 to `m-1`.
  for i in range(1, m):
    #check if congruent using naive method
    if (i * a) % m == 1:
      return i
  # No Modulo
  return -1

#Get input
n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))

start_time = time.time()
inverse = modInverse(n,m)
end_time = time.time()
print("run time in seconds (s):", (end_time - start_time))

if inverse:
    print(f"Modular inverse of {n} mod {m} is {inverse}")
else:
    print(f"{n} has no modular inverse mod {m}")