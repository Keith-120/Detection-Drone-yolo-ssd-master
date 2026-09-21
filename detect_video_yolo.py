import cv2
import random
from ultralytics import YOLO

# Classes du modèle (IMPORTANT)
class_list = ["Flame", "No_Flame"]

# Couleurs
detection_colors = [
    (255, 0, 0),    # Flame
    (0, 255, 0)     # No_Flame
]

# Charger le modèle
model = YOLO("Codes SSD/best_50.pt")

# Règles de recommandation
RECOMMENDATION_RULES = {
    "Flame": "⚠️ Incendie détecté : alerter les autorités",
    "No_Flame": "✅ Aucune flamme détectée"
}

# Vidéo
cap = cv2.VideoCapture("2345464_deforestation_fire_burn_3840x2160.mp4")

cv2.namedWindow("ObjectDetection", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detected_classes = []
    recommendations = set()

    results = model.predict(source=frame, conf=0.2, verbose=False)[0]

    if results.boxes is not None:
        for box in results.boxes:
            clsID = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            class_name = class_list[clsID]
            detected_classes.append(class_name)

            # Dessin bbox
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                detection_colors[clsID],
                2
            )

            cv2.putText(
                frame,
                f"{class_name} {conf:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                detection_colors[clsID],
                2
            )

    # Recommandation principale
    if "Flame" in detected_classes:
        flame_count = detected_classes.count("Flame")

        if flame_count > 2:
            recommendations.add("🚨 Incendie actif critique : intervention immédiate")
        else:
            recommendations.add(RECOMMENDATION_RULES["Flame"])
    else:
        recommendations.add(RECOMMENDATION_RULES["No_Flame"])

    # Affichage des recommandations
    y = 40
    for rec in recommendations:
        cv2.putText(
            frame,
            rec,
            (20, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )
        y += 35

    cv2.imshow("ObjectDetection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
