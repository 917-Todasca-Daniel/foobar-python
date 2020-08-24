#   Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it - so you took the job gladly. 

#   Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

#   The fuel control mechanisms have three operations: 

#   1) Add one fuel pellet
#   2) Remove one fuel pellet
#   3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

#   Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

#   For example:
#   solution(4) returns 2: 4 -> 2 -> 1
#   solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

class Queue:
    def __init__(self):
        self.idx = 0
        self.arr = []
        self.ndelay = 0

    def push(self, x):
        self.arr.append(x)

    def front(self):
        return self.arr[self.idx]

    def pop(self):
        self.idx += 1
        if self.idx == self.ndelay:
            self.idx = 0
            self.arr = self.arr[self.ndelay:]

    def empty(self):
        if self.idx >= len(self.arr):
            return True
        return False

def solution(n):
    queue = Queue()
    queue.push(int(n))
    mem = {int(n) : 0}
    while queue.empty() == False:
        front = queue.front()
        queue.pop()
        
        if front == 1:
            break
        
        arr = [front+1, front-1]
        if front%2 == 0:
            arr.append(front/2)
            
        for num in arr:
            if num not in mem:
                mem[num] = mem[front] + 1
                queue.push(num)
    return mem[1]