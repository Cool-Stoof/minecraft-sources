import time
def wait(seconds):
	time.sleep(seconds)
print("Hello!")	
wait(2)
print("Did you see README.md?")
ans = input("Y for yes and N for no")
if ans == "y":
	print("great, bye!")
elif ans == "n":
	print("Please read README.md!")
else:
	print("that's not an answer. y or n.")
