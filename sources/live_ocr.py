# Import libraries
from ultralytics import YOLO


def main() -> None:
    """
    Main function
    :return: None
    """

    # test of yolo  v8
    model = YOLO('yolov8n_ocr_best.pt')

    # test of yolo on camera feed is connected
    model(source=0, show=True, conf=0.4, save=True)


if __name__ == '__main__':
    main()
