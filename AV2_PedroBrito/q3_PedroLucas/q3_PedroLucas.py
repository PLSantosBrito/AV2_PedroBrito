import cv2

ajustaBrilho = lambda img, value : cv2.convertScaleAbs(img, alpha = 1, beta = value)
mensagem_erro = lambda: print("\n\nERROR\n\n")

#Caminho da imagem
img = cv2.imread("q3_PedroLucas\imagem.jpg")

valor_brilho = float(input("Digite um valor entre -150 e 150 (0 = imagem sem alterações)"))

imagem_ajustada = ajustaBrilho(img, valor_brilho)
title = "Imagem Ajustada, Brilho = " + str(valor_brilho)
cv2.imshow(title, imagem_ajustada)
 

cv2.waitKey(0) 
cv2.destroyAllWindows()
