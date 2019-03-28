#!/usr/bin/env python3
import random
import os
import json


count = int(os.getenv('FILE_COUNT') or 10)
words = [word.strip().lower() for word in open('/usr/share/dict/words').readlines()]

for receipt_num in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        'topic': random.choice(words),
        'value': f'{amount:.2f}'
    }
    with open(f'./new/receipt-{receipt_num}.json', 'w') as f:
        json.dump(content, f)
