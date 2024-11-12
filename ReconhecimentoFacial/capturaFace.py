import cv2
import os

# Criar diretório para salvar as imagens do rosto
if not os.path.exists('dataset'):
    os.mkdir('dataset')

# Carregar o classificador Haar para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializar a captura de vídeo (usando a webcam)
cap = cv2.VideoCapture(0)

# Variáveis para cadastro
id_pessoa = input("Digite o ID da pessoa (um número único): ")
count = 0

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

        # Salvar a imagem do rosto em um diretório
        cv2.imwrite(f"dataset/usuario_{id_pessoa}_{count}.jpg", rosto)

        count += 1

    # Exibir o vídeo com a detecção de rosto
    cv2.imshow("Cadastro de Rosto", frame)

    # Encerra o cadastro após 30 imagens ou tecla 'q'
    if count >= 30:
        print(f"Cadastro do rosto {id_pessoa} concluído!")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Finalizar a captura de vídeo e fechar a janela
cap.release()
cv2.destroyAllWindows()
