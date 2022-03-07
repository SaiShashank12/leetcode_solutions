class UnionFind:
    def __init__(self, num):
        self.parent = list(range(num))
        self.rank = [0 for _ in range(num)]
    
    def find_set(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find_set(self.parent[u])
        return self.parent[u]

    def union(self, set1, set2):
        if set1 == set2:
            return
        rank1, rank2 = self.rank[set1], self.rank[set2]
        if rank1 > rank2:
            self.parent[set2] = set1
        else:
            self.parent[set1] = set2
            if rank1 == rank2:
                self.rank[set2] += 1
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #create idx-to-address dictionary and address-to-idx dictionary
        address_set = set()
        for account in accounts:
            for address in account[1:]:
                address_set.add(address)
                
        N, M = len(accounts), len(address_set)
        addresses = sorted(list(address_set))
        idx_address_dict = {(idx + N) : address for idx, address in enumerate(addresses)}
        address_idx_dict = {address : (idx + N) for idx, address in enumerate(addresses)}
        
        #create union find object
        uf = UnionFind(N + M)
        
        #union all pairs of (person, address)
        for i, account in enumerate(accounts):
            for address in account[1:]:
                address_idx = address_idx_dict[address]
                uf.union(uf.find_set(i), uf.find_set(address_idx))
        
        #get the parent for all elements (it can be person's name or address)
        #note that for idx = 0, 1, 2, ..., N - 1, N, N + 1, ...., N + M - 2, N + M - 1,
        #0 <= idx < N      => name
        #N <= idx < N + M  => address
        parent_dict = collections.defaultdict(list)
        for i in range(N + M):
            parent = uf.find_set(i)
            parent_dict[parent].append(i)
        
        #for each group (=account), output the result
        #Note that the accounts themselves can be returned in any order
        #note: each group always contains exactly one person's name. Also, the smallest number is person's name
        res = []
        for group in parent_dict.values():
            person_idx = group[0]
            person = accounts[person_idx][0]
            data = [person]
            for address_idx in group[1:]:
                if address_idx >= N:
                    data.append(idx_address_dict[address_idx])
            res.append(data)
        
        return res