# Import libraries
import torch
import torchvision
import numpy as np
from ultralytics import YOLO

# import type hints
from typing import Tuple, List, Dict, Union, Any


def get_device() -> torch.device:
    """
    Get device specs
    :return: device
    """
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using {device} device')
    # get device specs
    print(torch.cuda.get_device_name(0))
    return device


def main() -> None:
    """
    Main function
    :return: None
    """

    # Check if GPU is available
    device = get_device()

    # test of yolo  v8
    model = YOLO('yolov8n_ocr_best.pt')
    # print(model.names)

    # test of yolo
    results = model(source=0, show=True, conf=0.4, save=True)



if __name__ == '__main__':
    main()
