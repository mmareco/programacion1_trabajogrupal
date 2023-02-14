
import time
import colorama
from colorama import Fore, Style, init
init(autoreset= True)

# ---------------------------- FUNCIONES ----------------------------
# -------------------------------------------------------------------

# ---------------------------- GRAFICOS -----------------------------
def graficos_inicio():
    print('''
                               ▖▖                                                 
                              ▖▚▐▐▚▘                                                   
                            ▖▞▐▐▐▐▐▝                         
                            ▖▞▐▞▜▜▟▐▐▘                        
                          ▖▝▖▄▟▟▄▄▚▘▌▘                       
                          ▄▟█████████▄▛                       
                        ▟████████████▛▙                      
                          ▚▛██████████▜▜                      
                      ▗▗▖▌▛█▜███████▛▛▙▚▄▗                   
                      ▞▞▟▞▞▙▞███████▜▛█▙▙▜▄▚▖                 
                    ▗▚▚▞█▟▐▙▚▚▚█▟▛▙▛▜▞▞█▌█▚▚▚▖                
                  ▞▟▞▌▌█▟▚▙▜▞▞▞▛█▌▛▙▜▞██▛▌▛▌▛▞               
                  ▙▜▟▝▀▘▀▀▘▀▘▘▘▀▝▘▘▀▝▀▀▘▘▀▟▙█▛▛▜              
                ▖▙▚█▟▖▖▝▗▗▗▗▝▗▘▝▖▘▘▞▗▗▗▝▝▖▞█▙█▜▚▛▌            
              ▗▟▟▟▜▟▜ ▖▘▖▗ ▖▝▗▝▖▖▘▘▖▖▖▖▘▘▖▜█▛▛▛▙▜▐▘           
            ▄▙▚▟▟█▟█▘▗▗ ▘▖▝▝▖▖▄▝▞▝▖▖▖▖▘▘▖█▖████▞▛▛▙          
            ▞▟▞▚▀▌█▜▞ ▘▗▝▖▝▞▐▗▚▖▌▞▞▖▞▗▝▝▝▗▟▌▀█▜▛▛▚▚▚█▚        
          ▗▛▌▟▝▞▞▞▀▖▝▝▗▗▝▞▐▐▐▖▌▙▚▚▚▞▞▐▝▞▗▝▚▖▖▌▌▜▐▞▙▜▌        
          ▐▙▛▙▜▐▟▙▗ ▝▝▖▚▚▚▙▙▙▜▜▞▙▜▞▟▐▖▌▞▗ ▘▐▜▟▞▙▙▛▛▙█        
        ▗▝▗▘▀▀▀▌▛▟▚▙▘▚▟▟▞▙▙▚▙▜▟▟▚█▟▚▙▙▚▞▗▟▞▟▜▚▜▀▀▀▀▚▘▚▝      
          ▝ ▝▝▝  ▝   ▀▘▘▘▀▀▟███▙██▙██▘▀▀▀▘    ▘ ▘▝ ▝ ▝        '
            ''') 
    print('''
   ▗▄  ▗▄▖  ▄▖ ▄▖   ▗▄ ▗▄▄▄▄▄▄▖    ▄▄▄▄▄▄▄ ▄▄▖   ▄▄▖    ▄▖  
   ▐█▖ ██▙ ▐█▘ █▌   ▝█▖▐█▝▝▝▝█▌    █▌▘▘▘▜█▘▟██▄ ▟██▘   ▗█▌  
    ▜▙▐█▝█▌█▛  ███████ ▐█    █▌    █▙▄▄▄▟█▘▟█▝██▛▗█▌    █▌  
     ██▌ ▐██   █▌   ▐█▘▐█▗▗▗ █▌    █▌▘▘▝▐█▌▟█  ▀  █▖   ▝█▘  
     ▝▀   ▀▘   ▀▘    ▀ ▝▀▀▀▀▀▀▘    ▀▘   ▝▀ ▝▀     ▀▘    ▀▘  
        ''') 

def graficos_fallo():
    print('''                                                                                                                         
                        ▄▄▟█████▙▄▄                         
    ▗ ▘  ▘  ▘  ▘ ▝ ▗▐▄███████████████▄▌ ▝  ▝  ▝  ▘  ▘  ▘ ▝  
  ▝              ▗▟█████████████████████▄▖                  
        ▖ ▗  ▖  ▄█████████████████████████▄  ▖ ▗  ▗  ▗  ▖   
   ▗  ▗        ████████████████████████████▙        ▗       
  ▝          ▗██████████████████████████████▙             ▗ 
          ▖ ▘▐████████████████████████████████▖ ▖▘      ▖▝  
      ▖▝     ▐█████████████████████████████████    ▘  ▗     
  ▗▝         ▐█████████████████████████████████      ▗      
         ▗  ▖▐█████████████████████████████████             
       ▗     ██████▛▀▀▀▀█████████████▜▀▜██████▛   ▗     ▗   
   ▗  ▝      █████▘      ▝▀██████▀▘      ▝████▛     ▝  ▖    
  ▘        ▗ █████       ▗▟██████▙▖       ▐████             
          ▖  █████▄▄▄▄▄▟████████████▄▄▖  ▄▟████  ▝        ▘ 
     ▝  ▘    ▐█████████████████████████████████     ▖▘  ▝   
  ▗ ▗        ▐████████████████████████████████▌   ▗         
         ▖  ▖ ████████████████████████████████▌  ▘     ▝    
       ▝      ▜███████████████████████████████              
  ▗  ▗         ████████████▀▘ ▝▀▜████████████▛       ▗▝   ▘ 
    ▝      ▘   ▜██████████▘      ▝▜██████████▘  ▘ ▝         
         ▘   ▗  ▜█████████▖       ▐█████████▛       ▝    ▝  
  ▝     ▘       ▝██████████▙▄▄▙▄▄▟██████████▘    ▗          
     ▖       ▖   ▜█████████████████████████▌   ▝        ▘   
   ▗       ▝   ▗ ▐████████████████████████▛   ▗     ▘ ▝   ▖ 
  ▝    ▝  ▘     ▗████████████████████████▛        ▗         
               ▐██████████████████████████       ▝      ▗   
      ▗ ▘   ▗▝ ▜██████████████████████████   ▘  ▘    ▝      
  ▗▝       ▝   ▐██████████████████████████              ▖   
               ▟██████████████████████████▘   ▖     ▖ ▗     
       ▖  ▘   ▐███████████████████████████▌ ▝   ▖ ▘       ▗ 
   ▖  ▘     ▗ ▀███████████████████████████▌              ▗  
  ▘      ▗     ▝██████████████████████████▘         ▗ ▗ ▝   
                 ▝▀▜████████████████████▛▘   ▗▝  ▝          
     ▝  ▘  ▗ ▝       ▝▀▀▜▜██████████▀▀▀                     
    ▗                                             ▗ ▘   ▖   
   ▘                                             ▘    ▝          
    ''')  


