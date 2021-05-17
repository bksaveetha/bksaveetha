'''import math

print("start quadratic and enter the value of a, b, c")

a = int(input())
b = int(input())
c = int(input())

discriminant = b*b-4*a*c

if(discriminant > 0):
    root1  = (-b+math.sqrt(discriminant))/(2*a)
    root2 =  (-b-math.sqrt(discriminant))/(2*a)
print("root1 " , root1 ,"=", "root2" ,root2)
elif(discriminant==0):
    root1 = root2 = b*b-4*(a*c)
print("root1=  root2", root1)


else:
    realpart = -b/(2*a)
    imaginary = math.sqrt(-discriminant)/(2*a)
    print("realpart = ", realpart , "imaginarypart = ", imaginary) '''



'''num = 5

factorial = 2


if num >=1:
    for i in range(1, num+1):
        factorial = factorial*i
        print("the factorial of num",num, "=" , factorial )'''


'''num  = 31


flag = False

if num > 1:
    for i in range(2, num):
        if(num% i)==0:
            flag = True
            break


if flag:
    print("The num is not prime number:",num)
else:
    print("it is a prime number", num)'''


'''terms = int(input("Enter the number :"))

a, b = 0,1
count = 0

if terms < 0:
    print("fibonacci doesn't exist")

if terms == 1:
    print("fibonacci exist for this number but try some higher number")  

if terms >  1:
    while count<terms:
        print(a)
        c= a+b
        a = b
        b = c 
        count += 1'''



'''def factorial(x):
    "hello geeks"

    if x == 1:
        return 1

    else:
        return(x *factorial(x-1))


num  = 4
print("the factorial of ", num, "is", factorial(num)) '''  


'''bk = []
fib(n)
    if n in bk , return bk[n]
    else,
        if n <2 , f = 1
        else , f = f(n-1)+f(n-2)
        bk[n] = f
        return f'''

#stack
'''def check_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) ==0

def push(stack, item):
    stack.append(item)
    print("show the item "   +item) 


def pop(stack):
    if (check_empty(stack)):
        return "stack is empty" 

    return stack.pop()


stack = check_stack()
push(stack, str(1))
push(stack, str(2)) 
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))
print("show the pop" +pop(stack))
print("show string objects" +str(stack))'''



'''class bkqueue():

    def __init__(self):
        self.queue= []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) <1:
            return None

        return self.queue.pop(0)   

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)         



mishra = bkqueue()
mishra.enqueue(1)
mishra.enqueue(2)
mishra.enqueue(3)
mishra.enqueue(4)

mishra.display()
mishra.dequeue()

print("after removing")
mishra.display()'''


#circular queue

'''class bkmishra():

    def __init__(self,k):
        self.k = k
        self.queue = [None]*k
        self.head = self.tail = -1


    def enqueue(self, data):
        if((self.tail -1)%self.k ==self.head):
            print("the circular queue is full")

        elif (self.head == -1):
            self.head =0 
            self.tail = 0
            self.queue[self.tail] = data

        else:
            self.tail = (self.tail +1)%  self.k
            self.queue[self.tail] =  data

    def dequeue(self):
        if (self.head ==-1):
            print("the circular queue is empty\n")

        elif (self.head==self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp

        else:
            temp = self.queue[self.head]
            self.head = (self.head +1)%self.k
            return temp



    def printqueue(self):
        if(self.head ==-1):
            print("no element in the queue")



        elif (self.tail>= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end= '')

            print()
        else:
            for i in range (self.head, self.k):
                print(self.queue[i],end ='')
            for i in range(0, self.tail +1):
                print(self.queue[i], end = '')

            print()


lol = bkmishra(5)
lol.enqueue(1)
lol.enqueue(2)
lol.enqueue(3)
lol.enqueue(4)
lol.enqueue(5)
print("initial queue")
lol.printqueue()

lol.dequeue()
print("after removing number")
lol.printqueue()'''



'''class priorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return '' .join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) ==0

    def insert(self, data):
        return self.queue.append(data)

    def delete(self):
        try:
            max= 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max =i
            item = self.queue[max] #max value
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

if __name__ == '__main__':
    myqueue = priorityQueue()
    myqueue.insert(1)                                        
    myqueue.insert(2)
    myqueue.insert(3)
    myqueue.insert(49)
    myqueue.insert(78)
    print(myqueue)
    while not myqueue.isEmpty():
        print(myqueue.delete())'''


'''class Deque:


    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.append(item)

    def addFront(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



q = Deque()
print(q.isEmpty())
q.addFront(2)
q.addFront(4)
q.addRear(7)
q.addRear(10)
print(q.size())
print(q.isEmpty())
q.addRear(11)
print(q.removeFront())
print(q.removeRear())
q.addFront(55)
q.addRear(44)
print(q.items)'''


