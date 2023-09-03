# @time   : 2023/7/12 10:14
# @author : Xiang Lei

from ultralytics import YOLO

# 加载模型
model = YOLO("/Users/lei/Desktop/qzj/ultralytics/con/qzj_model.yaml")  # 从头开始构建新模型
model = YOLO("yolov8n.pt")  # 加载预训练模型（建议用于训练）

# 使用模型
model.train(data="/Users/lei/Desktop/qzj/ultralytics/con/qzj_data.yaml", epochs=3)  # 训练模型
metrics = model.val()  # 在验证集上评估模型性能
# results = model("https://ultralytics.com/images/bus.jpg")  # 对图像进行预测
# success = model.export(format="onnx")  # 将模型导出为 ONNX 格式