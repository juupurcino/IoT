import cv2

# Carregar o classificador Haar para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Carregar o modelo treinado
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('modelo_face.yml')

# Inicializar a captura de vídeo
cap = cv2.VideoCapture(0)

while True:
    # Captura frame por frame
    ret, frame = cap.read()
    if not ret:
        break

    # Converter para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Desenhar um retângulo ao redor do rosto detectado
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Extrair a região do rosto
        rosto = gray[y:y + h, x:x + w]

        # Reconhecer o rosto
        id_pessoa, confianca = recognizer.predict(rosto)

        # Exibir o ID da pessoa reconhecida
        cv2.putText(frame, f"ID: {id_pessoa}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Exibir o vídeo com a detecção e reconhecimento de rosto
    cv2.imshow("Reconhecimento Facial", frame)

    # Finalizar ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Finalizar a captura de vídeo e fechar a janela
cap.release()
cv2.destroyAllWindows()