'''class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == '__main__':

    linked = LinkedList()


    linked.head = Node(1)
    second = Node(2)
    third = Node(3)


    linked.head.next = second
    second.next = third


    while linked.head != None:
        print(linked.head.item , end = '  ')
        linked.head = linked.head.next'''


#linked list operation
'''class Node:

    def __init__(self,item):
        self.item= item
        self.head = None


class bkLinkedList:
    def __init__(self):
        self.head = None


    def insertAtBegining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, node, data):
        if node is None:
            print("the given must be in bkLinkedList")
            return

        new_node  = Node(data)
        new_node.next = node.next
        node.next = new_node


    def insertEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head =  new_node
            return


        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node


    def deletelist(self, position):
        if self.head == None:
            return

        temp_node = self.head

        if position == 0:
            self.head = temp_node.next
            temp_node = None
            return


        for i in range (position -1):
            temp_node=  temp_node.next
            if temp_node is None:
                break            

        if  temp_node is None:
            return

        if temp_node.next is None:
            return

        next = temp_node.next.next
        temp_node= None
        temp_node = next   


    def printlist(self):
        temp_node= self.head
        while(temp_node):
            print((temp_node.item) + " ", end =" ")
            temp_node = temp_node.next

if __name__ == "__main__":

    lenovo = bkLinkedList()
    lenovo.insertAtBegining(1)
    lenovo.insertAtBegining(2)
    lenovo.insertEnd(11)
    lenovo.insertEnd(4)
    lenovo.insertAfter(lenovo.head.next ,5)

    print(" show list")
    lenovo.printlist()


    print("\n delete node")
    lenovo.deletelist(3)          
    lenovo.printlist()  '''


'''hashTable = [[],]*10

def checkPrime(n):
    if n ==0 or n==1:
        return 0

    for  i in range(2, n//2):
        if n%i ==0:
            return 0

    return 1


def getPrime(n):
    if n %2 ==0:
        n =n+1

    while not checkPrime(n):
        n+=2
    return n


def hashFunction(key):
    capacity =getPrime(10)
    return key%capacity

def insertdata(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]


def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0


insertdata(2, 'apple')
insertdata(4, 'orange')
insertdata(5, 'guava')
insertdata(7, 'watermelon')
insertdata(9, 'grapes')
print(hashTable)

removeData(234)

print(hashTable) '''


'''def heapify(arr,n, i):
    largest =i
    l = 2 * i +1
    r = 2 * i +2

    if l < n and arr[i] < arr[l]:
        largest = 1
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n , largest)


def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)



def deleteNode(array, num):
    size = len(array)
    i =0 
    for i in range (0, size):
        if num== array[i]:
            break

    array[i], array[size -1] = array[size -1], array[i]
    array.remove(num)    
  

    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array ), i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array" +str(arr))

deleteNode(arr, 4)
print("after deleting an element" +str(arr))'''


'''import math

class FibonacciTree:
    def __init__(self, value):
        self.value = value
        self.child  = []
        self.order = 0

    def add_at_end(self, t):
        self.child.append(t)
        self.order = self.order +1

class FibonacciHeap:
    def __init__(self, value):
        self.tree = []
        self.least = None  
        self.count  = 0

    def insert_node(self , value):
        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        if(self.least is None or value <self.least.value):
            self.least = new_tree
        self.count = self.count +1


    def get_min(self):
        if self.least is None:
            return None
        return self.least.value


    def extract_min(self):
        smallest = self.least
        if smallest is not None:
            for child in smallest.child:
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.tress == []:
                self.least = None 
            else:
                self.least =self.trees[0]
                self.consolidate()
            self.count = self.count -1
            return smallest.value

    def consolidate(self):
        aux = (floor_log(self.count) +1) *[None]
        while self.trees ! = []:
            x= self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.value > y.value:
                    x ,y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order +1
            aux[order] = x

        self.least = None
        for k in aux :
            if k is not None:
                self.trees.append(k)
                if (self.least is None
                    or k.value <  self.least.value):
                    self.least = k 
def floor_log(x):
    return math.frexp(x)[1] -1

fibonacci_heap = Fibonacciheap()
fibonacci_heap.insert_node(7)   
fibonacci_heap.insert_node(9)
fibonacci_heap.insert_node(14)
fibonacci_heap.insert_node(17)

print(" the minimum value  of fibonacci heap : {}".format(fibonacci_heap.get_min()))
print("minimum value is removed :{}" .format(fibonacci_heap.extract_min()))'''


    
            













        

