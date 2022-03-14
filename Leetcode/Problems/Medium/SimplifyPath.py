class Solution:
    def simplifyPath(self, path: str) -> str:
        newPath = []
        path = path.split('/')
        
        for i in range(len(path)):
            if len(newPath)!=0 and path[i]=='..':
                newPath.pop()
            elif path[i]!='.' and path[i]!='..' and path[i]!='':
                newPath.append(path[i])
        
        newPath = [s for s in newPath if s!='']
                
        return '/'+'/'.join(newPath)
        
