import pygame
import random
from pygame.locals import *

####### DEFINITIONS DE FONCTIONS #######

# Déclaration et initialisation des variables principales (globales)
def var_principales():

	global tourbg, bigby, couleurbb, vies, test, coeurbonus_startx, coeurbonus_starty, coeurbonus_vitesse , GameOver
	global coeurbonus_largeur, bonusAS_startx, bonusAS_starty, bonusAS_vitesse, bonusAS_largeur, bonusAS_hauteur,vitesse_attaque,i
	global coeurbonus_hauteur, bigbossdifficulte, BIGBOSS_VITESSE, scoreSauvegarde, laser_startx, laser_starty
	global premier, vert, BIGBOSS_VIE, BIGBOSS_LARGEUR, BIGBOSS_HAUTEUR, FENETRE_LARGEUR, FENETRE_HAUTEUR
	global VAISSEAU_LARGEUR, VAISSEAU_HAUTEUR, DECALAGE_VAISSEAU, blanc, SHOT_TAILLEW, SHOT_TAILLE, DECALAGE_IMAGE, vitessedeplacement
	global YBG, VITESSEBG, x, shoot_x, meteorite_largeur, meteorite_hauteur, meteorite_startx1, meteorite_startx2 
	global meteorite_starty1, meteorite_starty2, meteorite_vitesse, shoot_y, fini, score, colorx
	global vieplus1_startx, vieplus1_starty, vieplus1_vitesse, vieplus1_largeur, vieplus1_hauteur,receptacle
	global bonusvite_largeur, bonusvite_startx, bonusvite_starty, bonusvite_vitesse, bonusvite_hauteur,i1
	global bonuslent_largeur, bonuslent_startx, bonuslent_starty, bonuslent_vitesse, bonuslent_hauteur,i2
	
	FENETRE_LARGEUR 	= 1600
	FENETRE_HAUTEUR 	= 1000

	VAISSEAU_LARGEUR	= 150
	VAISSEAU_HAUTEUR 	= 150
	DECALAGE_VAISSEAU 	= 20
	vies 				= 3
	blanc 				= (255, 255, 255)
	vert				= (0, 255, 0)
	GameOver = False
	#caracs des coeurs bonus
	coeurbonus_startx = random.randrange(0,FENETRE_LARGEUR - 100)
	coeurbonus_starty = -50
	coeurbonus_vitesse = 8
	coeurbonus_largeur = 50
	coeurbonus_hauteur = 50
	#caracs du bonus de vitesse d'attaque
	bonusAS_startx = random.randrange(0,FENETRE_LARGEUR - 100)
	bonusAS_starty = -50
	bonusAS_vitesse = 8
	bonusAS_largeur = 50
	bonusAS_hauteur = 50
	i=0
	#caracs du réceptacle:
	vieplus1_startx = random.randrange(0,FENETRE_LARGEUR-115)
	vieplus1_starty = -50
	vieplus1_vitesse = 8
	vieplus1_largeur = 50
	vieplus1_hauteur = 50
	receptacle = 0
	#caracs de bonus de vitesse de déplacement
	bonusvite_startx = random.randrange(0,FENETRE_LARGEUR - 115)
	bonusvite_starty = -50
	bonusvite_vitesse = 8
	bonusvite_largeur = 50
	bonusvite_hauteur = 50
	i1=0
	#caracs du malus de vitesse de déplacement
	bonuslent_startx = random.randrange(0,FENETRE_LARGEUR - 115)
	bonuslent_starty = -50
	bonuslent_vitesse = 8
	bonuslent_largeur = 50
	bonuslent_hauteur = 50
	i2=0

	SHOT_TAILLEW		= 40
	SHOT_TAILLE 		= 100
	DECALAGE_IMAGE 		= 40
	# Position de l'arrière-plan
	YBG					= 0
	VITESSEBG			= 2
	# Variable pour le changement de couleur de l'arrière-plan
	colorx				= 0

	BIGBOSS_LARGEUR		= 1400
	BIGBOSS_HAUTEUR		= 270
	BIGBOSS_VIE		= 300
	BIGBOSS_VITESSE		= 20
	bigbossdifficulte	= 30
	couleurbb			= (0, 255, 0)
	# Position Y initiale du Boss
	bigby 				= -BIGBOSS_HAUTEUR-60
	# Variable permettant l'incrémentation unique du score
	premier 			= True
	# Variable temporaire de sauvegarde du score pour faire revenir le Boss après tel score dépassé
	scoreSauvegarde		= 0

	# Position x initiale du vaisseau
	x = FENETRE_LARGEUR/2
	shoot_x = -SHOT_TAILLE
	vitessedeplacement = 30

	# Caractéristiques des météorites
	meteorite_largeur = 200
	meteorite_hauteur = 200
	meteorite_startx1 = random.randrange(0, FENETRE_LARGEUR/2 -115)
	meteorite_startx2 = random.randrange(FENETRE_LARGEUR/2, FENETRE_LARGEUR - meteorite_largeur -115)
	meteorite_starty1 = -FENETRE_LARGEUR/2
	meteorite_starty2 = -FENETRE_LARGEUR	
	meteorite_vitesse = 10

	# Caractéristiques des lasers ennemis
	laser_startx = random.randrange(FENETRE_LARGEUR - BIGBOSS_LARGEUR, FENETRE_LARGEUR - BIGBOSS_HAUTEUR -115)
	laser_starty = BIGBOSS_HAUTEUR - 60

	# Score initial
	score = 0

	# Position initiale de l'obus + vitesse d'attaque
	shoot_y = -SHOT_TAILLE
	vitesse_attaque = 50

	# État du jeu
	fini = False

	# Variable permettant d'intervertir les arrière-plans pour leur animation verticale
	tourbg = 0

