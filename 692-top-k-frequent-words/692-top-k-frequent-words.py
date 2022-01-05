class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = collections.Counter(words)
		#De-duplicated words
        ddwords = list(freq.keys())
		#sort first with decreasing frequency then the second key is the word itself
        ddwords.sort(key = lambda x: (-freq[x], x))
		#return the first k words
        return ddwords[:k]