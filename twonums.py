#algorithm
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num=list(nums)
        x = 0
        #print(list(nums))
        for i in range(len(num)):
            #print(i)
            n=target-num[i]
            #print(num[i])
            print(i,n)
            print("########")
            for j in range(len(num)):
                print(j,num[j])
                if num[j] == n:
                    x = j
                    break
            print("----------")
            if x != 0:
                break

        return i,x
        
