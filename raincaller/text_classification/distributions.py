from bisect import bisect_left
from random import random



def create_cumulative_distribution(count_hashtable):
    x_cum_freqs = []
    x_range = []

    sorted_pairs = sorted([(freq, char) for (char, freq) in count_hashtable.items()], reverse=True)        
    cum_freq = 0
    x_cum_freqs = []
    x_range = []
    for freq, char in sorted_pairs:            
        cum_freq += freq
        x_cum_freqs.append(cum_freq)
        x_range.append(char)

    x_cum_freqs = [x/cum_freq for x in x_cum_freqs]
    return x_cum_freqs, x_range

class Distribution():
    def __init__(self):
        pass

    def get_one(self):
        pass

class CharacterDistribution(Distribution):
    def __init__(self, count_hashtable):
        
        self.x_cum_freqs, self.x_values = create_cumulative_distribution(count_hashtable)

    def get_one(self):
        seed = random()
        pos = bisect_left(self.x_cum_freqs, seed)
        return self.x_values[pos]

class WordDistribution(Distribution):
    def __init__(self):
        pass

    def get_one(self):
        pass