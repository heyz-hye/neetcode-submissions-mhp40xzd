'''
i use default list to avoid writing get method for table if a key has never be declared at the table
you want to see if there is a matching timestamp with the exact key, if there not a matching then you return the most recent one that is
lees than the timestamp
ex:
time stamp can be 1,4,9
i want timestamp 5, you return 4
To micmic the most recent choice possible, you need to keep track of the time stamps, if a timestamp is less than the timestamp ask
we append to the res incase there isnt a matching aka the best so far, if there is a mathcing we return it

mistakes:
if we only check left<right we ignore the fact that the answer can be at left and right endpoint, the only way to get the right and left 
endpoint timestamp is if left==right, if the while loop only allow left<right then we never check these endpoints and the answer can be in there
'''
class TimeMap:
    def __init__(self):
        self.table=defaultdict(list)       

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        res=""
        array=self.table[key]

        left=0
        right=len(array)-1

        while left<=right:
            mid=(left+right)//2

            if array[mid][0]==timestamp:
                res=array[mid][1]
                return res
            
            if array[mid][0]>timestamp:
                right=mid-1
            
            else:
                res=array[mid][1]
                left=mid+1
        
        return res

        
