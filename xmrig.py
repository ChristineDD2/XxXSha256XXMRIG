import hashlib
import json
import requests
import time

def fetch_work(pool_url, worker_name):
    response = requests.get(f'{pool_url}/work?worker={worker_name}')
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch work: {response.text}")

def submit_work(pool_url, worker_name, job_id, nonce, result):
    data = {
        'worker': worker_name,
        'job_id': job_id,
        'nonce': nonce,
        'result': result
    }
    response = requests.post(f'{pool_url}/submit', json=data)
    return response.json()

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def mine(pool_url, worker_name):
    while True:
        work = fetch_work(pool_url, worker_name)
        job_id = work['job_id']
        target = work['target']
        data = work['data']
        
        nonce = 0
        while True:
            nonce_bytes = nonce.to_bytes(4, byteorder='little')
            hash_result = sha256(data + nonce_bytes)
            if hash_result < target:
                result = hash_result
                break
            nonce += 1

        response = submit_work(pool_url, worker_name, job_id, nonce, result)
        print(f"Submitted result: {response}")

if __name__ == "__main__":
    pool_url = "http://mining-dutch.nl/api"
    worker_name = "worker1"
    mine(pool_url, worker_name)