# Permet de lancer l'obus grâce à la touche espace uniquement quand il sort de la fenêtre (limitation de tir)


# Classe concernant les touches (limites du vaisseau et mouvement)
class Touche():

	def Gauche(activee):
		if x > VAISSEAU_LARGEUR/2:
			activee = True
		return activee

	def Droite(activee):
		if x < (FENETRE_LARGEUR - VAISSEAU_LARGEUR/2 -115):
			activee = True
		return activee
	def Espace(activee):
		if (shoot_y <= -SHOT_TAILLE):
			activee = True
		return activee

	def Enfoncee():
		enfoncee = pygame.key.get_pressed() 
		return enfoncee

# Vaisseaux meteorites
def meteorites_caract(enx, eny, en_larg, en_haut):

	screen.blit(meteor, (enx, eny))

# Forme du texte
def text_objects(text, font, couleur):

	textSurface = font.render(text, True, couleur)
	return textSurface, textSurface.get_rect()

# Affichage de titres
def message_display(text, couleur): 

	largeText = pygame.font.Font("fonts/font.ttf",100) 
	TextSurf, TextRect = text_objects(text, largeText, couleur) 
	TextRect.center = ((FENETRE_LARGEUR/2),(FENETRE_HAUTEUR/3))
	screen.blit(TextSurf, TextRect)

# Affichage de l'introduction
def introduction(activee):

	while activee:
		screen.fill((0, 0, 0))
		message_display("SPACE INVASION", blanc)
		introductiontexte(FENETRE_LARGEUR/2 - 420, FENETRE_HAUTEUR/2, 45)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				activee = False
		pygame.display.flip()

# Affichage de l'explosion du Game Over
def explosion():

	explosion = pygame.image.load("images/explosion.png")
	explosion = pygame.transform.scale(explosion, (VAISSEAU_HAUTEUR + 80, VAISSEAU_HAUTEUR + 80))
	screen.blit(explosion, (x - VAISSEAU_LARGEUR/1.5, FENETRE_HAUTEUR - 2 * DECALAGE_VAISSEAU - VAISSEAU_HAUTEUR))

# Affichage du Game Over
def gameover():
	
	GameOver = True
	premiertour = True

	while GameOver:

		message_display("Game Over", (255, 0, 0))

		pygame.display.flip()

		if premiertour:
			pygame.time.wait(2000)
			premiertour = False
			introtextetaille = pygame.font.Font("fonts/ColabBol.otf", 50)
			texteintro = introtextetaille.render("Appuyez sur 'Espace' pour rejouer", 1, (80, 80, 80))
			screen.blit(texteintro, [FENETRE_LARGEUR/2 - 380, FENETRE_HAUTEUR/2 + 50])

		for event in pygame.event.get():		
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			# Rejouer si on appuie sur 'Espace'
			if event.type == pygame.KEYDOWN:
				if event.key == K_SPACE:
					GameOver = False
					background.play(-1)
					break
		pygame.display.flip()

