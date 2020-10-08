#单指针
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        p=n-1
        for i in range(n):
            if(p>i):
                s[i],s[p]=s[p],s[i]
                p=p-1
            else:
                break

#双指针
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        p=n-1
        i=0
        while(i<p):
            s[i], s[p] = s[p], s[i]
            p=p-1
            i=i+1
