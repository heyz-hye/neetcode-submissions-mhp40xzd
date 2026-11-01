class TimeMap:

    def __init__(self):
        self.table=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res=""
        array=self.table[key]
        l=0
        r=len(array)-1

        while l<=r:
            mid=(l+r)//2
            
            if array[mid][1]==timestamp:
                res=array[mid][0]
                return res
            
            elif array[mid][1]>timestamp:
                r=mid-1
            
            else:
                res=array[mid][0]
                l=mid+1
        
        return res


        
