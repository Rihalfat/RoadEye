from ultralytics.utils import ASSETS
from ultralytics.models.yolo.detect import DetectionPredictor

args = dict(model='yolov8n.pt', source="0")
predictor = DetectionPredictor(overrides=args)
predictor.predict_cli()
