import cv2

ann = "922 396 82 156 standing 918 302 82 133 standing 922 326 41 105 standing 808 294 57 145 standing 769 291 82 125 moving 548 321 60 122 setting 584 422 76 137 standing 521 409 65 124 standing 244 389 55 139 standing 1087 334 53 127 standing 1101 381 59 138 standing"
img = cv2.imread(r"C:\Users\engah\Downloads\videos_sample\videos_sample\10\20525\20525.jpg")

an_list = ann.split()

ACTION_COLORS = {
     "moving":(0, 255, 0),   
      "blocking": (0, 255, 255), 
    "standing": (255, 0, 0),   
   "setting":   (0, 0, 255),   
      "spiking":(255, 0, 255) 
}


for i in range(0, len(an_list), 5):
    x = int(an_list[i])
    y = int(an_list[i+1])
    w = int(an_list[i+2])
    h = int(an_list[i+3])
    x2 = x + w
    y2 = y + h
    action = an_list[i+4]
    color = ACTION_COLORS.get(action, (255, 255, 255))  
    
    cv2.rectangle(img, (x, y), (x2, y2), color, 2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    thickness = 1
    (text_width, text_height), baseline = cv2.getTextSize(action, font, font_scale, thickness)

    # مكان خلفية النص (مستطيل أسود تحت البوكس)
    cv2.rectangle(img, (x, y2), (x + text_width+4, 4+y2 + text_height + baseline), (255, 255, 255), -1)
    cv2.rectangle(img, (x-2, y2-2), (x + text_width+5, 5+y2 + text_height + baseline), (0, 0, 0), 2)
    # كتابة النص باللون المطلوب فوق الخلفية
    cv2.putText(img, action, (x, y2 + text_height), font, font_scale, color, thickness, cv2.LINE_AA)



cv2.rectangle(img,(100, 120),(300 , 170 ),(255, 255, 255),-1)
cv2.rectangle(img,(100-2, 120-2),(300+2 , 170+2 ),(0, 0,0),3)
cv2.putText(img, "Left Set", (130, 153),cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2,cv2.LINE_AA)
    
if img is not None:
    cv2.imshow("t", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
cv2.imwrite("sample.jpg", img)
