A=float(input("Enter your Units : "))
B=float(input("Enter your Units : "))

# 0-100 = 5RS PER UNIT , 100< =10RS PER UNIT

if A>=100:
   D = A   - 100
   C = 100 * 5
   E = D   * 10
   print(C+E)

else:
    print(A*5)

if B>=100:
   D = A   - 100
   C = 100 * 5
   E = D   * 10
   print(C+E)

else:
    print(B*5)




