import numpy as np
import random
import torch

if __name__ == '__main__':
    print('Torch test')
    x = torch.rand(5, 3)
    print(torch.cuda.is_available())
    print(torch.version.cuda)