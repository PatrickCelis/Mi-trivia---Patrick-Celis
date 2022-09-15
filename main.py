# Primeramente se importan las librerás random y time.
import random
import time

# Nuestra variable denominada "puntaje" es de 0 a 50 aleatoriamente.
puntaje = random.randint(0, 50)

# La variables comienza en True.
iniciar_trivia = True
ruleta_trivia = True

# La variable "intentos" almacenará cuantas veces el usuario quiere completar la trivia.
intentos = 0

# Coloco una bienvenida a mi trivia.
print ("Bienvenido/a a mi trivia sobre cultura general actual, las preguntas a tratar serán sobre tecnología y empresas.\n")

# Se espera 5 segundos antes de empezar.
time.sleep(5)

# Preguntaremos el nombre del participante y almacenamos el nombre en una variable.

nombre = input("Ingresa tu nombre: ")
print ("\n\033[34mHola 👋", nombre,"\033[39m")

# Para que el publico pueda entender debemos dar instrucciones sobre la funciones de nuestra trivia:
print ("Responde estas preguntas escribiendo la letra que sea tu alternativa, luego presiona 'Enter' en tu teclado para procesar tu respuesta.\n")

# Mostramos nuestro sistema de puntuación.
print("\033[33mMientras más respuestas aciertes más será tu puntaje. 😎")
print("Tienes: ", puntaje, "puntos\n")
print ("Tómate tu tiempo para responder y mucha suerte. 😀\033[39m\n")

# Mientras "trivia" sea True, se repetirá:
while iniciar_trivia == True:
 intentos += 1 
 
  # Se coloca el números e intentos.  
 print("\n\033[35m Intento número:", intentos,"\033[39m")

  # Se espera 5 segundos antes de empezar las preguntas.
 time.sleep(5)

  # Pregunta 1. 
 print ("\033[36m1. ¿Cuál de estas empresas no corresponden al empresario Elon Musk?\033[39m")
 print ("a) Tesla")
 print ("b) Neuralink")
 print ("c) Microsoft")
 print ("d) SpaceX")

  # Almacenamos la respuesta del usuario en la variable "respuesta_1".
 respuesta_1 = input("\nTu respuesta: ") 

 while respuesta_1 not in ("a", "b", "c", "d", "silabuz"):
  respuesta_1 = input("Esa no es una alternativa 🤔")

# Vamos a verificar las respuestas e interactuar con el ususario mostrandole si su respuesta es correcta o incorrecta.
 if respuesta_1 == "a":
  print("\033[31m La respuesta no es correcta. 😔", nombre, "sigue intentándolo.\033[39m")
  puntaje = puntaje - 20
 elif respuesta_1 == "b":
  print("\033[31m La respuesta es incorrecta. 😥", nombre, "prueba otra vez.\033[39m")
  puntaje = puntaje - 20
 elif respuesta_1 == "c":
  print("\033[32m Bien!", nombre, "La respuesta es correcta. 😀🎉\033[39m") 
  puntaje += 50
 elif respuesta_1 == "silabuz":   
  print("Parece que encontraste un secreto. 😮", nombre, "Mira esto! https://youtu.be/dQw4w9WgXcQ")
 elif respuesta_1 == "d":
  print("\033[31m Noooo, esa no es la respuesta. 😨", nombre, "sigue intentándolo.\033[39m")
  puntaje = puntaje - 20

  # Al final de cada pregunta mostramos el puntaje actual.
 print ("Tu puntaje actual es de", puntaje, "puntos.\n")

  # Se espera 3 segundos para pasar a la siguiente pregunta.
 time.sleep(3)

  # Pregunta 2
 print("\033[36m2. ¿Qué empresa desarrolló la serie de consolas de videojuegos llamada PlayStation?\033[39m")
 print ("a) Sony")
 print ("b) Apple")
 print ("c) Amazon")
 print ("d) Google")