def graficos_ganar():
    print('''                                                          
           ▗▗ ▖▖   ▖▗▗   ▖▖▗▗ ▖▖▗  ▖▖▗   ▗▗ ▖▖            
          ▝▚    ▌ ▐▖  ▐▗▌        ▌▜  ▐  ▝▌   ▐            
           ▝▖   ▌ ▞  ▖▌ ▌        ▌▛  ▐  ▝▖   ▜            
            ▐▌  ▛ ▌ ▗▀ ▗▌  ▄▄▄▖  ▌▜   ▙  ▐   ▟            
             ▝▖ ▝▀  ▞   ▌  ▌  ▐  ▌ ▌  ▙  ▐    ▌           
              ▌    ▜    ▌  ▌  ▐  ▌▝▌  ▙  ▜    ▙           
              ▌   ▞▘   ▞▘ ▗▘  ▀▖ ▚▞▌  ▙  ▐    ▌           
             ▗▘   ▌    ▛  ▐    ▌ ▐▗▌  ▗▌  ▛   ▌           
             ▐   ▞▘    ▛  ▐    ▌ ▐▖▚   ▌  ▛   ▜           
            ▝▌   ▟     ▜   ▀▀▀▀  ▐ ▐▖  ▝▀▀▀   ▐▘          
            ▞▘  ▗▞     ▛         ▐▖▐▖         ▐▖          
            ▙▄▄▄▞▖      ▚▄▄▄▄▄▄▄▄▘  ▝▄▄▄▄▄▄▄▄▝▘           
         ▞▝▝▝▗    ▖▘▘▘▚▖▞ ▝ ▘▝▝▝▝▖▟▝▘▘▝ ▘▄ ▗▝▀▐▖          
        ▝▌   ▐    ▌   ▐▖▌        ▌▟      ▝▖▐  ▐           
        ▙▘  ▗▞    ▌  ▝▌ ▝▝▐▖  ▜▝▝ ▟       ▐█   ▜          
        ▙   ▝▌▗▝▖▟   ▝▌   ▐   ▐    ▌       ▝   ▜          
        ▙   ▝▙▘ ▐█   ▛    ▐   ▜    ▌           ▟          
       ▗▘            ▛   ▗▞   ▝▖  ▗▌   ▗▄      ▝▖         
       ▐            ▗▀   ▗▌    ▌   ▌   ▐▚▘      ▌         
       ▐      ▞▛▖   ▐   ▖▄▌    ▙▗  ▌    ▌▀▖     ▌         
       ▌     ▐  ▜▘  ▐  ▙         ▐▘▐▘   ▛ ▚▖    ▚▖        
       ▚▝▖▄▗▝▘  ▝▚▗▗▘  ▚▗▗▗▖▞▖▚▗▘▞▘▝▚▗▖▖▌  ▚▗▖▖▚▐                
       ''') 
    print('''
            ▖     ▗▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▖       ▖     ▖ 
  ▗ ▗▝ ▝ ▝    ▖▘ ▘▜███████████████████████▘   ▖▘ ▘ ▘   ▘ ▘  
 ▝          ▖ ▄▄▄ ▜███████████████████████▖▗▄▄        ▖     
         ▖ ▘▄████▌▜███████████████████████▗████▙▖▗       ▖  
     ▖▝    ▐██▛   ▐███████████████████████   ▜███   ▘  ▖▘   
 ▗▝      ▖ ███▌   ▐███████████████████████    ███▖    ▘     
        ▖  ███▌ ▖ ▐███████████████████████▝   ███▘  ▖       
     ▘ ▘   ▜██▙▘  ▐██████████████████████▛  ▗▐███▘    ▗   ▖ 
  ▗▝       ▝███▙   ██████████████████████▌  ▄███▌   ▖▝      
       ▖ ▗  ▝▜████▙▜█████████████████████▗█████▀   ▘     ▘  
 ▗    ▘        ▀▀▀▀ ▜███████████████████▘▝▀▀▀▘              
    ▝      ▗         ▜█████████████████▘         ▗▝  ▗  ▘ ▝ 
    ▖   ▗ ▘   ▗ ▗     ▜██████████████▛▘ ▝ ▗ ▝ ▗ ▝           
  ▖▘  ▗▝     ▝    ▗▝   ▝▜███████████▛ ▗▝            ▗ ▗▝ ▝  
            ▖            ▀████████▛▘        ▗   ▗           
           ▖   ▗ ▘   ▝ ▗   ▀████▛▘       ▗ ▘   ▘   ▝        
  ▘ ▝ ▝  ▖▘   ▝    ▗▝    ▗  ▝██▛     ▖▝           ▝  ▗▝  ▖▘ 
             ▗             ▗▐███  ▝      ▖   ▖▘  ▖          
  ▖ ▖ ▖ ▖         ▝    ▖▘   ▟███    ▗   ▖   ▘       ▖       
          ▗ ▗   ▖▘    ▖   ▗ ████▌ ▖▝   ▘        ▖ ▖▘  ▗▝ ▝  
  ▗   ▗        ▘    ▖▘     ▐█████          ▘  ▗             
     ▘   ▝   ▗           ▗ ██████▌     ▖ ▗   ▝              
 ▗ ▗    ▝  ▗▝    ▗▝▄▄▄▄▄▟▄▟███████▄▄▟▄▄▄▄▖  ▘    ▖▘  ▖▘ ▝ ▝ 
       ▖        ▝ ▐█████▀▀▀▀▀▀▀▀▀▀▀▀▜█████     ▗            
    ▗ ▘   ▖       ▐█████            ▟█████▗ ▖ ▝     ▖   ▖ ▖ 
  ▖▘        ▗  ▘  ▐█████▄▄▄▄▄▄▄▄▄▄▄▄▟█████        ▗    ▘    
        ▖▘ ▝     ▘▐███████████████████████    ▖ ▗▝   ▝      
     ▗         ▝   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▘ ▗ ▘           ▖  
        ''') 

def graficos_perder():
    print('''                                                             
          ▖▖▖▖▖     ▗▄▄▄▄     ▄▄▄▖     ▄▙▟▖ ▙███████████▖   
      ▟████████▘   ▄██▀▜█▙▄   ▟███▄▖ ▗▄███▌ ███▌            
    ▐███▘         ███▀ ▝▀██▙▄ ▟████▙▄█████▙ ███▌            
   ███▌         ▐███     ▐███ ▟███████████▙ ███▙▄▄▄▄▙▙▌     
   ███▌   ▜████▌▐███▌    ▐███ ▐███▛██▛▜▜██▙ ███▛▀▀▀▀▀▀▘     
   ███▌    ▝███▌▗████████████▘▐███ ▝▀▘ ▐███ ███▛            
   ▝▜██▙▖   ███▌ ███▌    ▐███▖▜███     ▜███ ▟███▄▄▄▄▄▄▄▄▖   
     ▀▜████████▌ ███▌    ▐███▖▐███     ▐▛▛▀ ▀▀▀▀▀▀▀▀▀▀▀▀▘   
       ▀▘▀▝▀▝▘▘                                             
                          ▄▄▄▖ ▄▄▄▄▄▄▄▄▄▄▄▄ ▗▄▄▄▟▟▟▙██▙     
     █████████   ███▌     ███▖▐███▛▀▀▀▀▀▀▀▀ ▟███▀▀▀▀▀██▙▌   
   ▗███     ████ ███▙     ███▌▐███▌         ▐███     ▟███   
   ▐███     ▟███ ███▙     ███▌▐███▌ ▗▗▗▗▄   ▐███   ▗▄███▙   
   ▐███     ▟███ ▟████▖ ▟████▌▐██████████▘  ▐███▙▄▄▟█▛▀▀▀   
   ▐███     ▐███  ▀█████████  ▗███▌         ▐███▛████▙▄     
   ▐███     ▟███   ▝▝█████▘    ███▌         ▐███▖ ▜████▙▗   
   ▝▀██▄▄▄▄▄▟█▛▀     ▀▜█▛▘    ▝████████████▌▐███    ▛▜▀▀▀   
     ▝▀▀▀▀▀▀▀▀▘       ▝▀                                    
     ''') 

