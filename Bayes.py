class Bayes:


    def __init__(self):
        self._container = dict()

    def set_prior(self,hypothis,prior):

        self._container[hypothis]=prior

    def mult(self,hypothis,likehood):

        prior = self._container[hypothis]

        self._container[hypothis]= prior * likehood

    # 归一化
    def nomalize(self):

        sum =0

        for prob in  self._container.values():
            sum+=prob
        for hypothis in self._container.keys():
            old= self[hypothis]
            self[hypothis]= old/sum
    def prob(self,hypothis):
        prob= self._container[hypothis]
        return prob
if __name__ == "__main__":
     bayes = Bayes()
     bayes.set_prior("FR",30/365)
     bayes.set_prior("FNR",335/365)
     bayes.mult("FR",0.8)
     bayes.mult("FNR",0.2)
     print(bayes.prob("FNR"))