# Classe concernant les météorites
class meteoriteTouchee():

	# Relation entre obus et météorite gauche
	def obusTouche1(etat):
		if (shoot_y > -SHOT_TAILLE) and (shoot_y < meteorite_starty1 + meteorite_hauteur) and (shoot_x >= meteorite_startx1 - SHOT_TAILLEW) and (shoot_x <= meteorite_startx1 + meteorite_largeur + SHOT_TAILLEW):
			etat = True
		return etat

	# Relation entre obus et météorite droite
	def obusTouche2(etat):
		if (shoot_y > -SHOT_TAILLE) and (shoot_y < meteorite_starty2 + meteorite_hauteur) and (shoot_x >= meteorite_startx2 - SHOT_TAILLEW) and (shoot_x <= meteorite_startx2 + meteorite_largeur + SHOT_TAILLEW):
			etat = True
		return etat

	# Relation entre vaisseau et météorite gauche
	def meteorite1(etat):
		if (vaisseau_top < meteorite_starty1 + meteorite_hauteur/2) and (x >= meteorite_startx1 - VAISSEAU_LARGEUR/3) and (x -VAISSEAU_LARGEUR/3<= meteorite_startx1 + meteorite_largeur):
			etat = True
		return etat

	# Relation entre vaisseau et météorite gauche
	def meteorite2(etat):
		if (vaisseau_top < meteorite_starty2 + meteorite_hauteur/2) and (x >= meteorite_startx2 - VAISSEAU_LARGEUR/3) and (x- VAISSEAU_LARGEUR/3 <= meteorite_startx2 + meteorite_largeur):
			etat = True
		return etat

	# Incrémentation du score de 1 si météorite évitée
	def score():
		global score, meteorite_starty1, meteorite_startx1, meteorite_starty2, meteorite_startx2

		if (meteorite_starty1 > FENETRE_HAUTEUR):
			meteorite_starty1 = -meteorite_largeur
			meteorite_startx1 = random.randrange(0, FENETRE_LARGEUR/2 -115)
			score += 1

		if (meteorite_starty2 > FENETRE_HAUTEUR):
			meteorite_starty2 = -FENETRE_LARGEUR/2
			meteorite_startx2 = random.randrange(FENETRE_LARGEUR/2, FENETRE_LARGEUR - meteorite_largeur -115)
			score += 1


# Affichage du score
def Score(x, y, taille):
	tailleTexteScore = pygame.font.Font("fonts/ColabBol.otf", taille)
	texteScore = tailleTexteScore.render("Score : "+str(score), 1, blanc)
	screen.blit(texteScore, [x, y])

# Affichage du texte de l'introduction
def introductiontexte(x, y, taille):
	introtextetaille = pygame.font.Font("fonts/ColabBol.otf", taille)
	texteintro = introtextetaille.render("Appuyez sur une touche pour commencer", 1, blanc)
	screen.blit(texteintro, [x, y])

# Animation des couleurs d'arrière-plan
def arriereplan():
	global YBG
	global colorx

	if not (YBG >= FENETRE_HAUTEUR):
		screen.fill((10+1.5*colorx, 2*colorx, 20+2*colorx))
		screen.blit(arriere_plan,(0, 0+YBG))
		screen.blit(arriere_plan, (0, -FENETRE_HAUTEUR+YBG))
	else:
		YBG = 0
	YBG += VITESSEBG

# Défilement des étoiles
def couleurbg():
	global colorx, tourbg

	if tourbg == 0:
		colorx += 0.03
		if colorx >= 20:
			tourbg = 1
	elif tourbg == 1:
		colorx -= 0.03
		if colorx <= 0:
			tourbg = 0