# ----------------------------- RANDOM ------------------------------
def randoms(N, a, b, seed = time.gmtime(), integer = True):
    # Se le declara un numero a seed (en este caso elegimos 1234 pero podrían ser otras combinaciones), y la funcion devuelve n PRNG entre 'a' y 'b'
    rands=[]
    if integer:
        for i in range(N):
            num = int(a+(b-a)*(abs(hash(str(hash(str(seed)+str(i+1)))))%10**13)/10**13)
            rands.append(num)
        return rands
    else:
        for i in range(N):
            num = a+(b-a)*(abs(hash(str(hash(str(seed)+str(i+1)))))%10**13)/10**13
            rands.append(num)
        return rands

# -------------------------- MOSTRAR TEXTO --------------------------
def mostrar_texto(lore):
    for palabra in lore:
        print(palabra,end="")
        time.sleep(0.005)

# ---------------------------- HISTORIA -----------------------------
def dialogo_uno():
    error_mal = False
    try: 
        respuesta_uno = int(input(''' ES TU TURNO DE RESPONDER. ELIGE UNA OPCIÓN:
        1 = Muchas gracias por presentarnos, estamos seguros que esta noche les mostraremos al público y la comunidad quienes serán los nuevos lideres.
        2 = Buenas noches. Esto será muy divertido, que gane el mejor, no? 
        >>> '''))
        while (respuesta_uno != 1) and (respuesta_uno != 2):
            respuesta_uno = int(input("Ingrese 1 o 2 >>> "))
        if respuesta_uno == "1":
            texto1= '''Moderador:
    "Me encanta esa seguridad. Bien dicho CLAY. Empecemos." 
    '''
            mostrar_texto(texto1)
        else:
            texto2 = '''FR13NDS:
    "Jajaja! Exacto, nosotros." 
Moderador:
    "Empecemos"
    '''
            mostrar_texto(texto2)
    except ValueError:
        error_mal = True
        print('VALOR INGRESADO INVALIDO')
    return error_mal

def dialogo_dos():
    error_mal = False
    try: 
        texto3='''Moderador:
        "Están listos para la final? FR13NDS?"

        FR13NDS:
        "Por supuesto."

        Moderador:
        "CLAY?"
        '''
        mostrar_texto(texto3)
        respuesta_uno = int(input(''' ES TU TURNO DE RESPONDER. ELIGE UNA OPCIÓN:
        1 = Si.
        2 = No. 
        >>> '''))
        while (respuesta_uno != 1) and (respuesta_uno != 2):
            respuesta_uno = int(input("Ingrese 1 o 2 >>> "))
        if respuesta_uno == "1":
            print('''*JUEGO FINAL
    ''')
        else:
            texto4 ='''Moderador:
    "Bueno, aunque no quieras debes. Son las reglas
    '''
            mostrar_texto(texto4)
    except ValueError:
        error_mal = True
        print('VALOR INGRESADO INVALIDO')
    return error_mal

def acertijo_uno():
    try: 
        respuesta_uno = input('\nUSTED HA RECIBIDO UN ARCHIVO, DESEA ABRIRLO? PRESIONE CUALQUIER NUMERO O LETRA >>> ')
        arch = open("unoacertijo.txt", "r", encoding='UTF-8')
        linea = arch.readline( )
        while linea:
            print(linea)
            linea = arch.readline( )
        opcion = int(input("Escriba la opción que elige >>> "))
        while (1>opcion>4):
            opcion = int(input("Escriba la opción que elige. 1, 2, 3 o 4? >>> "))
        if opcion == 2:
            print('Acertarste. Están salvadas.')
        else:
                acertijo_uno()
    except ValueError:
        print('VALOR INGRESADO INVALIDO')
        acertijo_uno()
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
        acertijo_uno()
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
        acertijo_uno()
    finally:
        try:
            arch.close()
        except NameError:
            pass

def acertijo_dos():
    try: 
        respuesta_uno = input('USTED HA RECIBIDO UN ARCHIVO, DESEA ABRIRLO? PRESIONE CUALQUIER NUMERO O LETRA >>> ')
        arch = open("dosacertijo.txt", "r", encoding="UTF-8")
        linea = arch.readline( )
        while linea:
            print(linea)
            linea = arch.readline( )
        opcion = int(input("Escriba la opción que elige >>> "))
        inicio = time.time()
        while (1>opcion>4):
            opcion = int(input("Escriba la opción que elige. 1, 2, 3 o 4? >>> "))
        if (opcion == 3) and ((time.time()-inicio) < 60):
            print('Acertarste. Una lastima, la cuidad se vería muy bella sin luz.')
        else:
                acertijo_dos()
    except ValueError:
        print('VALOR INGRESADO INVALIDO')
        acertijo_dos()
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
        acertijo_dos()
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
        acertijo_dos()
    finally:
        try:
            arch.close()
        except NameError:
            pass

#terminar
def acertijo_tres():
    try: 
        respuesta_uno = int(input('USTED HA RECIBIDO UN ARCHIVO, DESEA ABRIRLO? PRESIONE CUALQUIER NUMERO O LETRA >>> '))
        arch = open("tresacertijo.txt", "r", encoding='UTF-8' )
        linea = arch.readline( )
        while linea:
            print(linea)
            linea = arch.readline( )
        arch1 = open("password.txt", "w", encoding='UTF-8')
        contraseña = input("Escriba el numero que obtuvo con letras >>> ")
        arch1.write(contraseña)
    except ValueError:
        print('VALOR INGRESADO INVALIDO')
        acertijo_tres()
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
        acertijo_tres()
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
        acertijo_tres()
    except:
        print("VALOR INVALIDO")
        acertijo_tres()
    finally:
        try:
            arch.close()
            arch1.close()
        except NameError:
            pass

def verificacion_acertijo_tres():
    try: 
        arch = open("password.txt", "r", encoding='UTF-8')
        linea = arch.readline( )
        if linea == "quinientos dos":
            print("Ganaste")
        else: 
            print("Perdiste")
    except ValueError:
        print('VALOR INGRESADO INVALIDO')
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass

# --------------------------- MINIJUEGO 1 ---------------------------
#Funciones del minijuego1
def friends():
    randNum = randoms(3, 1, 3) 
    if randNum[0] == 1:
        computadora = 'v'
    elif randNum[1] == 2:
        computadora = 't'
    elif randNum[2] == 3:
        computadora = 'r'
    return computadora

