from collections import Counter

def fruit(reels, spins):
    jackpots = {
        'Wild': 100,
        "Star": 90,
        "Bell": 80,
        "Shell": 70,
        "Seven": 60,
        "Cherry": 50,
        "Bar": 40,
        "King": 30,
        "Queen": 20,
        "Jack": 10
    }
    
    result = [r[s] for r, s in zip(reels, spins)]
    
    counts = Counter(result)
    
    if len(counts) == 1:
        return jackpots[result[0]]
    
    if len(counts) == 2:
        for symbol, count in counts.items():
            if count == 2:
                score = jackpots[symbol] // 10
                if 'Wild' in counts and counts['Wild'] == 1 and symbol != 'Wild':
                    score *= 2
                return score
    return 0