# Classe concernant le Boss
class BigBoss():

	def bigBoss():

		global bigby, couleurbb, score, bigbossdifficulte, premier, laser_startx, laser_starty, scoreSauvegarde, shoot_y, BIGBOSS_VIE, BIGBOSS_VITESSE
		tour1 = True
		# "Si palier de score atteint, on fait apparaître le Boss"
		if (score >= scoreSauvegarde + 100):
			screen.blit(bigboss, (FENETRE_LARGEUR/2 - bigboss.get_width()/2, 60+bigby))
			pygame.draw.rect(screen, couleurbb, (FENETRE_LARGEUR/2-150, 20+bigby, BIGBOSS_VIE, 40), 0)
			pygame.draw.rect(screen, couleurbb, (FENETRE_LARGEUR/2-150, 20+bigby, 300, 40), 2)
			premier = True

			# Gestion de la vie, du laser ennemi et du score
			if (bigby >= 0):
				screen.blit(shot2, (laser_startx, laser_starty))
				laser_starty += BIGBOSS_VITESSE
				if (BIGBOSS_VIE > 0) and (shoot_y > -SHOT_TAILLE) and (shoot_y <= 2*VAISSEAU_HAUTEUR - 30) and (shoot_x >= FENETRE_LARGEUR/2 - bigboss.get_width()/2 - SHOT_TAILLEW/2) and (shoot_x <= FENETRE_LARGEUR/2 - bigboss.get_width()/2 + BIGBOSS_LARGEUR + SHOT_TAILLEW/2):
					tirtouche.play()
					BIGBOSS_VIE -= bigbossdifficulte
					shoot_y = -SHOT_TAILLE
					BigBoss.bigBossLasers()
					if BIGBOSS_VIE <= 150 and BIGBOSS_VIE > 75:
						couleurbb = (255, 100, 0)
					elif BIGBOSS_VIE <= 75:
						couleurbb = (255, 0, 0)

			BigBoss.bigBossLasers()

			# Animation du vaisseau (arrivée)
			if (bigby < 0) and (BIGBOSS_VIE > 0):
				bigby += 4

			# Animation du vaisseau (départ)
			elif (BIGBOSS_VIE <= 0) and (bigby > -BIGBOSS_HAUTEUR-60):
				BIGBOSS_VIE = 0
				bigby -= 12
				#if tour1:
					#jouer bruit du vaisseau qui part

			# Réinitialisation des variables pour le prochain vaisseau
			elif (BIGBOSS_VIE <= 0) and premier:
				score += 100
				premier = False
				scoreSauvegarde = score
				BIGBOSS_VIE = 300
				bigby = - BIGBOSS_HAUTEUR - 60
				laser_starty = BIGBOSS_HAUTEUR - 60
				BIGBOSS_VITESSE += 2
				bigbossdifficulte /= 1.25
				couleurbb = (0, 255, 0)

	# Remise en place du laser du vaisseau 
	def bigBossLasers():
		global laser_startx, laser_starty

		# Disposition aléatoire initiale du laser ennemi
		if (laser_starty > FENETRE_HAUTEUR):
			laser_starty = BIGBOSS_HAUTEUR - 60
			laser_startx = random.randrange(FENETRE_LARGEUR - BIGBOSS_LARGEUR, FENETRE_LARGEUR - BIGBOSS_HAUTEUR -115)

	# Relation entre le laser ennemi et le vaisseau du joueur
	def bigBossLaserTouche():

		global laser_starty, laser_startx, vies
		if (vaisseau_top < laser_starty + SHOT_TAILLE/2) and (laser_starty <= FENETRE_HAUTEUR - 2*SHOT_TAILLE) and (x >= laser_startx - VAISSEAU_LARGEUR/2) and (x <= laser_startx + (VAISSEAU_LARGEUR/10)*7):
			meteoritetouche.play()
			laser_starty+=500			
			vies -= 1

# Test de Game Over
def testGameOver():
	global vies, meteorite_startx1, meteorite_starty1, meteorite_startx2, meteorite_starty2

	if meteoriteTouchee.meteorite1(False):
		meteoritetouche.play()
		meteorite_starty1 = -meteorite_largeur
		meteorite_startx1 = random.randrange(0, FENETRE_LARGEUR/2 -115)
		vies-=1
	if meteoriteTouchee.meteorite2(False):
		meteoritetouche.play()
		meteorite_startx2 = random.randrange(FENETRE_LARGEUR/2, FENETRE_LARGEUR - meteorite_largeur -115)
		meteorite_starty2 = -3*meteorite_largeur
		vies-=1


# Affichage de l'obus du vaisseau du joueur
def affichageObus():

	global shoot_y, shoot_x, meteorite_startx1, meteorite_startx2, meteorite_starty1, meteorite_starty2, score, vitesse_attaque

	# "Si obus (toujours) à l'écran, on fait monter"
	if (shoot_y >= -SHOT_TAILLE) and not meteoriteTouchee.obusTouche1(False) and not meteoriteTouchee.obusTouche2(False):
		screen.blit(shot, (shoot_x - SHOT_TAILLEW/2 , shoot_y - SHOT_TAILLE))
		shoot_y -= vitesse_attaque

	else:
	# Incrémentation du score de 2 si obus touche météorite
		if meteoriteTouchee.obusTouche1(False):
			tirtouche.play()
			meteorite_startx1 = random.randrange(0, FENETRE_LARGEUR/2 -115)
			meteorite_starty1 = -3*meteorite_largeur
			shoot_y = -SHOT_TAILLE	
			score += 2

		if meteoriteTouchee.obusTouche2(False):
			tirtouche.play()
			meteorite_startx2 = random.randrange(FENETRE_LARGEUR/2, FENETRE_LARGEUR - meteorite_largeur -115)
			meteorite_starty2 = -3*meteorite_largeur
			shoot_y = -SHOT_TAILLE	
			score += 2

