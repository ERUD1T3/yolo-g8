# Import libraries
import torch
import torchvision
import numpy as np
from ultralytics import YOLO

# import type hints
from typing import Tuple, List, Dict, Union, Any


def main() -> None:
    """
    Main function
    :return: None
    """

    # Check if GPU is available
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using {device} device')
    # get device specs
    print(torch.cuda.get_device_name(0))

    # test of yolo  v8
    model = YOLO('yolov8n.pt')

    # test of yolo
    results = model(source=1, show=True, conf=0.4, save=True, stream=True)



if __name__ == '__main__':
    main()
