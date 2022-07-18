import pygame, sys, random #importamos pygame,sys y random
####################################################################################
pygame.init()       #En estas tres lineas  inicializamos los modulos importados 
pygame.font.init()  #   para poder utilizarlos
pygame.mixer.init() #font espara las tipografias

########################## CONSTANTES ##########################################################
BLANCO=(255,255,255)
NEGRO=(0,0,0)       #Colores
ALTO=900
ANCHO=600           #Dimenciones de pantalla

############################# DECLARACION DE VARIABLES #######################################################
pos_x=0 #POSICION DE LA IMAGEN DE FONDO ENEJE X
pos_y=0 #POSICION DE LA IMAGEN DE FONDO ENEJE Y
vidas=3 #CANTIDAD DE VIDAS DEL JUGADOR
pantalla=pygame.display.set_mode((ANCHO,ALTO)) #ESTA VARIABLE ES PARA MOSTRAR LA PANTALLA PRINCIPAL DEL VIDEO JUEGO
pista=pygame.mixer.music.load("let-the-games-begin-21858.mp3") #EN ESTAVARIABLE SE ALMACENA LA MUSICA DE FONDO DEL VIDEOJUEGO
reloj=pygame.time.Clock() #ESTA ES UNA INSTANCIA AL MODULO PARA CONTROLAR LAS IMAGENES POR SEGUNDOS

####################################################################################
pygame.mixer.music.play(1) #SE DA LA INSTRUCCION DE PONER PLAY A LA MUSICA



#############################   CLASES  #######################################################
"""CREAMOSLA CLASE ENEMIGOS Y JUGADOR PARA PODER CARGAR EN LOS METODOS,LAS IMAGENES QUE REPRESENTAN A LOS  JUGADORES
Y POSICIONAMIENTO DE ESTOS SPRITES CON SELF.IMAGE GUARDAMOS LAS IMAGENES EN VARIABLES Y CON SELF.RECT OBTENEMOS LAS CORDENADAS
PARA MOSTRAR ESTAS IMAGENES.
CON EL METODO UPDATE DE LA CLASE JUGADOR ACTUALIZAMOS LA POSICION DEL JUGADOR CUANDO POR TECLADO SE LE DA LA ORDEN DE MOVERSE DE POSICION"""
class Enemigos(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.image=pygame.image.load("policia.png")
        self.image.set_colorkey(BLANCO)
        self.rect=self.image.get_rect()
class Jugador(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.image=pygame.image.load("player.png")
        self.image.set_colorkey(BLANCO)
        self.rect=self.image.get_rect()
    def update(self):
        super().__init__()
        if event.key==pygame.K_LEFT:
            player.rect.x-=10
        if event.key==pygame.K_RIGHT:
            player.rect.x+=10
#############################   FIN CLASES  #######################################################


lista_policias=pygame.sprite.Group()    # LISTA QUE CONTIENE A LOS SPRITE DE LOS ENEMIGOS
todos_los_sprites=pygame.sprite.Group() #ACA INGRESAMOS A TODOS LOS SPRITES INCLUYENDO AL JUGADOR
lista_coliciones=pygame.sprite.Group() #ESTA LISTA SIRVE PARA DETECTAR CUANDO PERDEMOS UNA VIDA
player=Jugador() #INSTANCIA A LA CLASE JUGADOR
player.rect.x=400/2-player.image.get_rect().height/2  #POSICIONAMIENTO DE LA IMAGEN DEL JUGADOR EN EJE X
player.rect.y=ALTO-52 #POSICIONAMIENTO DE LA IMAGEN DEL JUGADOR EN EJE Y

"""EN ESTE CICLO LO QUE SE HACE ES CREAR UNA INSTANCIA EN LA CANTIDAD ESTABLECIDAD (20) DE LA CLASE POLICIA PARA
ASI CREAR UNA IMAGEN 20 VECES Y LOS AGREGAMOS A LAS LISTAS. DANDOLE COORDENADAS ALEATORIAS EN EJE X E Y  """
for policia in range (20):
    policia=Enemigos()
    policia.rect.x=random.randrange(0,ANCHO-52,133)
    policia.rect.y=random.randrange(-1000,-100,133)
    todos_los_sprites.add(policia)
    lista_policias.add(policia)
    lista_coliciones.add(policia)
todos_los_sprites.add(player)
lista_coliciones.add(player)
fondo= pygame.image.load("fondo_carrera.jpg") #CARGAMOS LA IMAGEN DE FONDO


###########################  CICLO PRINCIPAL ###################################################################################

while vidas>0:
    tiempo=round (pygame.time.get_ticks()/1000)#creamos la variable tiempo redondeando los milisegundos que obtenemos de el modulo time
    arial=pygame.font.SysFont("arial",30)#Creamos el tipo fuente de los textos en pantalla
    fuente=arial.render(str(vidas)+" Vidas",0, BLANCO) #Aca la creamos a la fuente mostrando las vidas
    tiempo_pantalla=arial.render("Tiempo: "+str(tiempo),0,BLANCO) #Lo almacenamos en esta variable mostrando el tiempo

################################################################################################################################
    """Creamos el movimiento de la imagen con una ilusion de ciclo infinito opteniendo el largo de la pantalla y 
    cuando llega al final la imagen se vuelve a mostrar disminuyendo su eje Y"""
    pos_y_relativa=pos_y%fondo.get_rect().height
    pantalla.blit(fondo,(pos_x,pos_y_relativa-fondo.get_rect().height))
    if pos_y_relativa<ALTO:
        pantalla.blit(fondo,(0,pos_y_relativa))
    pos_y+=1
################################################################################################################################
    """En estos for lop detectamos los eventos entre ellos los movimientos de eje x del jugador"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            player.update()
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                player.rect.x-=0
            if event.key==pygame.K_RIGHT:
                player.rect.x+=0
################################################################################################################################
    """En este ciclo for creamos las iteraciones a la lista de policias donde estan almacenados los sprites y le damos 
    el efecto de movimiento sobre el eje y decrementandolo en el eje Y g y dandole un valor random en eje x """
    for policia in lista_policias:
        policia.rect.y+=1
        if policia.rect.y>ALTO:
            policia.rect.y=0
            policia.rect.x=random.randrange(ANCHO)
    #Usamos esta variable para detectar las colisiones de los sprites entre el jugador y los policias
    lista_coliciones=pygame.sprite.spritecollide(player,lista_policias,True)
    #En esta parte usamos el condicional para determinar si perdemoss una vida o no
    if lista_coliciones:
        vidas-=1

    todos_los_sprites.draw(pantalla)#mostramos todos los sprites en pantalla
    pantalla.blit(fuente,(0,0))#mostramos las vidas
    pantalla.blit(tiempo_pantalla,(ANCHO-150,0))#Mostramos el tiempo en pantalla
    pygame.display.update()#Actualización constante de pantalla
    reloj.tick(60)#Movimiento de imagenes por segundo