# Gestion des événements pygame (QUIT, KEYDOWN, .get_pressed)
def touchesClavier():
	global fini, shoot_y, shoot_x, x, event, vitessedeplacement

	# Gestion des événements
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			fini = True
		
	if Touche.Enfoncee()[pygame.K_SPACE]:
		if Touche.Espace(False):
			tir.play()
			shoot_y = screen.get_height() - VAISSEAU_HAUTEUR
			shoot_x = x
	# "Si Gauche enfoncée et dans les limites, on fait bouger"
	if Touche.Enfoncee()[pygame.K_LEFT]:
		if Touche.Gauche(False):
			x -= vitessedeplacement
	# "Si Droite enfoncée et dans les limites, on fait bouger"
	if Touche.Enfoncee()[pygame.K_RIGHT]:
		if Touche.Droite(False):
			x += vitessedeplacement

def Vies():

	global vies,i,i1,i2
	if (receptacle == 1) :
		
		if (vies>4):
			vies=4
		if (vies==4):
			screen.blit(coeurplein,((FENETRE_LARGEUR-110),10))
			screen.blit(coeurplein,((FENETRE_LARGEUR-175),10))
			screen.blit(coeurplein,((FENETRE_LARGEUR-240),10))
			screen.blit(coeurplein,((FENETRE_LARGEUR-305),10))
			if(i>1):
				screen.blit(imagebonusAS,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-145)))  
			if(i1>1):
				screen.blit(imagebonusvite,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-345)))
			if(i2>1):
				screen.blit(imagebonuslent,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-245)))
		if (vies==3):
			screen.blit(coeurvide,((FENETRE_LARGEUR-110),10))
			screen.blit(coeurplein,((FENETRE_LARGEUR-175),10))
			screen.blit(coeurplein,((FENETRE_LARGEUR-240),10))
			screen.blit(coeurplein,((FENETRE_LARGEUR-305),10))
			if(i>1):
				screen.blit(imagebonusAS,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-145)))  
			if(i1>1):
				screen.blit(imagebonusvite,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-345)))
			if(i2>1):
				screen.blit(imagebonuslent,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-245)))
		if (vies==2):
			screen.blit(coeurvide,((FENETRE_LARGEUR-110),10))
			screen.blit(coeurvide,((FENETRE_LARGEUR-175),10))
			screen.blit(coeurplein,((FENETRE_LARGEUR-240),10))
			screen.blit(coeurplein,((FENETRE_LARGEUR-305),10))
			if(i>1):
				screen.blit(imagebonusAS,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-145)))  
			if(i1>1):
				screen.blit(imagebonusvite,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-345)))
			if(i2>1):
				screen.blit(imagebonuslent,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-245)))
		if (vies==1):
			screen.blit(coeurvide,((FENETRE_LARGEUR-110),10))
			screen.blit(coeurvide,((FENETRE_LARGEUR-175),10))
			screen.blit(coeurvide,((FENETRE_LARGEUR-240),10))
			screen.blit(coeurplein,((FENETRE_LARGEUR-305),10))
			if(i>1):
				screen.blit(imagebonusAS,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-145)))  
			if(i1>1):
				screen.blit(imagebonusvite,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-345)))
			if(i2>1):
				screen.blit(imagebonuslent,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-245)))
		if (vies==0):
			explosion()
			Score(FENETRE_LARGEUR/2 - 175, FENETRE_HAUTEUR/3 + 80, 80)
			background.stop()
			# Réinitialisation des variables principales
			var_principales()
			boum.play()
			gameover()
	else :
		if (vies>3):
			vies=3
		if (vies==3):
			screen.blit(coeurplein,((FENETRE_LARGEUR-110),10))
			screen.blit(coeurplein,((FENETRE_LARGEUR-175),10))
			screen.blit(coeurplein,((FENETRE_LARGEUR-240),10))
			if(i>1):
				screen.blit(imagebonusAS,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-145)))  
			if(i1>1):
				screen.blit(imagebonusvite,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-345)))
			if(i2>1):
				screen.blit(imagebonuslent,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-245)))
		if (vies==2):
			screen.blit(coeurvide,((FENETRE_LARGEUR-110),10))
			screen.blit(coeurplein,((FENETRE_LARGEUR-175),10))
			screen.blit(coeurplein,((FENETRE_LARGEUR-240),10))
			if(i>1):
				screen.blit(imagebonusAS,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-145)))  
			if(i1>1):
				screen.blit(imagebonusvite,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-345)))
			if(i2>1):
				screen.blit(imagebonuslent,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-245)))
		if (vies==1):
			screen.blit(coeurvide,((FENETRE_LARGEUR-110),10))
			screen.blit(coeurvide,((FENETRE_LARGEUR-175),10))
			screen.blit(coeurplein,((FENETRE_LARGEUR-240),10))
			if(i>1):
				screen.blit(imagebonusAS,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-145)))  
			if(i1>1):
				screen.blit(imagebonusvite,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-345)))
			if(i2>1):
				screen.blit(imagebonuslent,((FENETRE_LARGEUR-95),(FENETRE_HAUTEUR-245)))
		if (vies==0):
			explosion()
			Score(FENETRE_LARGEUR/2 - 175, FENETRE_HAUTEUR/3 + 80, 80)
			background.stop()
			# Réinitialisation des variables principales
			var_principales()
			boum.play()
			gameover()


