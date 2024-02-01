# Multiprocessing in Python #

## ThreadPool Class in Python ##
The multiprocessing.pool.ThreadPool class in Python provides a pool of resable threads for executing ad hoc tasks.

"A thread pool object which controls a pool of workers threads to which jobs can be submitted." - MULTIPROCESSING PROCESS-BASED PARALLELISM

We can create a thread pool by instantiating the ThreadPool class and specifying the number of threads via the “processes” argument; 
for example:
```
# create a thread pool
pool = ThreadPool(processes=10)
```

## Life-Cycle of the ThreadPool ##
There are four main steps in the life-cycle of using the ThreadPool class, they are: create, submit, wait, and shutdown.

<br>Step 1. Create: Create the thread pool by calling the constructor ThreadPool().
<br>Step 2. Submit: Submit tasks synchronously or asynchronously.
<br>Step 3. Wait: Wait and get results as tasks complete (optional).
        <br>3a. Wait on AsyncResult objects to Complete
        <br>3b. Wait on AsyncResult objects for Result
<br>Step 4. Shutdown: Shut down the thread pool by calling shutdown().
        <br>4a. Shutdown Automatically with the Context Manager

The following figure helps to picture the life-cycle of the ThreadPool class.

1. CREATE: pool = multiprocessing.pool.ThreadPool(processes = 4)
```
# create a default thread pool
pool = multiprocessing.pool.ThreadPool()
```
```
# create a thread pool with 4 workers
pool = multiprocessing.pool.ThreadPool(processes=4)
```

2. SUBMIT: pool.apply(task), pool.map(task, items), pool.starmap(task, items)
<br>  2a. Issue Tasks Synchronously
```
# issue a task to the thread pool
pool.apply(task)
```
```
# iterates return values from the issued tasks
for result in map(task, items):
	# ...
```
```
# iterates return values from the issued tasks
for result in starmap(task, items):
	# ...
```
<br>  2b. Issue Tasks Asynchronously
Issuing tasks asynchronously to the thread pool means that the caller will not block, allowing the caller to continue on with other work while the tasks are executing.
```
# issue tasks to the thread pool asynchronously
result = map_async(task, items)
```
The imap() function takes the name of a target function and an iterable like the map() function.
<br>The difference is that the imap() function is lazier in two ways:
* imap() issues multiple tasks to the thread pool one by one, instead of all at once like map().
* imap() returns an iterable that yields results one-by-one as tasks are completed, rather than one-by-one after all tasks have been completed like map().
<br>For example:
```
# iterates results as tasks are completed in order
for result in imap(task, items):
	# ...
```
3. WAIT: pool.wait(), pool.get()
<br>3a. Wait on AsyncResult objects to Complete
```
# wait for issued task to complete with a timeout
result.wait(timeout=10)
# check if the tasks are all done
if result.ready()
	print('All Done')
	...
else :
	print('Not Done Yet')
	...
```
<br>3b. Wait on AsyncResult objects for Result
<br>A “timeout” argument can be specified. If the tasks are still running and do not completed within the specified number of seconds, a multiprocessing.TimeoutError is raised.
```
# get the result of the task or tasks
value = result.get()
```

4. SHUTDOWN: pool.close(), pool.terminate()
<br>The close() function will return immediately and the pool will not take any further tasks.
<br>For example:
```
# close the thread pool
pool.close()
```
Alternatively, we may want to forcefully terminate all worker threads, regardless of whether they are executing tasks or not.
<br>This can be achieved via the terminate() function.
<br>For example:
```
# forcefully close all worker threads
pool.terminate()
```
We may want to then wait for all tasks in the pool to finish.
<br>This can be achieved by calling the join() function on the pool.
<br>For example:
```
# wait for all issued tasks to complete
pool.join()
```
