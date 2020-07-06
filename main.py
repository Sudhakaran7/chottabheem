class bheem():
    
    def __generate_roomno(self,arr):
        Max_pos = 0
        Min_pos = 0
        maxx = arr[0]
        minn = arr[0]
        val = 0
        for i in range(0, len(arr)):
            if (arr[i] > maxx):
                Max_pos = i
                maxx = arr[i]
        for i in range(0, len(arr)):
            if (arr[i] < minn):
                Min_pos = i
                minn = arr[i]
        val = abs(Max_pos) - abs(Min_pos)
        return arr[val - 1]
def rescue(self):
    return self.__generate_roomno()