def bonus():
	global coeurbonus_starty, bonusAS_starty,vieplus1_starty, bonusvite_starty, bonuslent_starty
	# Apparition des 'coeurs'
	if ((((score+100)%200)==0) or (((score+100)%200)==1)) and (score!=1) and (score !=0):
		test = 1		
		if (test==1) and (coeurbonus_starty > FENETRE_HAUTEUR-51) :
			coeurbonus_starty = -FENETRE_HAUTEUR/6
	else :
		test=0
	# Apparition 'vitesse d'attaque'
	if ((((score+25)%100)==0) or (((score+25)%100)==1)) and (score!=1) and (score !=0):
		test1 = 1
		if (test1==1) and (bonusAS_starty > FENETRE_HAUTEUR-51):
			bonusAS_starty = -FENETRE_HAUTEUR/6
	else :
		test1 = 0
	# Apparition du 'réceptacle'
	if ((score==250) or (score==251)):
		test2 = 1
		if (test2==1) and (vieplus1_starty > FENETRE_HAUTEUR-51):
			vieplus1_starty = -FENETRE_HAUTEUR/6
	else :
		test2 = 0
	# Apparition du bonus de vitesse de déplacement
	if ((((score+50)%100)==0) or (((score+50)%100)==1)) and (score!=1) and (score !=0):
		test3 = 1
		if (test3==1) and (bonusvite_starty > FENETRE_HAUTEUR-51):
			bonusvite_starty = -FENETRE_HAUTEUR/6
	else :
		test3 = 0
	# Apparition du malus de déplacement
	if ((((score+75)%100)==0) or (((score+75)%100)==1)) and (score!=1) and (score !=0):
		test4 = 1
		if (test4==1) and (bonuslent_starty > FENETRE_HAUTEUR-51):
			bonuslent_starty = -FENETRE_HAUTEUR/6
	else :
		test4 = 0