def verificarDato(nosotros):
    while (nosotros != "v") and (nosotros != "t") and (nosotros!= "r"):
        print("Dato inválido.")
        print("Intente nuevamente.")
        nosotros = input('''Tu turno:
        Piedra=Virus(v), Papel=Troyano(t) o Tijeras=Rootkit(r)? Juega CLAY >>> ''')
    return nosotros

def ganar(computadora, nosotros):
    if computadora == nosotros:
        return None
    elif computadora == 'v':
        if nosotros=='t':
            return False
        elif nosotros=='r':
            return True   
    elif computadora == 't':
        if nosotros=='r':
            return False
        elif nosotros=='v':
            return True
    elif computadora == 'r':
        if nosotros=='v':
            return False
        elif nosotros=='t':
            return True

def resultado(a):
    ganador = 0
    if a == None:
        print("EMPATE!")
    elif a:
        print("FR13NDS GANA")
    else:
        print("CLAY GANA")
        ganador = 1
    return ganador

#Main del minijuego1
def main_minijuego1():
    texto5 = '''En este juego tendras que jugar Piedra-Papel-Tijeras pero con un giro de tuerca:
    Piedra = Virus(v)
    Papel = Troyano(t)
    Tijeras = Rootkit(r)
    
    Explicacion:
        Virus: tipo de malware que se adhiere a programas o archivos legítimos y se replica para 'infectar' la computadora e implementar la carga útil.
        Troyano: disfrazado como software legítimo, un troyano engaña al usuario para que lo ejecute y permita que se implemente la carga útil, que puede incluir una "puerta trasera" que un atacante puede usar para obtener acceso.
        Rootkit: conjunto de herramientas de software diseñado para permitir que un atacante obtenga acceso no autorizado, a menudo acceso elevado (por ejemplo, nivel de administrador), a una computadora sin ser detectado.
        '''
    mostrar_texto(texto5)  
    texto6 = '''
    Turno de FR13NDS:
    Piedra=Virus(v), Papel=Troyano(t) o Tijeras=Rootkit(r)? Juega FR13NDS
    FR13NDS ya eligió. 
    '''
    mostrar_texto(texto6)

    f = friends()

    c = input('''Tu turno:
    Piedra=Virus(v), Papel=Troyano(t) o Tijeras=Rootkit(r)? Juega CLAY >>> ''')
    c= verificarDato(c)

    juego = ganar(f, c)

    print(f"FR13NDS elige {f}")
    print(f"CLAY elige {c}")

    partidas_ganadas = resultado(juego)
    return partidas_ganadas

# --------------------------- MINIJUEGO 2 ---------------------------
#funciones mini2

def relleno_tablero(tab):
    tab[4][2]="⭧"

    tab[4][4]="⭦"

    tab[2][3]="⭣"
    tab[5][0]="⭣"
    tab[5][1]="⭣"
    tab[5][5]="⭣"
    tab[5][6]="⭣"

    tab[0][2]="⭢"
    tab[0][6]="⭢"
    tab[6][4]="⭢"
    tab[6][6]="⭢"

    tab[1][0]="⭡"
    tab[1][3]="⭡"
    tab[1][6]="⭡"
    tab[3][0]="⭡"
    tab[3][6]="⭡"

    tab[4][0]="⭥"
    tab[4][6]="⭥"
    

    tab[0][0]="⭠"
    tab[0][4]="⭠"
    tab[6][0]="⭠"
    tab[6][2]="⭠"

    tab[0][1]="⭤ "
    tab[0][5]="⭤ "
    tab[6][3]="⭤ "

    tab[0][3]="Ⓐ"
    tab[2][0]="🕵"
    tab[3][3]="Ⓒ"
    tab[2][6]="💾"
    tab[6][1]="Ⓔ"
    tab[6][5]="Ⓕ"

def impresion(tab,simbolos):
    print("\n")
    for fila in tab:
        print(f"".rjust(80),end=" ")
        for elemento in fila:
            if elemento in simbolos:
                print(f"{Fore.CYAN}{elemento}",end=" "*12)
                continue
            print(f"{Fore.MAGENTA}{elemento}",end=" "*12)
        print("\n\n")
    print("\n")

def busqueda(valor,tab):
    for i,fila in enumerate(tab):
        for j,elemento in enumerate(fila):
            if elemento==valor:
                return (i,j)  

def reemplazo(tab,dic_pos,dic_simbol,pos_futura,pos_animal,animal):
    fila,columna=busqueda(animal,tab)
    tab[fila][columna]=dic_simbol[pos_animal]

    dic_pos[pos_animal]=dic_simbol[pos_animal]

    fila,columna=busqueda(dic_pos[pos_futura],tab)
    tab[fila][columna]=animal

    dic_pos[pos_futura]=animal

def mov_raton(posibilidades,gato,raton):
    random_choice = randoms(2, 0, 1)
    casillas_inseguras=[]
    casillas_seguras=[]
    for casilla in posibilidades[raton]:
        seguridad=True
        if casilla==gato:
            continue
        for casilla_2 in posibilidades[casilla]:
            if gato==casilla_2:
                casillas_inseguras.append(casilla)
                seguridad=False
                break            
        if seguridad:
            casillas_seguras.append(casilla)    
    if len(casillas_seguras)!=0:
        a = random_choice[0]
        seguras = casillas_seguras[a]
        return (seguras)
    else:
        a = random_choice[0]
        inseguras = casillas_inseguras[a]
        return (inseguras)    

#Main mini2
def main_minijuego2():
    tablero=[[" "]*7 for i in range(7)]

    relleno_tablero(tablero)

    dic_posiciones={
    "A":tablero[0][3],
    "B":tablero[2][0],
    "C":tablero[3][3],
    "D":tablero[2][6],
    "E":tablero[6][1],
    "F":tablero[6][5]}

    dic_posibilidades={
    "A":["B","C","D"],
    "B":["A","E"],
    "C":["A","E","F"],
    "D":["A","F",],
    "E":["B","C","F"],
    "F":["E","C","D"]}

    dic_simbolos={
    "A":"Ⓐ",
    "B":"Ⓑ",
    "C":"Ⓒ",
    "D":"Ⓓ",
    "E":"Ⓔ",
    "F":"Ⓕ"}
    sim=("Ⓐ","Ⓑ","Ⓒ","Ⓓ","Ⓔ","Ⓕ")
    pos_gato="B"
    pos_raton="D"
    inicio=time.time()
    texto7="Tienes 60 segundos para recuperar el codigo antes de que perdamos la señal"
    print()
    mostrar_texto(texto7)
    time.sleep(1)
    perder_mini2 = False
    while True:

        impresion(tablero,sim)

        posicion_futura = input("Ingrese la vulnerabilidad por la que quiera acceder (A, B, C, D, E, F) >>> ").upper()  #Lo coloco en mayusculas para que no de error si el usuario ingresa minusculas

        if time.time()-inicio>=80:   #Verifica si supero el tiempo limite(en segundos) despues de que el usuario ingresa la posicion
            print("\n\n\n"+"PERDIMOS LA SEÑAL".center(235))
            perder_mini2 = True
            break

        while posicion_futura not in dic_posibilidades[pos_gato]:  # Verifica que el usuario haya ingresado una posicion que se ecuentre en el tablero y a la que pueda acceder

            posicion_futura=input("Ingrese el lugar valido >>> ").upper()

        reemplazo(tablero,dic_posiciones,dic_simbolos,posicion_futura,pos_gato,"🕵")

        pos_gato=posicion_futura #Actualiza la posicion del gato

        impresion(tablero,sim)

        if pos_gato==pos_raton:#Corrobora que siga vivo el raton
            print("\n\n\n"+"ESTAMOS DENTRO".center(235))
            break

        print("\n\n\n"+"Recibiendo señal del servidor...".center(235))

        time.sleep(1)#Retrasa el programa para dar la impresion de que el raton esta pensando

        movimiento_raton=mov_raton(dic_posibilidades,pos_gato,pos_raton) #ELIGE LA POSICION A DONDE VA A IR EL RATON  

        reemplazo(tablero,dic_posiciones,dic_simbolos,movimiento_raton,pos_raton,"💾") 

        pos_raton=movimiento_raton#Actualiza la posicion del gato
    return perder_mini2

