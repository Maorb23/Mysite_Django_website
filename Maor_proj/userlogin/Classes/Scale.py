class Scale:
    def __init__(self):
        self.mean = None
        self.median = None
        self.max = None
        self.min = None
        self.std = None
        
    ## Standardization
    def stand_fit(self, X):
        self.mean = X.mean(axis=0)
        self.std = X.std(axis=0, ddof=0) # ddof=0 is the default, with 1 we get worse results because it's with correction
        return self


    def transform(self, X):
        return (X - self.mean) / self.std

    def fit_transform(self, X):
        self.stand_fit(X)
        return self.transform(X)

    def inverse_stand(self, X):
        return X * self.std + self.mean
    
    ## MinMax - Extra
    def minmax_fit(self, X): 
        self.min = X.min(axis=0)
        self.max = X.max(axis=0)
        return self
    
    def minmax_transform(self, X):
        return (X - self.min) / (self.max - self.min)
    
    def minmax_fit_transform(self, X,a,b):
        return self.minmax_fit(X).minmax_transform(X) * (b - a) + a