def dispositionBonus():

	global score, coeurbonus_starty, coeurbonus_vitesse, coeurbonus_startx, vies, bonusAS_startx, bonusAS_starty, bonusAS_vitesse, vitesse_attaque, vieplus1_starty, vieplus1_startx,receptacle,i,i1,i2, bonusvite_starty, bonusvite_vitesse, bonusvite_startx, bonuslent_starty, bonuslent_startx, bonuslent_vitesse, vitessedeplacement, GameOver

	#disposition des coeurs:
	if (score>=100):
		if (coeurbonus_starty <= FENETRE_HAUTEUR):
			coeurbonus_starty+= coeurbonus_vitesse
			screen.blit(bonusvie,(coeurbonus_startx,coeurbonus_starty))
			
			if (vaisseau_top < coeurbonus_starty + coeurbonus_hauteur/2) and (FENETRE_HAUTEUR > coeurbonus_starty - coeurbonus_hauteur/4) and (x -VAISSEAU_LARGEUR/2 < (coeurbonus_startx + coeurbonus_largeur)) and (( x+ 	VAISSEAU_LARGEUR) > coeurbonus_startx):
				sonbonus.play()
				score+=2
				vies+=1
				coeurbonus_starty+=FENETRE_HAUTEUR
				coeurbonus_startx=random.randrange(0, FENETRE_LARGEUR-115)	
	#dispositions des bonus d'AS:
	if (score>=75):
		if (bonusAS_starty <= FENETRE_HAUTEUR):
			bonusAS_starty+= bonusAS_vitesse
			screen.blit(bonusAS,(bonusAS_startx, bonusAS_starty))
			if (vaisseau_top < bonusAS_starty + bonusAS_hauteur/2) and (FENETRE_HAUTEUR > bonusAS_starty - bonusAS_hauteur/4) and (x - VAISSEAU_LARGEUR/2 < (bonusAS_startx + bonusAS_largeur)) and (( x+ 	VAISSEAU_LARGEUR) > bonusAS_startx):
				sonbonus.play()
				i=400
				vitesse_attaque+=100
				score+=2
				bonusAS_starty += FENETRE_HAUTEUR
				bonusAS_startx = random.randrange(0, FENETRE_LARGEUR-115)
		if(i>1):
			i-=1
		if(i==1):
			vitesse_attaque=50
			i-=1

	#dispositions des bonus de vitesse de déplacement:
	if (score>=50):
		if (bonusvite_starty <= FENETRE_HAUTEUR):
			bonusvite_starty+= bonusvite_vitesse
			screen.blit(bonusvite,(bonusvite_startx, bonusvite_starty))
			if (vaisseau_top < bonusvite_starty + bonusvite_hauteur/2) and (FENETRE_HAUTEUR > bonusvite_starty - bonusvite_hauteur/4) and (x - VAISSEAU_LARGEUR/2 < (bonusvite_startx + bonusvite_largeur)) and (( x+ 	VAISSEAU_LARGEUR) > bonusvite_startx):
				sonbonus.play()
				i1=400
				vitessedeplacement+=15
				score+=2
				bonusvite_starty += FENETRE_HAUTEUR
				bonusvite_startx = random.randrange(0, FENETRE_LARGEUR-115)
		if(i1>1):
			i1-=1
		if(i1==1):
			vitessedeplacement=30
			i1-=1

	#dispositions des malus de vitesse de déplacement:
	if (score>=25):
		if (bonuslent_starty <= FENETRE_HAUTEUR):
			bonuslent_starty+= bonuslent_vitesse
			screen.blit(bonuslent,(bonuslent_startx, bonuslent_starty))
			if (vaisseau_top < bonuslent_starty + bonuslent_hauteur/2) and (FENETRE_HAUTEUR > bonuslent_starty - bonuslent_hauteur/4) and (x - VAISSEAU_LARGEUR/2 < (bonuslent_startx + bonuslent_largeur)) and (( x+ 	VAISSEAU_LARGEUR) > bonuslent_startx):
				sonbonus.play()
				i2=400
				vitessedeplacement-=15
				score+=2
				bonuslent_starty += FENETRE_HAUTEUR
				bonuslent_startx = random.randrange(0, FENETRE_LARGEUR-115)
		if(i2>1):
			i2-=1
		if(i2==2):
			vitessedeplacement=30		
			i2-=1	
			
	#disposition du réceptacle :
	if (score>=250):
		if(vieplus1_starty <= FENETRE_HAUTEUR):
			screen.blit(vieplus1,(vieplus1_startx,vieplus1_starty))
			vieplus1_starty+= vieplus1_vitesse
			if (vaisseau_top < vieplus1_starty + vieplus1_hauteur/2) and (FENETRE_HAUTEUR > vieplus1_starty - vieplus1_hauteur/4) and (x - VAISSEAU_LARGEUR/2< (vieplus1_startx + vieplus1_largeur)) and (( x+ 	VAISSEAU_LARGEUR) > vieplus1_startx):
				sonbonus.play()
				score+=2
				receptacle=1
				vies+=1
				vieplus1_starty+= FENETRE_HAUTEUR
		


####### INITIALISATION DU JEU ET DES FICHIERS #######

pygame.init()

# Initialisation des variables globales
var_principales()

# Titre de fenêtre
pygame.display.set_caption("SPACE INVASION")

# Musique de fond
#background = pygame.mixer.Sound("music/bg_music.wav")
pygame.mixer.music.load("music/bg_music.mp3")
boum = pygame.mixer.Sound("music/boum.wav")
tir = pygame.mixer.Sound("music/tir1.wav")
tir.set_volume(0.9)
tirtouche = pygame.mixer.Sound("music/Tirtouche.wav")
meteoritetouche = pygame.mixer.Sound("music/MeteoriteTouche.wav")
sonbonus = pygame.mixer.Sound("music/bonus.wav")

clock = pygame.time.Clock()

fenetre_taille = (FENETRE_LARGEUR, FENETRE_HAUTEUR)

# Crée une fenêtre de taille "fenetre_taille"
screen = pygame.display.set_mode(fenetre_taille)

# Chargement des images et positionnement
vaisseau = pygame.image.load("images/spaceship.png").convert_alpha()
arriere_plan = pygame.image.load("images/space_stars.png").convert_alpha()
shot = pygame.image.load("images/shot.png").convert_alpha()
shot2 = pygame.image.load("images/shot2.png").convert_alpha()
vaisseau_top = FENETRE_HAUTEUR - VAISSEAU_HAUTEUR - DECALAGE_VAISSEAU
vaisseau_gauche = FENETRE_LARGEUR/2 - VAISSEAU_LARGEUR/2
bigboss = pygame.image.load("images/bigboss.png").convert_alpha()
meteor = pygame.image.load("images/meteor.gif").convert_alpha()
coeurplein = pygame.image.load("images/coeur.png").convert_alpha()
coeurvide = pygame.image.load("images/coeurvide.png").convert_alpha()
bonusvie = pygame.image.load("images/bonuscoeur.png").convert_alpha()
bonusAS = pygame.image.load("images/bonusAS.png").convert_alpha()
bonusvite = pygame.image.load("images/sprint.png").convert_alpha()
bonuslent = pygame.image.load("images/snail.png").convert_alpha()
imagebonusAS = pygame.image.load("images/imagebonusAS.png").convert_alpha()
vieplus1 = pygame.image.load("images/receptacle.png").convert_alpha()
hexagone = pygame.image.load("images/hexagone.png").convert_alpha()



