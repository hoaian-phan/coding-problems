class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        results = []
        
        all_files = []
        for path in paths:
            content = path.split()
            print(content)
            directory = content[0]
            files = content[1:]
            print(directory, files)
            for file in files:
                file_path = directory + '/' + file
                all_files.append(file_path)
                
        print("all_files", all_files)
        content_file = defaultdict(list)
        for file in all_files:
            inside = file.split("(")
            print(inside)
            name, reading = inside
            content_file[reading].append(name)
            
        print(content_file)
        for key, value in content_file.items():
            if len(value) >= 2:
                results.append(value)
            
        return results
                