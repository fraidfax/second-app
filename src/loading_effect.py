from tqdm import tqdm
import time
import random
import sys
def pre_effect(num):
    for i in tqdm(range(0, random.randint(10,num))):
        time.sleep(random.uniform(0.1 ,0.3))
		# random.randint(1, random.randint(10, 30)
	
def time_effect(text):
	ran_dom = random.randint(18, 47)
	random_step = random.randint(-5, -1)
	time_freeze = random.uniform(0.1 ,0.3)

	for remaining in range(ran_dom, -1, random_step):
		sys.stdout.write("\r")
										# {:2d}".format(remaining)
		sys.stdout.write(str(text) + ".." +".") 
		sys.stdout.flush()
		time.sleep(time_freeze)
