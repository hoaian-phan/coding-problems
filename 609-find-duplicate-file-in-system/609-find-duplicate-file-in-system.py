class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        results = []
        
        all_files = []
        for path in paths:
            content = path.split()
            for i in range(1, len(content)):
                file_path = content[0] + '/' + content[i]
                all_files.append(file_path)
                
       
        content_file = defaultdict(list)
        for file in all_files:
            inside = file.split("(")
            content_file[inside[1]].append(inside[0])
            
   
        for key, value in content_file.items():
            if len(value) >= 2:
                results.append(value)
            
        return results
                