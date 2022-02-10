import time 

print("Press Enter To Start, Press Ctrl+C To Stop")

while True:
	try:
		input()
		starttime = time.time()
		print("Started")
	except KeyboardInterrupt:
		print("Stopped")
		endtime = time.time()
		print("Total time:",round(endtime - starttime,2),'secs')
		break