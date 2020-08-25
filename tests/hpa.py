
from tqdm import tqdm
import requests


for _ in tqdm(range(10000000)):
    requests.get("http://localhost:3080")
