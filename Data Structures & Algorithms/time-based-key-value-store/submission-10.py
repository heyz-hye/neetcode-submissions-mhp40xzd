'''
time:key:value

get return most recent value of key that has being set
also make the set timestamp prev_timestamp
set timestamp are in increasing order
creat a hashtable




'''


class TimeMap:

    def __init__(self):
        self.table={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key]=[] #initiate key match with an empty list 
        self.table[key].append([value,timestamp]) #we use bracket in this case because bracket is for list
        #in the bracket we have pairs
            
        

    def get(self, key: str, timestamp: int) -> str:
        res=""
        values=self.table.get(key,[])

        left=0
        right=len(values)-1

        while left<=right:
            mid=(left+right)//2

            if values[mid][1]==timestamp:
                res=values[mid][0]
                return res

            if values[mid][1]<timestamp:
                res=values[mid][0]
                left=mid+1

            if values[mid][1]>timestamp:
                right=mid-1
        return res
            

        
