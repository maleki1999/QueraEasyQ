from collections import Counter
vowel = ['a','e','u','i','o']
freq = Counter(input())
print(sum([freq[ch] for ch in freq.keys() if ch in vowel]))