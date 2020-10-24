from functions import preprocess
import time
start_time = time.time()
preprocess("./images/4.jpg", "./result.jpg")
print("--- %s seconds ---" % (time.time() - start_time))