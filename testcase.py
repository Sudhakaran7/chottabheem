from main import bheem

def test_case1(return_val):
    flag=0

    if['1 2 3 4 5'] == return_val:
        print(return_val)
        flag+=1
        exit(0)

    else:
        pass
    if(flag==0):
        print('0')
arr = list(map(int,input().split()))
child = bheem(arr)
test_case1(child.edges())
