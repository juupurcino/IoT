import cv2
import os
import numpy as np

# Carregar o classificador Haar para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializar o modelo LBPH para reconhecimento facial
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Carregar imagens de rostos e os IDs correspondentes
faces = []
ids = []

# Percorrer o diretório "dataset" e carregar as imagens
for root, dirs, files in os.walk("dataset"):
    for file in files:
        if file.endswith('.jpg'):
            caminho_imagem = os.path.join(root, file)
            # Ler a imagem e converter para escala de cinza
            imagem = cv2.imread(caminho_imagem)
            gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

            # Detectar rostos na imagem
            faces_detectadas = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Extrair os rostos detectados e associar ao ID
            for (x, y, w, h) in faces_detectadas:
                rosto = gray[y:y + h, x:x + w]
                faces.append(rosto)
                # Extrair o ID da pessoa do nome do arquivo
                id = int(file.split('_')[1])  # O ID é extraído do nome do arquivo (ex: usuario_1_0.jpg -> ID = 1)
                ids.append(id)

# Treinar o modelo com as imagens
recognizer.train(faces, np.array(ids))

# Salvar o modelo treinado
recognizer.save('modelo_face.yml')
print("Modelo treinado e salvo com sucesso!")
