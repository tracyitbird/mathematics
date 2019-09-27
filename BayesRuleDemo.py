"""

贝叶斯概率计算
p(a|b)=(p(a)*p(b|a))/p(b)

参数：
prior:
likehood:
part1:
part2:
part3:
condition1:
condition2:
condition3:


"""

def BayesProbability(prior,likehood,dict1,dict2):

    if dict1.keys().__len__() != dict2.keys().__len__():
        print("check your input! The third argument and the fouth argument must "
              "have the equal number of elements")
        return


    posterior =0.0
    for i in range(dict1.keys().__len__()):
        posterior += dict1[i]*dict2[i]

    return (prior*likehood)/posterior










if __name__=="__main__":
    prior = 0.5
    likehood = 0.6
    dict1={}
    dict2={}
    dict1[0]= 0.5
    dict2[0]= 0.6
    dict1[1]=0.5
    dict2[1]=0.2

    print(BayesProbability(prior,likehood,dict1,dict2))