# --------------------------- MINIJUEGO 3 ---------------------------
#Funciones mini3
def set_move(dic_col):

    while True:

        try:
            
            fila = int(input("\nIngrese la fila de la pieza que desea mover >>> ")) 
            assert 1<=fila<=8, "Recuerde que las coordenaadas de las filas van del '1' al '8'."
            
            columna = input("Ingrese la columna de la pieza que desea mover >>> ")
            assert 'A'<=columna.upper()<='H', "Recuerde que las coordenadas de las columnas van de la 'A' a la 'H'."
            
            columna = dic_col.get(columna.upper())

            break
        
        except ValueError:
            print('Dato ingresado inválido.')
            continue
        
        except AssertionError as msg:
            print('Error de ingreso.', msg)
            continue
    
    return fila,columna

def queen_move(tabla,cm,fi,co,pieza,oponente,qpieza,qooponente,dire,vert,eat = False):
    
    contador = 0
    
    try:
        
        for i in range(cm):
            
            assert fi+vert >= 0 and co+dire >=0, "\nEl movimiento que se desea hacer no pertenece al tablero."
            assert tabla[fi+vert][co+dire] != oponente and tabla[fi+vert][co+dire] != qooponente, "\nEl lugar al que se desea ir está ocupado por una pieza rival."
            assert tabla[fi+vert][co+dire] != pieza and tabla[fi+vert][co+dire] != qpieza,"\nEl lugar al que se desea ir está ocupado por una pieza aliada."

            tabla[fi][co] = '◼'
            tabla[fi+vert][co+dire] = qpieza
            fi += vert
            co += dire

            contador += 1
        
        if eat:
            return fi,co
        else:
            return 1
    
    except AssertionError as msg:
        
        if contador == 0:
            print(msg)
            if eat:
                return fi,co
            else:
                return 0

        if eat:
            return fi,co
        else:
            return 1
        
    except IndexError:
        
        if contador == 0:
            print("El movimiento que se desea hacer no pertenece al tablero.")
            if eat:
                return fi,co
            else:
                return 0

        if eat:
            return fi,co
        else:
            return 1

def val_queen_move(tabla,fil,col,pieza,oponente,qpieza,qoponente,dire): # side es innecesario dire = derecha o izq, direeccion = arriba o abajo.
    
    try:

        direccion =  int(input("Ingrese si desea realizar el movimiento hacia arriba (1) o hacia abajo (2) >>> "))
        
        while direccion != 1 and direccion != 2:
            direccion = int(input("\nINVÁLIDO -- Ingrese si desea realizar el movimiento hacia arriba (1) o hacia abajo (2) >>> "))
        
        cant_mov = int(input("Ingrese la cantidad de movimientos que desea realizar >>> "))
        
        if direccion == 1:
            movimientos = queen_move(tabla,cant_mov,fil,col,pieza,oponente,qpieza,qoponente,dire,-1)
        else:
            movimientos = queen_move(tabla,cant_mov,fil,col,pieza,oponente,qpieza,qoponente,dire,1)
        
        if movimientos == 0:
            return 0
        
        return 1

    except ValueError:

        print("El valor ingresado es incorrecto.", end = " ")
        return 0

def val_queen_eat(tabla,fila,colu,pieza,oponente,qpieza,qoponente): 
    
    movimientos = 0
    flag = False
    
    try:
        
        while True:
            
            print("\nSeleccione qué movimiento desea hacer: \n\n - MOVER A LA IZQUIERDA ARRIBA(1) \n - MOVER A LA IZQUIERDA ABAJO(2) \n - MOVER A LA DERECHA ARRIBA(3)\n - MOVER A LA DERECHA ABAJO(4)\n - TERMINAR TURNO(5)\n")
            mov = int(input("Ingrese el dato solicitado >>> "))
    
            while mov not in (1,2,3,4,5): #while mov != 1 and mov != 2 and mov != 3 and mov!= 4 and mov != 5
                print("INVÁLIDO. Seleccione qué movimiento desea hacer: \n\n - MOVER A LA IZQUIERDA ARRIBA(1) \n - MOVER A LA IZQUIERDA ABAJO(2) \n - MOVER A LA DERECHA ARRIBA(3)\n - MOVER A LA DERECHA ABAJO(4)\n - TERMINAR TURNO(5)\n")
                mov = int(input("Ingrese el dato solicitado >>> "))
            
            if mov == 1:
                if movimientos == 0:
                    fila, colu = queen_move(tabla,8,fila,colu,pieza,oponente,qpieza,qoponente,-1,-1,True)
                
                assert (fila-2 >= 0 and colu-2 >= 0) and (fila-1 >= 0 and colu-1 >= 0),'INVÁLIDO -- La ficha se sale del tablero al intentar comer.' # SACAR LOS AND SI SON INNECESARIOS (SOLO X TESTEO)
                assert tabla[fila-2][colu-2] == '◼', 'INVÁLIDO -- No hay un casillero libre siguente a la ficha que se intenta comer.'
                assert tabla[fila-1][colu-1] == qoponente or tabla[fila-1][colu-1] == oponente,'INVÁLIDO -- No se pueden comer fichas aliadas.'

                tabla[fila][colu] = '◼'
                tabla[fila-1][colu-1] = '◼'
                tabla[fila-2][colu-2] = qpieza
                movimientos += 1
                print_tab(tabla) 
                fila, colu = fila-2, colu-2

            elif mov == 2:
                if movimientos == 0:
                    fila, colu = queen_move(tabla,8,fila,colu,pieza,oponente,qpieza,qoponente,-1,1,True)

                assert (fila+2 <= 8 and colu-2 >= 0) and (fila+1 <= 8 and colu-1 >= 0),'INVÁLIDO -- La ficha se sale del tablero al intentar comer.'
                assert tabla[fila+2][colu-2] == '◼', 'INVÁLIDO -- No hay un casillero libre siguente a la ficha que se intenta comer.'
                assert tabla[fila+1][colu-1] == qoponente or tabla[fila+1][colu-1] == oponente,'INVÁLIDO -- No se pueden comer fichas aliadas.'

                tabla[fila][colu] = '◼'
                tabla[fila+1][colu-1] = '◼'
                tabla[fila+2][colu-2] = qpieza
                movimientos += 1
                print_tab(tabla)
                fila, colu = fila+2, colu-2

            elif mov == 3:
                if movimientos == 0:
                    fila, colu = queen_move(tabla,8,fila,colu,pieza,oponente,qpieza,qoponente,1,-1,True)

                assert (fila-2 >= 0 and colu+2 <= 8) and (fila-1 >= 0 and colu+1 <= 8),'INVÁLIDO -- La ficha se sale del tablero al intentar comer.'
                assert tabla[fila-2][colu+2] == '◼', 'INVÁLIDO -- No hay un casillero libre siguente a la ficha que se intenta comer.'
                assert tabla[fila-1][colu+1] == qoponente or tabla[fila-1][colu+1] == oponente,'INVÁLIDO -- No se pueden comer fichas aliadas.'

                tabla[fila][colu] = '◼'
                tabla[fila-1][colu+1] = '◼'
                tabla[fila-2][colu+2] = qpieza
                movimientos += 1
                print_tab(tabla)
                fila, colu = fila-2, colu+2

            elif mov == 4:
                if movimientos == 0:
                    fila, colu = queen_move(tabla,8,fila,colu,pieza,oponente,qpieza,qoponente,1,1,True)

                assert (fila+2 <= 8 and colu+2 <= 8) and (fila+1 <= 8 and colu+1 <= 8),'INVÁLIDO -- La ficha se sale del tablero al intentar comer.'
                assert tabla[fila+2][colu+2] == '◼','INVÁLIDO -- No hay un casillero libre siguente a la ficha que se intenta comer.'
                assert tabla[fila+1][colu+1] == qoponente or tabla[fila+1][colu+1] == oponente, 'INVÁLIDO -- No se pueden comer fichas aliadas.'

                tabla[fila][colu] = '◼'
                tabla[fila+1][colu+1] = '◼'
                tabla[fila+2][colu+2] = qpieza
                movimientos += 1
                print_tab(tabla) 
                fila, colu = fila+2, colu+2

            else:
                flag = True
                break
        
        return 0 if flag and movimientos == 0 else 1 
        
    except AssertionError as msg:
        
        if movimientos > 0:
            print(msg)
            return 1
        
        print(msg)
        return 0
    
    except IndexError:
        
        if movimientos > 0:
            return 1
    
        return 0

