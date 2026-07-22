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

        