# Almacenamos la respuesta del usuario en la variable "respuesta_2".
 respuesta_2 = input("\nTu respuesta: ") 

 while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input("Esa no es una alternativa 🤔")

# Vamos a verificar las respuestas e interactuar con el ususario mostrandole si su respuesta es correcta o incorrecta.
 if respuesta_2 == "a":
  print("\033[32m Muy bien!", nombre, "La respuesta es correcta. 😜👌\033[39m")
  puntaje += 50
 elif respuesta_2 == "b":
  print("\033[31m La respuesta es incorrecta. 😥", nombre, "prueba otra vez.\033[39m")
  puntaje = puntaje - 20
 elif respuesta_2 == "c":
  print("\033[31m Que mal, no es la respuesta. 😧", nombre, "inténtalo de nuevo.\033[39m")
  puntaje = puntaje - 20
 elif respuesta_2 =="d":
  print("\033[31m Noooo, esa no es la respuesta. 😨", nombre, "sigue intentándolo.\033[39m")
  puntaje = puntaje - 20

  # Al final de cada pregunta mostramos el puntaje actual.
 print ("Tu puntaje actual es de", puntaje, "puntos.\n")

  # Se espera 3 segundos para pasar a la siguiente pregunta.
 time.sleep(3)

  # Pregunta 3
 print ("\033[36m3. ¿A que nombre pasó a llamarse la compañía Facebook?\033[39m")
 print ("a) Instagram")
 print ("b) Meta")
 print ("c) Netflix")
 print ("d) Reddit")

# Almacenamos la respuesta del usuario en la variable "respuesta_3".
 respuesta_3 = input("\nTu respuesta: ") 

 while respuesta_3 not in ("a", "b", "c", "d"):
  respuesta_3 = input("Esa no es una alternativa 🤔")

# Vamos a verificar las respuestas e interactuar con el ususario mostrandole si su respuesta es correcta o incorrecta.
 if respuesta_3 == "a":
  print("\033[31m Mmmmm... puede ser, No! La respuesta es incorrecta. 😬 ", nombre, "prueba otra vez. \033[39m")
  puntaje = puntaje - 20
 elif respuesta_3 == "b":
  print("\033[32m Ok!", nombre, "La respuesta es correcta. 🤗🎉\033[39m")
  puntaje += 50
 elif respuesta_3 == "c":
  print("\033[31m La respuesta es incorrecta. 😞", nombre, "inténtalo de nuevo.\033[39m")
  puntaje = puntaje - 20
 elif respuesta_3 =="d":
  print("\033[31m Oh no, es la respuesta equivocada. 😭", nombre, "sigue intentándolo.\033[39m")
  puntaje = puntaje - 20

  # Al final de cada pregunta mostramos el puntaje actual.
 print ("Tu puntaje actual es de", puntaje, "puntos.\n")

  # Se espera 3 segundos para pasar a la siguiente pregunta.
 time.sleep(3)

  # Pregunta 4
 print ("\033[36m4. ¿Quien es el propietario y fundador de Amazon?\033[39m")
 print ("a) Larry Page")
 print ("b) David Baszucki")
 print ("c) Mark Zuckerberg")
 print ("d) Jeff Bezos")

# Almacenamos la respuesta del usuario en la variable "respuesta_4".
 respuesta_4 = input("\nTu respuesta: ") 

 while respuesta_4 not in ("a", "b", "c", "d"):
  respuesta_4 = input("Esa no es una alternativa 🤔")

