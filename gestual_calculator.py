# powered by : oub3t4 #

import cv2
import mediapipe as mp
import os

from comands import *

def count_fingers(handLandmarks):
    dedos = [8, 12, 16, 20]
    dedoslevantados = []
    if handLandmarks:
        if handLandmarks[4].x < handLandmarks[3].x:
            dedoslevantados.append(0)  # Polegar levantado
        for i, x in enumerate(dedos):
            if handLandmarks[x].y < handLandmarks[x - 2].y:
                dedoslevantados.append(i+1)  # Dedo i levantado
    return dedoslevantados

def detect_hand(img, Hands, mpDraw):
    frameRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hands.process(frameRGB)
    handPoints = results.multi_hand_landmarks

    global fingers_raised

    fingers = [4,8,12,16,20]

    fingers_raised = {}

    if handPoints:
        for handId, handLandmarks in enumerate(handPoints):

            try:
                fingers_raised[str(handId)] = [finger + 1 for finger in count_fingers(handLandmarks.landmark)]
            except:
                count_fingers(handLandmarks.landmark)

            if state == "started" :

                for id, cord in enumerate(handLandmarks.landmark):

                    for num_value in fingers:

                        if id == num_value:

                            h, w, _ = img.shape
                            cy = int(cord.y * h)
                            cx = int(cord.x * w)
                            cv2.putText(img, str(handId), (cx - 10, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

                mpDraw.draw_landmarks(img, handLandmarks, hands.HAND_CONNECTIONS,mpDraw.DrawingSpec(color=(28, 115, 35), thickness=2, circle_radius=5), mpDraw.DrawingSpec(color=(109,30,148), thickness=2, circle_radius=2))

    return img

# //=====================// //=====================// #

counter:int = 0
fingers_raised = {}
equation = ""
state = "waiting"
historic = []

video = cv2.VideoCapture(0)

hands = mp.solutions.hands
Hands = hands.Hands(max_num_hands=2)
mpDraw = mp.solutions.drawing_utils

while True:

    counter += 1

    success, img = video.read()

    if not success:
        print("Erro ao capturar vídeo.")
        break

    img = detect_hand(img, Hands, mpDraw)

    if counter % 20 == 0:

        os.system('cls')

        actions = {

        "two_handed" : None,
        "0" : None,
        "1" : None

        }

        fHand = False
        sHand = False

        if "0" in fingers_raised:
            fHand = True
            actions["0"] = (read_action(fingers_raised["0"]))

        if "1" in fingers_raised:
            sHand = True
            actions["1"] = (read_action(fingers_raised["1"]))

        if "0" in fingers_raised and "1" in fingers_raised:

            fingers_raised["1"] = [x + 5 for x in fingers_raised["1"] ]
            actions["two_handed"] = read_action(fingers_raised["0"] + fingers_raised["1"],bits=10)
        
        
        for i in actions: print(f"{i} : {actions[i]}")


        if state == "waiting":
            if actions["two_handed"] == "start":
                state = "started"
                print("Iniciando...")

        elif state == "started":

            if actions["1"] == "register": equation += f"{int(to_binary(fingers_raised['0']),2)}"

            if actions["1"] == "register_negative": equation += f"-{int(to_binary(fingers_raised['0']),2)}"

            if actions["1"] == "add" :  equation += f" + "

            if actions["1"] == "sub" :  equation += f" - "

            if actions["1"] == "div" :  equation += f" / "

            if actions["1"] == "mul" :  equation += f" * "

            if actions["1"] == "parens_open" :  equation += f"("

            if actions["1"] == "parens_close" :  equation += f") "

            if actions["1"] == "decimal" :  equation += f"."

            if actions["1"] == "out" :  historic.append(equation)

            if actions["1"] == "erase" : equation = equation[:-1]

            if actions["two_handed"] == "end":
                state = "ended"
                print("Terminando...")

        elif state == "ended":

            equation = ""
            print("Aguardando novo comando...")
            state = "waiting"


        print(equation)

        print()

        for i in historic: print(eval(i))

        counter = 0

    cv2.imshow('Imagem', img)
    key = cv2.waitKey(int(1000 / 60))
    if key & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()