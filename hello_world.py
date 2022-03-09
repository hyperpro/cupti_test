import numpy as np
import random
import torch


def test_sys_environment():
    # Cuda installed
    assert torch.cuda.is_available() is True
    print('System works OK!')
    return 0


if __name__ == '__main__':
    test_sys_environment()
    