# Vamos a verificar las respuestas e interactuar con el ususario mostrandole si su respuesta es correcta o incorrecta.
 if respuesta_4 == "a":
  print("\033[31m Respuesta incorrecta. 🤨", nombre, "prueba otra vez. \033[39m")
  puntaje = puntaje - 20
 elif respuesta_4 == "b":
  print("\033[31m No! Te has equivocado de respuesta. 😴", nombre, "sigue intentándolo.\033[39m")
  puntaje = puntaje - 20
 elif respuesta_4 == "c":
  print("\033[31m Que mal, no es la respuesta. 😣", nombre, "inténtalo de nuevo.\033[39m")
  puntaje = puntaje - 20
 elif respuesta_4 =="d":
  print("\033[32m Correcto!", nombre, "Has elegido bien la respuesta. 😉👍\033[39m")
  puntaje += 50

  # Al final de cada pregunta mostramos el puntaje actual.
 print ("Tu puntaje actual es de", puntaje, "puntos.\n")

  # Se espera 3 segundos para pasar a la última pregunta.
 time.sleep(3)

  # Pregunta 5
 print ("\033[36m5. ¿Cuál de estos productos/programas no son de Adobe?\033[39m")
 print ("a) Acrobat")
 print ("b) CorelDRAW")
 print ("c) Photoshop")
 print ("d) Illustrator")

# Almacenamos la respuesta del usuario en la variable "respuesta_5".
 respuesta_5 = input("\nTu respuesta: ") 

 while respuesta_5 not in ("a", "b", "c", "d"):
  respuesta_5 = input("Esa no es una alternativa 🤔")

# Vamos a verificar las respuestas e interactuar con el ususario mostrandole si su respuesta es correcta o incorrecta.
 if respuesta_5 == "a":
  print("\033[31m Claro que no, esa no es la respuesta. 😂 ", nombre, "prueba otra vez. \033[39m")
  puntaje = puntaje - 20
 elif respuesta_5 == "b":
  print("\033[32m Buena!", nombre, "Tu respuesta es la correcta. 😎🎉\033[39m")
  puntaje += 50
 elif respuesta_5 == "c":
  print("\033[31m Te equivocaste pero no te rindas. 🙂", nombre, "intenta de nuevo. \033[39m")
  puntaje = puntaje - 20
 elif respuesta_5 =="d":
  print("\033[31m Yyyy la respuesta es... incorrecta. 🙄", nombre, "sigue intentándolo.\033[39m")
  puntaje = puntaje - 20

  # Al final de cada pregunta mostramos el puntaje actual.
 print ("Tu puntaje final es de", puntaje, "puntos.\n")
  
  # Se espera 3 segundos más para entrar a la ruleta de puntos.
 time.sleep(3)

  
    # Se pregunta si se desea iniciar con la ruleta de puntos.
 print("\n\033[35m¿Quieres iniciar una ruleta de puntos? Te sumará unos cuantos puntos a tu puntaje final. 😎\033[39m\n")
 ruleta_trivia = input("Ingresa 'ok' para jugar la ruleta de puntos, o cualquier tecla para continuar: ").lower()

 if ruleta_trivia == "ok":
   puntaje = (puntaje + random.randint(0, 50))
 elif ruleta_trivia != "ok":  
   print("\nBien", nombre,"!")
   ruleta_trivia = False  
  
   # Se muestra el puntaje si el usuario accede a la ruleta.
 print ("\033[33mTu puntaje final es de", puntaje, "puntos.\033[39m\n")

  #Preguntamos al usuario si quiere intentar la trivia otra vez.
 print("\n¿Quieres intentar la trivia nuevamente?🤔")
 repetir_trivia = input("Escribe 'si' para repetir la trivia, o cualquier otra tecla para finalizar: ").lower()

  # Si el usuario responde "si" la trivia empezará otra vez y si así es el caso comenzará con puntos aleatorios otra vez.
 if repetir_trivia == "si":
  puntaje = random.randint(0, 50)
 elif repetir_trivia != "si":  
  print("\n\033[35mMuchas gracias!", nombre,"espero que te hayas divertido completando esta trivia, hasta luego! 👋😀\033[39m\n")
  iniciar_trivia = False  
# Se cambia el valor de "iniciar_trivia" a False para evitar que se repita.
 # Trivia elaborada por : Jean Patrick Pisconte Celis - 2022