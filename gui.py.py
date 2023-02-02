## imports
import time
import datetime
import obd
import pygame
from sys import exit

## increment for running tach GUI
RPM_INCREMENT = 250
## pygame font size
FONT_SIZE = 30
## screend dimensions
SCREEN_WIDTH = 800
SCREEN_LENGTH = 400
## intializing pygame and display
pygame.init()
font = pygame.font.SysFont("FreeSans", FONT_SIZE)
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_LENGTH))
pygame.display.set_caption("GUI")
clock = pygame.time.Clock()
## font = pygame.font.SysFont("Times New Roman", 36)

## intializing obd connection variables
speed = obd.commands.SPEED
rpm = obd.commands.RPM
oil_temp = obd.commands.OIL_TEMP
intake_temp = obd.commands.INTAKE_TEMP
maf = obd.commands.MAF

## speedDisplayValue = font.render(str(connection.query(speed)))

# TODO: feed async value into runGui, use switch statement to display correct number of rectangles

def main():
	# Connection setup: open, watch.
	connection = obd.Async()
	connection.watch(speed)
	connection.watch(rpm, callback = new_rpm)
	connection.watch(oil_temp)
	connection.watch(intake_temp)
	connection.watch(maf)
	connection.start()
	rpmValue = 0

	while True:
		screen.fill((0,0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				connection.stop()
				pygame.quit()
				exit()

		# Connection query updates.
		speedValue = str(connection.query(speed))
		oilTempValue = str(connection.query(oil_temp))
		mafValue = str(connection.query(maf))
		intakeTempValue = str(connection.query(intake_temp))
		displaySpeed = font.render(speedValue, True, (255,255,255))
		file = open("rpms.txt", "r")
		rpmF = file.read()
		rpmF = rpmF[0:rpmF.find(".")]
		if rpmF != '':
			rpmValue = int(rpmF) // RPM_INCREMENT
		file.close()

		#rendder data values into font objects
		displaySpeed = font.render(speedValue, True, (255,255,255))
		displayOilTemp = font.render(oilTempValue, True, (255,255,255))
		displayMAF = font.render(mafValue, True, (255,255,255))
		displayIntakeTemp = font.render(intakeTempValue, True, (255,255,255))

		#display data to user on screen
		screen.blit(displaySpeed, (35, 170))
		screen.blit(displayOilTemp, (30, 310))
		screen.blit(displayMAF, (610, 170))
		screen.blit(displayIntakeTemp, (615, 310))

		renderRecs()
		renderText()

		for posX in range(40, 41 + 30*(rpmValue - 2), 30):
			pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
			for negX in range(40 + 30*(rpmValue - 1),751, 30):
				pygame.draw.rect(screen, (0,0,0), pygame.Rect((negX, 10), (25, 100)))

		# Update display
		pygame.display.update()

## function to render text labels for data points
def renderText():
	speedLabel = font.render("SPEED", True, (255, 255, 255))
	airLabel = font.render("MAF", True, (255,255,255))
	intakeLabel = font.render("INTAKE TEMP", True, (255,255,255))
	oilLabel = font.render("OIL TEMP", True, (255,255,255))
	logo = pygame.image.load("/home/asubach/CS121/project/subaru_logo.png").convert()
	screen.blit(logo, (225,120))
	screen.blit(speedLabel, (50, 115))
	screen.blit(oilLabel, (15, 255))
	screen.blit(airLabel, (640, 115))
	screen.blit(intakeLabel,(590, 255))


## function to render data outlines
def renderRecs():
	recDataOutlineSpeed  = pygame.Rect((10,145), (175, 100))
	recDataOutlineIntake = pygame.Rect((10, 285), (175, 100))
	recDataOutlineOil = pygame.Rect((600, 145), (175, 100))
	recDataOutlineMAF = pygame.Rect((600, 285), (175, 100))

	for posX in range(40, 740, 30):
		pygame.draw.rect(screen,(255,255,255), pygame.Rect((posX, 10), (25, 100)), 4)

	pygame.draw.rect(screen, (255,255,255), recDataOutlineSpeed, 4) ## outline for speed data
	pygame.draw.rect(screen, (255,255,255), recDataOutlineIntake, 4) ## outline for intake temp data
	pygame.draw.rect(screen, (255,255,255), recDataOutlineOil, 4)  ## outline for oil temp data
	pygame.draw.rect(screen, (255,255,255), recDataOutlineMAF, 4) ## outline for mass air flow data

def new_rpm(r):
	rpm_file = open('rpms.txt', 'w')
	print(r.value, file = rpm_file)
	rpm_file.close()

if __name__ == "__main__":
	main()