def eat_piece(tb,sentido,fi,co,oponente,qoponente,pieza): 

    try:
        print('Elija si quiere comer a la pieza de la izquierda(1) o a la de la derecha(2).')
        move = int(input('Seleccione el sentido solicitado >>> ')) #Hacer un try por si se ingresa un str o un float.

        while move != 1 and move != 2:
            move = input('INVÁLIDO. Seleccione el sentido solicitado >>> ')
        
        if move == 1 and (tb[fi+sentido][co-1] == oponente or tb[fi+sentido][co-1] == qoponente) and tb[fi+sentido*2][co-2] == '◼':
            tb[fi][co] = '◼'
            tb[fi+sentido][co-1] = '◼'
            tb[fi+sentido*2][co-2],fi,co = pieza,fi+sentido*2,co-2
            return 1,fi,co
            
        elif move == 2 and (tb[fi+sentido][co+1] == oponente or tb[fi+sentido][co+1] == qoponente) and tb[fi+sentido*2][co+2] == '◼': 
            tb[fi][co] = '◼'
            tb[fi+sentido][co+1] = '◼'
            tb[fi+sentido*2][co+2],fi,co = pieza,fi+sentido*2,co+2
            return 1,fi,co

        return 0,fi,co

    except ValueError:
        print('\nEl dato ingresado es incorrecto.')
        return 0,fi,co

def val_piece_eat(tb,side,fi,co,pieza,oponente,qoponente): # La funcion valida si es posible comer la otra pieza, y la cantidad de veces que se puede comer.
    
    try:
        movimientos = 0
        flag = False

        while side == 'Blanco':
            
            if fi <= 5 and co <= 5:
                assert (tb[fi+2][co+2] == '◼' and tb[fi+1][co+1] == oponente) or (tb[fi+2][co-2] == '◼' and tb[fi+1][co-1] == oponente) or (tb[fi+2][co+2] == '◼' and tb[fi+1][co+1] == qoponente) or (tb[fi+2][co-2] == '◼' and tb[fi+1][co-1] == qoponente),'No quedan más piezas que puedan ser comidas.'
            elif fi<=5:
                assert (tb[fi+2][co-2] == '◼' and tb[fi+1][co-1] == oponente) or (tb[fi+2][co-2] == '◼' and tb[fi+1][co-1] == qoponente),'No quedan más piezas que puedan ser comidas.'
            else:
                print("No se puede comer ninguna pieza")
                flag = True
                break
            assert (co-2 >= 0 and fi+2 < 8) or (co+2 < 8 and fi+2 <8),'No puede comerse esa pieza ya que el movimiento se sale del tablero.'
            movimiento_realizado,fi,co = eat_piece(tb,1,fi,co,oponente,qoponente,pieza)   

            if movimiento_realizado == 0:
                print('No puede realizarse tal movimiento.\n')
                flag = True
                break        
            else:
                movimientos += 1
                print('movimiento realizado exitosamente.\n')

        while side == 'Negro':

            if co <= 5:
                assert (tb[fi-2][co+2] == '◼' and tb[fi-1][co+1] == oponente) or (tb[fi-2][co+2] == '◼' and tb[fi-1][co+1] == qoponente) or (tb[fi-2][co-2] == '◼' and tb[fi-1][co-1] == oponente) or (tb[fi-2][co-2] == '◼' and tb[fi-1][co-1] == qoponente),'No quedan más piezas que puedan ser comidas.'
            else:
                assert (tb[fi-2][co-2] == '◼' and tb[fi-1][co-1] == oponente) or (tb[fi-2][co-2] == '◼' and tb[fi-1][co-1] == qoponente),'No quedan más piezas que puedan ser comidas.'
                        
            assert (fi-2 >= 0 and co+2 < 8) or (fi-2 >= 0 and co-2 >= 0),'No puede comerse esa pieza ya que el movimiento se sale del tablero.'
            
            movimiento_realizado,fi,co = eat_piece(tb,-1,fi,co,oponente,qoponente,pieza) 
            
            if movimiento_realizado == 0:
                print('No puede realizarse tal movimiento.\n')
                flag = True
                break
            else:
                movimientos += 1
                print('movimiento realizado exitosamente.\n')

        if flag and movimientos == 0:
            return 0

    except AssertionError as msg:
        if movimientos > 0:
            return 1
        print(f'{msg}', end = " ")
        return 0

    except IndexError: 
        print('No puede comerse esa pieza ya que el movimiento se sale del tablero.', end = " ")
        return 0

