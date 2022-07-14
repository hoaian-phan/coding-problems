class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        
        # make a dict of {index:soldier}
        # sort dict by values
        # return slicing of sorted keys until k index
        
        results = []
        mat_dict = {}
        for index in range(len(mat)):
            mat_dict[index] = mat[index].count(1)
            
        print(mat_dict)
        
        sort_dict = sorted(mat_dict.items(), key=lambda x: x[1], reverse=False)
        
        print(sort_dict)
        
        for i in range(k):
            results.append(sort_dict[i][0])
            
        return results
        
        
        