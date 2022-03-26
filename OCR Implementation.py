# -*- coding: utf-8 -*-
"""
@author: oramonviana
"""

##### PASSO 01: Instalar Libraries

from PIL import Image
import pytesseract
import cv2


##### PASSO 02: Carregar imagem para OCR

# Declarar o caminho do Executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\oramonviana\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

# Carregar a imagem de exemplo e converter para Grayscale (Escala de Cinza)
image_to_ocr = cv2.imread("testing\\fox_sample1.png")


##### PASSO 03: Fazer o Pre-processamento da Imagem

### Pre Processamento 01: Converter para Escala de Cinza (GrayScale)
preprocessed_img = cv2.cvtColor(image_to_ocr, cv2.COLOR_BGR2GRAY)

### Pre Processamento 02: fazer o Binario e Otsu Thresholding
preprocessed_img = cv2.threshold(preprocessed_img, 0, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)[1]

## OBS_01: Thresholding significa que a imagem em escala de cinza será composta por diferentes intensidades de cinza. A escala
## de cinza irá de 0 para 255. Enquanto fazemos Thresholding, especificamente o binario e o OTSU. Iremos converter a imagem
## em outro formato onde teremos apenas 2 cores. Duas solidas cores: Ou os Pixels serão Brancos ou os Pixels serão Pretos.

## OBS_02: cv2.threshold irá retornar uma tupla com 2 valores: threshold value e resulting image. Para evitar possiveis erros
## sempre que precisemos apenas dos resultados da imagem, é preciso colocar cv2.threshold(...)[1]

### Pre Processamento 03: Median Blur para remover ruido da imagem
preprocessed_img = cv2.medianBlur(preprocessed_img, 3)


#### PASSO 04: Fazer o Pre-processamento da Imagem:
cv2.imwrite('testing\\imagem_tratada_01.png', preprocessed_img)
   
imagem = Image.open('testing\\imagem_tratada_01.png')    
imagem = imagem.convert("L") # Transformando em tons de cinza novamente para assegurar esta transformaçao
imagem2 = Image.new("L", imagem.size, 255) # Fazer uma copia dessa imagem com fundo branco

for x in range(imagem.size[1]):
        for y in range(imagem.size[0]):
            cor_pixel = imagem.getpixel((y, x))
            if cor_pixel < 115:
                imagem2.putpixel((y, x), 0)

imagem2.save('testing\\imagemfinal2.png')

#### PASSO 05: Fazer OCR da Imagem

# Fazer OCR usando tesseract
text_extracted = pytesseract.image_to_string(Image.open('testing\\imagemfinal2.png'))

# Printar o texto extraido
print(text_extracted)



