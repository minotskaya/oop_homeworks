import time
import sys




def logger(path):

	def wrapper(func):

		def f(*args, **kwargs):

			start = time.time()
			result = func(*args, **kwargs)
			finish = time.time()
			data = {"start": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start)) ,
					"args": args, "return": (lambda x: "-" if x == None else x)(result),
					"finish": time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(finish)) ,
			 		"time_of_work": round(finish - start, 3)}
			with open(path, 'a' ) as f:
				f.write(str(data) + "\n")

			return result

		return f

	return wrapper




@logger("data.log")
def my_func(a, b, c):
	d = a + b + c
	time.sleep(1)




my_func(1, 2, 3)
