# 要求一
def calculate(min, max, step):
    sum=0
    for i in range(min, max, step):
        sum+=i
    if (max-min)%step==0:
        sum+=max
    print(sum)

calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6 
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18 
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

# 要求二
def avg(data):
    sum=0
    n_manager=0
    for emp in data["employees"]:
        if emp["manager"]==False:
            n_manager+=1
            sum+=emp["salary"]
    print(sum/n_manager)

avg({
    "employees":[
        {   
            "name":"John", 
            "salary":30000, 
            "manager":False
        },
        {   
            "name":"Bob", 
            "salary":60000, 
            "manager":True
        },
        {
           "name":"Jenny", 
            "salary":50000, 
            "manager":False
        },
        {   "name":"Tony", 
            "salary":40000, 
            "manager":False
        }
    ]
}) # 呼叫 avg 函式

# 要求三
def func(a):
    def multiply(x,y):
        print(a+x*y)
    return multiply 

func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14 
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0 
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15 
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

# 要求四
def maxProduct(nums):
    n_num=len(nums)
    max=nums[0]*nums[1]
    if n_num>2:
        for i in range(n_num):
            for j in nums[i+1:]:
                temp=nums[i]*j
                if temp>max:
                    max=temp
    print(max)

maxProduct([5, 20, 2, 6]) # 得到 120 
maxProduct([10, -20, 0, 3]) # 得到 30 
maxProduct([10, -20, 0, -3]) # 得到 60 
maxProduct([-1, 2]) # 得到 -2 
maxProduct([-1, 0, 2]) # 得到 0 
maxProduct([5,-1, -2, 0]) # 得到 2 
maxProduct([-5, -2]) # 得到 10

# 要求五
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if target-nums[i]==nums[j]:
                return [i, j]
    
    # num_map={}
    # for i in range(len(nums)):
    #     difference=target-nums[i]
    #     if difference in num_map:
    #         return [num_map[difference],i]
    #     num_map[nums[i]]=i

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

# 要求六(optional)
def maxZeros(nums):
    n_zero=0
    max_length=0
    for i in nums:
        if i==0:
            n_zero+=1
        else:
            if n_zero>max_length:
                max_length=n_zero
            n_zero=0
    if n_zero>max_length:
        print(n_zero)
    else:
        print(max_length)
        
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4 
maxZeros([1, 1, 1, 1, 1]) # 得到 0 
maxZeros([0, 0, 0, 1, 1]) # 得到 3