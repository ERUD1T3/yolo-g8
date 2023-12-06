# Import libraries
from ultralytics import YOLO


def main() -> None:
    """
    Main function
    :return: None
    """

    # test of yolo  v8
    model = YOLO('yolov8n.pt')
    # print(model.names)

    # test of yolo
    model(source=0, show=True, conf=0.4, save=True)


if __name__ == '__main__':
    main()
