#TC - O(∣E∣+∣V∣)
#SC - O(∣E∣+∣V∣)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses
        q = deque()
        adj = defaultdict(list)
        
        for course,prereq in  prerequisites:
            adj[prereq].append(course)
            indegree[course]= indegree[course]+1
            
        for k,v in enumerate(indegree):
            if v == 0:
                q.append(k)
        
        if not q:
            return False
        
        courseCompleted = 0
        while q:
            c = q.popleft()
            courseCompleted+=1
            for v in adj[c]:
                indegree[v]-=1
                if indegree[v] == 0:
                    q.append(v)
        
        return courseCompleted == numCourses