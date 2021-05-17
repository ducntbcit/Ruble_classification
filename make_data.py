import numpy as np
import cv2
import time
import os

# Label: 00000 là ko cầm tiền, còn lại là các mệnh giá
label = "0000"

cap = cv2.VideoCapture(0)

# Переменная счетчика, позволяющая сохранять данные только после 60 кадров, позволяет избежать получения денег вначале.
i=0
while(True):
    # Capture frame-by-frame
    #
    i+=1
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.resize(frame, dsize=None,fx=0.3,fy=0.3)

    # Hiển thị
    cv2.imshow('frame',frame)

    # Lưu dữ liệu
    if i>=60 and i<=1060:
        print("Количество снятых изображений  = ",i-60)
        # Создайте папку, если у вас ее нет, сохраните изображение в папке, соответствующей номиналу
        if not os.path.exists('data/' + str(label)):
            os.mkdir('data/' + str(label))

        cv2.imwrite('data/' + str(label) + "/" + str(i) + ".png",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Когда все будет сделано, отпустите захват
cap.release()
cv2.destroyAllWindows()