def val_piece_move(tb,dire,side,fi,co,pieza,oponente,qpieza,qoponente): # tablero, direeccion de la pieza, pieza (◎ o ◉), coordenadas(fi,co), pieza propia y pieza rival -- La función verifica que se pueda (o no) realizar el movimiento establecido
    
    if side == 'Blanco':
        diagonal = (fi+1,co+dire) #cambiar a dire-co cuando hagamos la matriz invertida :D
    
    elif side == 'Negro':
        diagonal = (fi-1,co+dire)

    
    try:
        
        assert diagonal[1] >= 0, 'no pertenece al tablero' 
        assert tb[diagonal[0]][diagonal[1]] != oponente and tb[diagonal[0]][diagonal[1]] != qoponente, 'está ocupado por una pieza rival'
        assert tb[diagonal[0]][diagonal[1]] != pieza and tb[diagonal[0]][diagonal[1]] != qpieza, 'está ocupado por una pieza propia'

        tb[fi][co] = '◼' # tb[diagonal[0]][diagonal[1]]
        tb[diagonal[0]][diagonal[1]] = pieza
        
        return 1

    except AssertionError as msg:
        print(f"El movimiento que se desea hacer {msg}.", end = " ")
        return 0

    except IndexError:
        print("El movimiento que se desea hacer no pertenece al tablero.", end = " ")
        return 0

def piece_act(tabla,side,fi,co,pieza,oponente,qpieza,qoponente,queen = False): # tablero, direccion de la pieza, pieza (◎ o ◉), coordenadas(fi,co)
    
    print("\nSeleccione qué movimiento desea hacer: \n\n - MOVER A LA IZQUIERDA(1) \n - MOVER A LA DERECHA(2) \n - COMER PIEZA(3)\n - CAMBIAR DE PIEZA(4)\n - RENDIRSE(5)\n")
    mov = int(input("Ingrese el dato solicitado >>> "))
    
    while mov not in (1,2,3,4,5):
        
        print("INVÁLIDO. Seleccione qué movimiento desea hacer: \n - MOVER A LA IZQUIERDA(1) \n - MOVER A LA DERECHA(2) \n - COMER PIEZA(3)\n - CAMBIAR DE PIEZA(4)\n - RENDIRSE(5)\n")
        mov = int(input("ingrese el dato solicitado >>> "))
    
    if mov == 1:
        
        if queen:
            movimiento_realizado = val_queen_move(tabla,fi-1,co,pieza,oponente,qpieza,qoponente,-1)
        else:
            movimiento_realizado = val_piece_move(tabla,-1, side,fi-1,co,pieza,oponente,qpieza,qoponente)
        
        if movimiento_realizado == 0:
            return movimiento_realizado 
            
    elif mov == 2:
    
        if queen:
            movimiento_realizado = val_queen_move(tabla,fi-1,co,pieza,oponente,qpieza,qoponente,1)
        else:
            movimiento_realizado = val_piece_move(tabla,1,side,fi-1,co,pieza,oponente,qpieza,qoponente)

        if movimiento_realizado == 0:
            return movimiento_realizado

    elif mov == 3:
        
        if queen:
            movimiento_realizado = val_queen_eat(tabla,fi-1,co,pieza,oponente,qpieza,qoponente)
        else:
            movimiento_realizado = val_piece_eat(tabla,side,fi-1,co,pieza,oponente,qoponente) # tablero, fi,co , diag-rig, diag-lef
        if movimiento_realizado == 0:
            return movimiento_realizado 

    elif mov== 4:
        return 0   
        
    else:
        rendicion=input('¿Está seguro de que se quiere rendir? (Sí/No) >>> ')
        while rendicion.upper() not in ('SÍ','SI','NO','NEL'):
            rendicion=input('Por favor responda con "Sí" o "No".\n¿Está seguro de que se quiere rendir? (Sí/No) >>> ')

        try:
            assert rendicion.upper() == 'NO'
            return 0
        except AssertionError:
            return -1

def turno_x(dic_col,table,side,pieza,qpieza):
    
    try:

        fi,co = set_move(dic_col)
        
        while table[fi-1][co] != pieza and table[fi-1][co] != qpieza:
            print('La posición seleccionada es inválida.\n')
            fi,co = set_move(dic_col)

        if side == 'Negro':
            
            if "♚" in table[fi-1][co]:
                movimiento = piece_act(table,side,fi,co,'◉','◎',"♚","♔",True) #REINA WHITE REINA BLACK
            else: 
                movimiento = piece_act(table,side,fi,co,'◉','◎',"♚","♔")
            
            while movimiento == 0 and (table[fi-1][co] != pieza and table[fi-1][co] != qpieza):
                print('Vuelva a ingresar su movimiento.\n')
                fi,co = set_move(dic_col)
                
                if "♚" in table[fi-1][co]:
                    movimiento = piece_act(table,side,fi,co,'◉','◎',"♚","♔",True)
                else:
                    movimiento = piece_act(table,side,fi,co,'◉','◎',"♚","♔")

        if side == 'Blanco':

            if "♔" in table[fi-1][co]:
                movimiento = piece_act(table,side,fi,co,'◎','◉',"♔","♚",True)    
            else:
                movimiento = piece_act(table,side,fi,co,'◎','◉',"♔","♚")
            
            while movimiento == 0 and (table[fi-1][co] != pieza and table[fi-1][co] != qpieza):
                print('Vuelva a ingresar su movimiento.\n')                
                fi,co = set_move(dic_col)                
                
                if "♔" in table[fi-1][co]:
                    movimiento = piece_act(table,side,fi,co,'◎','◉',"♔","♚",True)     
                else:
                    movimiento = piece_act(table,side,fi,co,'◎','◉',"♔","♚")
            
        return movimiento
    
    except ValueError:
        print('El dato ingresado no es correcto. Intente nuevamente a continuación.\n')
        return 0

# CREACION DEL TABLERO Y PIEZAS

def tab_checkers():
    
    tab = [[" "] * 8 for i in range(8)]
    blancas = '◎' #verdes
    negras = '◉'  #celestes

    for fila in range(8):
        for columna in range(8):
            if fila % 2 == columna % 2 and (fila == 0 or fila == 1 or fila == 2):
                tab[fila][columna] = blancas
            elif fila % 2 == columna % 2 and (fila == 5 or fila == 6 or fila == 7):
                tab[fila][columna] = negras
            elif fila % 2 == columna % 2:
                tab[fila][columna] = '◼'
            else:
                tab[fila][columna] = "⬚"

    return tab

def print_tab(tab):
    
    for fila in range(8):
            print(f"{Fore.RED}{fila+1}{Fore.BLUE}|", end = "  ")
            for columna in range(8):
                
                if '◎' in tab[fila][columna] or '♔' in tab[fila][columna]:
                    print(f"{Style.DIM}{Fore.GREEN}{tab[fila][columna]}", end = "  ")
                elif '◉' in tab[fila][columna] or '♚' in tab[fila][columna]:
                    print(f"{Fore.CYAN}{tab[fila][columna]}", end = "  ")
                elif '⬚' in tab[fila][columna]:
                    print(f"{Style.BRIGHT}{Fore.WHITE}{tab[fila][columna]}", end = "  ")
                else:
                    print(f"{Style.DIM}{Fore.WHITE}{tab[fila][columna]}", end = "  ")
            print()
    print(" ",f"{Fore.BLUE}-"*25)
    print(f"{Fore.RED}    A  B  C  D  E  F  G  H")

