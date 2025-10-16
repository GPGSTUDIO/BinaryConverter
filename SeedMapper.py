import random
import hashlib

def shuffle_text(text, seed=None):
    if seed is not None:
        if isinstance(seed, (int, float)):
            numeric_seed = int(seed)
        else:
            seed_str = str(seed)
            hash_obj = hashlib.md5(seed_str.encode())
            numeric_seed = int(hash_obj.hexdigest(), 16)
        random.seed(numeric_seed)
    text_list = list(text)
    random.shuffle(text_list)
    return ''.join(text_list)