# Redimensionnement des images
vaisseau = pygame.transform.scale(vaisseau, (VAISSEAU_LARGEUR, VAISSEAU_HAUTEUR)) 
arriere_plan = pygame.transform.scale(arriere_plan, (FENETRE_LARGEUR, FENETRE_HAUTEUR))
shot = pygame.transform.scale(shot, (SHOT_TAILLEW, SHOT_TAILLE))
shot2 = pygame.transform.scale(shot2, (SHOT_TAILLEW, SHOT_TAILLE))
bigboss = pygame.transform.scale(bigboss, (BIGBOSS_LARGEUR, BIGBOSS_HAUTEUR))
meteor = pygame.transform.scale(meteor, (meteorite_largeur, meteorite_hauteur))
coeurplein = pygame.transform.scale(coeurplein, (100,100))
coeurvide = pygame.transform.scale(coeurvide,(100,100))
bonusvie = pygame.transform.scale(bonusvie,(coeurbonus_largeur,coeurbonus_hauteur))
bonusAS = pygame.transform.scale(bonusAS, (bonusAS_largeur,bonusAS_hauteur))
bonusvite = pygame.transform.scale(bonusvite,(bonusvite_largeur,bonusvite_hauteur))
bonuslent = pygame.transform.scale(bonuslent,(bonuslent_largeur,bonuslent_hauteur))
imagebonusvite = pygame.transform.scale(bonusvite,(90,90))
imagebonuslent = pygame.transform.scale(bonuslent,(90,90))
vieplus1 = pygame.transform.scale(vieplus1, (vieplus1_largeur,vieplus1_hauteur))
hexagone = pygame.transform.scale(hexagone, (100,100))
imagebonusAS = pygame.transform.scale(imagebonusAS, (90,90))
introduction(True)

# Mise en marche de la musique de fond (-1 = infiniment ; 0.5 = commencer à 0.5s.)
#background.play(-1)
pygame.mixer.music.play(-1, 0.5)
####### BOUCLE PRINCIPALE #######



while not fini:

	# 40 images par seconde
	clock.tick(60)

	arriereplan()
	bonus()
	dispositionBonus()
	BigBoss.bigBoss()
	BigBoss.bigBossLaserTouche()

	# Disposition aléatoire des météorites et mouvement
	meteorites_caract(meteorite_startx1, meteorite_starty1, meteorite_largeur, meteorite_hauteur)
	meteorites_caract(meteorite_startx2, meteorite_starty2, meteorite_largeur, meteorite_hauteur)
	
	# Mouvement des météorites
	meteorite_starty1 += meteorite_vitesse
	meteorite_starty2 += meteorite_vitesse

	# Augmentation graduelle de la vitesse des météorites
	meteorite_vitesse += 0.002

	couleurbg()

	meteoriteTouchee.score()

	touchesClavier()

	affichageObus()

	screen.blit(vaisseau, (x-vaisseau.get_width()/2,vaisseau_top))

	testGameOver()

	Vies()
	
	#on affiche à l'écran les hexagones, puisqu'ils restent de toute facon tout le temps
	screen.blit(hexagone,((FENETRE_LARGEUR-100),(FENETRE_HAUTEUR-150)))
	screen.blit(hexagone,((FENETRE_LARGEUR-100),(FENETRE_HAUTEUR-250)))
	screen.blit(hexagone,((FENETRE_LARGEUR-100),(FENETRE_HAUTEUR-350)))
	Score(20, 20, 40)

	# Rafraîchissement
	pygame.display.flip()

################ A FAIRE :	
#	- Régler le bug des bonus
################ SI POSSIBLE (FPS) :
#	- Créer des bonus
#		- Bonus +x points
#		- Bonus transparence (avec temps)
#		- Bonus rapidité (avec temps)
#			idée temps : créer une variable bonus1,2 qui se décrémente à chaque tour de boucle jusqu'à 0 (0 = fin bonus)
#		- idée : idem vaisseau ennemi avec bonus arrivant tous les x score de la même façon que les météorites (aléatoirement)
# ATTENTION : tenir compte que trop d'options peut ralentir le jeu
