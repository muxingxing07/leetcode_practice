##˼·����Ҫ���������ٲ��
#��·��һ���������ԣ����漰����ģ����ݵ�һ��Ԫ���������򣬸��ݵڶ���Ԫ�ط������򣬻��߸��ݵ�һ��Ԫ�ط������򣬸��ݵڶ���Ԫ�����������ܹ��򻯽�����̡�
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