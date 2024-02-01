import threading
import time

# Define the first function to run in a separate thread
def function_one(a):
    time.sleep(1)
    print("Function One is running after ", a," second.")
    pass

# Define the second function to run in a separate thread
def function_two(b):
    time.sleep(5)
    print("Argument : ", b)
    print("Function Two is running after 3 second.")
    pass

if __name__ == "__main__":  # confirms that the code is under main function
    # Create two threads for each function
    thread_two = threading.Thread(target=function_two, args=[2])

    # Start both threads
    print("I am calling one fuction then calling other without waiting to complete first one")
    thread_two.start()
    print("Calling function 2\n\n")
    thread_two.join()
    
    for i in range(10):
        thread_one = threading.Thread(target=function_one, args=[i])
        thread_one.start()

    print("Calling function task is completed\n\n")

    # Wait for both threads to finish (this won't happen in this example)
    # thread_one.join()
    # thread_two.join()
