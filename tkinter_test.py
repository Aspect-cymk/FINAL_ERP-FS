from tqdm import tqdm
from time import sleep

for i in tqdm(range(0, 100), ncols=100, desc="Text You Want"):
    sleep(0.1)
