##思路最重要，先排序，再插队
#套路，一般这种数对，还涉及排序的，根据第一个元素正向排序，根据第二个元素反向排序，或者根据第一个元素反向排序，根据第二个元素正向排序，能够简化解题过程。
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result=[]
        people=sorted(people,k=lambda x:(-x[0],x[1]))
        #people.sort(k=lambda x:(-x[0],x[1]))
        for i in people:
            if len(result)<=i[1]:
                result.append(i)
            else:
                result.insert(i[1],i)
        return result