def col_translate():
    letras = ['A','B','C','D','E','F','G','H']
    columnas = dict()
    for i,letra in zip(range(8),letras):
        columnas[letra] = columnas.get(letra,i)  
    return columnas

def main_minijuego3(color_Clay):
    tablero = tab_checkers()
    columnas = col_translate()

    print('Empiezan las Verdes. El juego termina unicamente cuando uno de los dos jugadores gane.\n')
    print(f'VERDES = {Style.DIM}{Fore.GREEN}◎', f'\nCELESTES = {Fore.CYAN}◉', f'\nREINA VERDE = {Style.DIM}{Fore.GREEN}♔', f'\nREINA CELESTE = {Fore.CYAN}♚', f'\nCASILLA IMPOSIBLE = {Style.BRIGHT}{Fore.WHITE}⬚', f'\nCASILLA VACÍA = {Style.DIM}{Fore.WHITE}◼\n')
    print_tab(tablero)
    print('\n')
    
    mal_celeste = False
    mal_verde = False
    while True:
        print('Es el turno de las Verdes.')
        
        t_b = turno_x(columnas,tablero,'Blanco','◎', '♔')
        
        while t_b == 0:
            t_b = turno_x(columnas,tablero,'Blanco','◎', '♔')

        if t_b == -1:
            mal_verde = True
            print('\nTe has rendido.\nGanan las Celestes.') 
            break
        if '◉' not in (item for filas_tablero in tablero for item in filas_tablero) and '♚' not in (item for filas_tablero in tablero for item in filas_tablero):
            mal_celeste = True
            print('\nGanan las Verdes.') 
            break
        if "◎" in tablero[7]:
            print("Su pieza se ha convertido en reina.")
            pos = tablero[7].index("◎")
            tablero[7][pos] = "♔"

        print('\n')
        print_tab(tablero)
        print('\n')
        
        print('Es el turno de las Celestes.')
        
        t_n = turno_x(columnas,tablero,'Negro','◉', '♚')
        
        while t_n == 0:
            t_n = turno_x(columnas,tablero,'Negro','◉', '♚')

        if t_n == -1:
            mal_celeste = True
            print('\nTe has rendido.\nGanan las Verdes.') 
            break
        if '◎' not in (item for filas_tablero in tablero for item in filas_tablero) and '♔' not in (item for filas_tablero in tablero for item in filas_tablero):
            mal_verde = True
            print('\nGanan las Celestes.') 
            break
        if '◉' in tablero[0]:
            print("Su pieza se ha convertido en reina.")
            pos = tablero[0].index('◉')
            tablero[0][pos] = '♚'
        
        print('\n')
        print_tab(tablero)
        print('\n')
    if color_Clay == "2":
        return mal_celeste
    else: 
        return mal_verde
 
# ------------------------------ MAIN -------------------------------
# -------------------------------------------------------------------
graficos_inicio()

texto8= '''E L   J U E G O
  En esta historia tú serás parte de un grupo de hackers llamado CLAY que se enfrentara contra FR13NDS para ganar el campeonato.
  ⚬	 A lo largo del juego tendras que recolectar informacion guardada en archivos .txt que te llevarán a la final
  ⚬	 Tienes 3 mini-enfrentamientos, el último definirá si ganas o no
  '''
mostrar_texto(texto8)
texto9 = '''Moderador:
  "Hola, soy el moderador. Yo estaré controlando que ninguno de los dos equipos este jugando sucio. Como ya saben tiene que recolectar las claves y simplemente ganar.
  Casi me olvido de presentarlos. Por un lado tenemos a FR13NDS."

FR13NDS:
  "Un placer estar aquí como todos los años. Y como siempre mantendremos nuestra reputación en lo alto."

Moderador:
  "Genial! Un placer tenerlos aquí. Y por el otro lado está CLAY un nuevo grupo prometedor."
  '''
mostrar_texto(texto9)

uno_d = dialogo_uno()
while uno_d == True:
    uno_d = dialogo_uno()

texto10 = '''Compañero 1:
  "Hola, chicos. Estaba pensando en distraer a los contrincantes haciendoles pensar en que entraré en la computadora de MRX (el lider de FR13NDS)"
Compañero 2:
  "Me parece una buena idea. Yo estaré trabajando en Ἃ░⡭19₠7⦪23ẻ84" *SEÑAL PERDIDA*
FR13NDS:
  "Eso si que fue muy rápido no lo creen? Buenos les tenemos una sorpresita."
  '''
mostrar_texto(texto10)

acertijo_uno()

texto11='''Compañero 2:
  "Chicos, pude recuperarme"
Compañero 1:
  "Genial. Es hora de atacar." 

JUEGO N°1
  '''
mostrar_texto(texto11)

contador_mini1 = 0
for partidas in range(3):
    a = main_minijuego1()
    contador_mini1 = contador_mini1 + a
if contador_mini1 < 2:
    graficos_fallo()

#Si gana
texto12 ='''Compañero 1:
  "Durante este tiempo pude encontrar vulnerabilidades en los paquetes de la NGFW."
FR13NDS:
  "Buen jugada, pero no fue lo suficiente como para detenernos grupo CLAY."
  '''
mostrar_texto(texto12)

acertijo_dos()

texto13='''Compañero 1:
  "Encontré problemas del cifrado RC4 y se como descifrar esas claves pero tenemos tiempo reducido espiando una de estas conexiones e inspeccionando los paquetes que se iban intercambiando uno de los integrantes de FR13NDS conectado a un punto de acceso. De hecho el tráfico es bajo, es posible inyectar y "estimular" paquetes de respuesta que servirán para lograr que la cantidad de IVs permitiese luego encontrar la clave de acceso WiFi. "
Compañero 1:
  "Ayudanos." 

JUEGO N°2
  '''
mostrar_texto(texto13)

a2 = main_minijuego2()
if a2 == True:
    graficos_fallo()

#Si gana
texto14='''Moderador:
  "Han llegado muy lejos muchachos. Ahora están a punto de enfrentarse a la final."
FR13NDS:
  "Oye CLAY tenemos un mensajito para ti. No seas tímido, abrelo."
  '''
mostrar_texto(texto14)

acertijo_tres()
verificacion_acertijo_tres()

print("EL SIGUIENTE JUEGO SE NECESITA DE UN COMPAÑERO PARA PODER JUGARLO.")
color = int(input('''Qué color quiere que sea CLAY:
  1. Verde
  2. Celeste
 >>> '''))

creditos = '''© CREATED BY:
  Angulo Snaider, Tomás
  Maldonado, Emanuel Agustin   
  Mareco, Melissa Oriana  
  Suazo Verger, Juan Ignacio    '''

a3 = main_minijuego3(color)
if a3 == True:
    texto15='''Moderador:
  "Felicidades FR13NDS has ganado el juego."
FR13NDS:
  "Gracias por esta partida Clay. Nos vemos en la proxima"
  '''
    mostrar_texto(texto15)
    graficos_perder()
    print(creditos)
else: 
    texto16='''Moderador:
  "Felicidades CLAY has ganado el juego."
FR13NDS:
  "Se lo merecen. Nos vemos en la proxima"
  '''
    mostrar_texto(texto16)
    graficos_ganar()
    print(creditos)