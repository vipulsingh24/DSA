class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjancency list of prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []    
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True 