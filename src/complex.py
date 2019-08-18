import torch 
import numpy as np 


class CPLX:
    
    def __init__(self, real, imag):
        self.r = real
        self.i = imag 
    
    def magnitude(self):
        return torch.sqrt(self.r.pow(2) + self.i.pow(2))
    
    def size(self):
        return self.r.size(), self.i.size()

    def flatten(self):
        self.r = torch.flatten(x.r)
        self.i = torch.flatten(x.i)
    
    