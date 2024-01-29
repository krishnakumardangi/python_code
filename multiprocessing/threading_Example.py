import threading
import time

# Define the first function to run in a separate thread
def function_one():
    time.sleep(5)
    print("Function One is running after 5 second.")
    pass

# Define the second function to run in a separate thread
def function_two():
    time.sleep(3)
    print("Function Two is running after 3 second.")
    pass

if __name__ == "__main__":  # confirms that the code is under main function
    # Create two threads for each function
    thread_one = threading.Thread(target=function_one)
    thread_two = threading.Thread(target=function_two)

    # Start both threads
    print("I am calling one fuction then calling other without waiting to complete first one")
    thread_one.start()
    print("Somethig in between")
    thread_two.start()
    print("Calling funvtioin is complete")

    # Wait for both threads to finish (this won't happen in this example)
    # thread_one.join()
# thread_two.join()
