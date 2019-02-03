# Object-Oriented programming utilizes objects linkning to other objects. 
# Works upon the idea of inheritance - assigning your types based on what you are
# Pros:
# - allows for parallel development once the modular classes have been worked out
# - modular classes are often reusable
# - very readable and understandable
# - utilizes an imperative style, in which code reads like a straigt-forward set of instructions as a computer would read
# Cons:
# - tends to use more CPU
# - Too scalable: massive amount of bloated, unnecessary code
# - commonly depends upon shareable state.
# - race conditions: when parallel code that would access a shared resouce do so in such a way as to cause unexpected results
# Function programming avoids shared state and mutation. 
# Pros: 
# - Utilizing pure functions, reliable functions with no side effects 
# - declarative style, focus on what to do rather than how it's being done
# - emphasis on performance and optimization
# Cons:
# - lack readability at times
# - newer paradigm

class HitCounter(object):
    def __init__(self, size):
        self.size = size
        self.hit_counts = {}
        self.count = 0

    def _prune_hit_counts(self):
        t = time.time()
        t_cutoff = t - self.size
        for t_hit in self.hit_counts.keys():
            if t_hit < t_cutoff:
                self.count -= self.hit_counts[t_hit]
                self.hit_counts[t_hit] = 0

    def log_hit(self):
        t = time.time()
        if t in self.hit_counts:
            self.hit_counts[t] += 1
        else:
            self.hit_counts[t] = 1
        self.count += 1
        self._prune_hit_counts()

    def get_hit(self):
        t = time.time()
        self._prune_hit_counts()
        return self.count

def main():
    # Write a hit counter for hits received in the past 5 minutes.
    # The HitCounter has two methods:
    # void hit()   // record a hit.
    # long getHits()   // Return the number of hits in the last 5 minutes.

    HIT = 10
    WAIT = 5
    hc = HitCounter(HIT)

    print('Hitting once a second for {} seconds...'.format(HIT))
    for _ in range(HIT):
        hc.log_hit()
        print(hc.get_hit())
        time.sleep(1)
    for _ in range(WAIT):
        print('Waiting...')
        time.sleep(1)

    print(hc.get_hit())     # HIT - WAIT - 1
    time.sleep(1)
    print(hc.get_hit())     # HIT - WAIT - 2
    print('End')

if __name__ == "__main__":
    main()