#AERT TOOLKIT -UNIT-1 ASSIGNMENT
#--------------------------------#
# PART-A-STACK ADT
#--------------------------------#
class StackADT:
    def __init__(self):
        self.stack = []

    def push(self,x):
            self.stack.append(x)

    def pop(self):
          if not self.is_empty():
              return self.stack.pop()
          return None
        
    def peek(self):
          if not self.is_empty():
             return self.stack[-1]
          return None
          
    def is_empty(self):
         return len(self.stack)==0
    
    def size(self):   
      return len(self.stack)
#-----------------------------------#
#PART-B-FACTORIAL(RECURSIVE)
#-----------------------------------#
def factorial(n):
         if n < 0:
            return "Invalid input"
         if n ==0 or n==1:
              return 1
         return n * factorial(n-1)

#------------------------------------#
#FIBONACCI SERIES
#------------------------------------#
count1=0

def fib_naive(n):
     global count1
     count1=count1+1

     if n==0:
          return 0
     if n==1:
          return 1
     return fib_naive(n-1)+fib_naive(n-2)

#------------------------------------------#
# fibonacci(memorized)
#------------------------------------------#

count2=0
memo={}

def fib_memo(n):
     global count2
     count2=count2+1

     if n in memo:
          return memo[n]
     
     if n ==0:
          memo[n]=0
     elif n ==1:
          memo[n]=1
     else:
          memo[n]=fib_memo(n-1)+fib_memo(n-2)

     return memo[n]

#--------------------------------------#
#tower of hanoi
#--------------------------------------#

def hanoi(n, source, auxiliary, destination, stack):

    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        stack.push(move)
        return

    hanoi(n-1, source, destination, auxiliary, stack)

    move = f"Move disk {n} from {source} to {destination}"
    stack.push(move)

    hanoi(n-1, auxiliary, source, destination, stack)
    

#------------------------------------------#
#recursive binary search
#------------------------------------------#

def binary_search(arr,key,low,high):

     if low>high:
          return-1
     
     mid = (low+high)//2

     if arr[mid]==key:
          return mid
     
     elif key<arr[mid]:
          return binary_search(arr,key,low,mid-1)
     
     else:
          return binary_search(arr,key,mid+1,high)
     

#---------------------------------------------------#
#main function
#---------------------------------------------------#

if __name__=="__main__":
    print("----- STACK TEST -----")
    st = StackADT()
    st.push(10)
    st.push(20)
    print("Top element:", st.peek())
    print("Stack size:", st.size())
    print("Popped:", st.pop())
    print("Stack size after pop:", st.size())


    print("\n----- FACTORIAL TEST -----")
    for n in [0,1,5,10]:
        print("factorial(", n, ") =", factorial(n))


    print("\n----- FIBONACCI TEST -----")
    for n in [5,10,20,30]:

        count1 = 0
        result1 = fib_naive(n)
        print("\nNaive fib(", n, ") =", result1)
        print("Naive Calls =", count1)

        count2 = 0
        memo.clear()
        result2 = fib_memo(n)
        print("Memo fib(", n, ") =", result2)
        print("Memo Calls =", count2)


    print("\n----- TOWER OF HANOI (N=3) -----")
    st_hanoi = StackADT()
    hanoi(3, "A", "B", "C", st_hanoi)

    while not st_hanoi.is_empty():
        print(st_hanoi.pop())

    print("\n----- BINARY SEARCH TEST -----")
    arr = [1,3,5,7,9,11,13]

    for key in [7,1,13,2]:
        print("Search", key, ":", binary_search(arr, key, 0, len(arr)-1))

    print("Empty array test:",
          binary_search([], 5, 0, -1))

