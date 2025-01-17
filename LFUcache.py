class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = {}
        self.min_freq = 0

    def _update_freq(self, key):
        freq = self.key_to_freq[key]
        self.key_to_freq[key] += 1
        self.freq_to_keys[freq].remove(key)
        
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        
        new_freq = freq + 1
        if new_freq not in self.freq_to_keys:
            self.freq_to_keys[new_freq] = set()
        self.freq_to_keys[new_freq].add(key)

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        self._update_freq(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._update_freq(key)
            return
        
        if len(self.key_to_val) >= self.capacity:
            lfu_key = next(iter(self.freq_to_keys[self.min_freq]))
            self.freq_to_keys[self.min_freq].remove(lfu_key)
            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]
            del self.key_to_val[lfu_key]
            del self.key_to_freq[lfu_key]
        
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.min_freq = 1
        if 1 not in self.freq_to_keys:
            self.freq_to_keys[1] = set()
        self.freq_to_keys[1].add(key)
