from ultralytics import YOLO

model = YOLO("model.pt")


def predict(source):
    results = model.predict(source=source, save=True, save_txt=True)
    print(results)

    return results
