
import threading
from queue import Queue
import time

# 1. Design a food ordering system where your python program will run two threads,
# Place Order: This thread will be placing an order and inserting that into a queue. 
                # This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. 
                # This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.




food_order = Queue()

def place_order(order):
    for i in order:
        order = food_order.enqueue(i)
        print("Food ordering : ", i)
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while food_order.size() !=0 :
        order = food_order.dequeue()
        print("Now serving : ", order)
        time.sleep(2)


# 2. Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented

def produce_binary(number):
    num_queue = Queue()
    num_queue.enqueue('1')
    for i in range(number):
        front = num_queue.front()
        print(front) 
        num_queue.enqueue(front + '0') 
        num_queue.enqueue(front + '1') 

        num_queue.dequeue() 

if __name__=="__main__":

    dish = ['pizza','samosa','pasta','biryani','burger']

    place = threading.Thread(target = place_order, args = (dish,))
    server = threading.Thread(target = serve_order)
        
    place.start()
    server.start()

    produce_binary(10)
