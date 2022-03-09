# cupti_test

## Set up python virtual environment

### Install python virtual environment
    cupti_test$ python3 -m venv ./venv

### Enter/Exit virtual environment
Enter python virtual environment

    cupti_test$ source ./venv/bin/activate

Exit python virtual environment

    (venv) cupti_test$ deactivate

### Set up library dependencies
Numpy, PyTorch, Pillow, matplotlib, torchvision

    (venv) cupti_test$ pip install numpy torch Pillow matplotlib, torchvision

If you are using `heart` server, please install pytorch as

    (venv) cupti_test$ pip3 install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio==0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

## Usage

Start training with: 

    python main.py

You can manually resume the training with: 
    
    python main.py --resume --lr=0.01
