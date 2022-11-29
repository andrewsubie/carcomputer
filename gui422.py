## imports
import time
import datetime
import obd
import pygame
from sys import exit

## increment for running tach GUI
RPM_INCREMENT = 250

## intializing pygame and display
pygame.init()
font = pygame.font.SysFont("FreeSans", 36)
pygame.font.init()
screen = pygame.display.set_mode((800,400))
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

	while True:
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
		rpm = file.readline()
		rpm = rpm[0:rpm.find(".")]
		rpmValue = int(rpm) // RPM_INCREMENT
		file.close()

		#rendder data values into font objects
		displaySpeed = font.render(speedValue, True, (255,255,255))
		displayOilTemp = font.render(oilTempValue, True, (255,255,255))
		displayMAF = font.render(mafValue, True, (255,255,255))
		displayIntakeTemp = font.render(intakeTempValue, True, (255,255,255))

		#display data to user on screen
		screen.blit(displaySpeed, (30, 150))
		screen.blit(displayOilTemp, (30, 290))
		screen.blit(displayMAF, (610, 150))
		screen.blit(displayIntakeTemp, (610, 290))

		renderRecs()
		renderText()

		if rpmValue == 2:
			for posX in range(40, 41, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 3:
			for posX in range(40, 71, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 4:
			for posX in range(40, 101, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 5:
			for posX in range(40, 131, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 6:
			for posX in range(40, 161, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 7:
			for posX in range(40, 191, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 8:
			for posX in range(40, 221, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 9:
			for posX in range(40, 251, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 10:
			for posX in range(40, 281, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 11:
			for posX in range(40, 311, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 12:
			for posX in range(40, 341, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 13:
			for posX in range(40, 371, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 14:
			for posX in range(40, 401, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 15:
			for posX in range(40, 431, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 16:
			for posX in range(40, 461, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 17:
			for posX in range(40, 491, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 18:
			for posX in range(40, 521, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 19:
			for posX in range(40, 551, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 20:
			for posX in range(40, 581, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 21:
			for posX in range(40, 611, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 22:
			for posX in range(40, 641, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))
		elif rpmValue == 23:
			for posX in range(40, 671, 30):
				pygame.draw.rect(screen, (255,0,0), pygame.Rect((posX, 10), (25, 100)))

		# Update display
		pygame.display.update()

## function to render text labels for data points
def renderText():
	speedLabel = font.render("SPEED", True, (255, 255, 255))
	oilLabel = font.render("OIL TEMP", True, (255,255,255))
	volumeLabel = font.render("MAF", True, (255,255,255))
	airLabel = font.render("INTAKE TEMP", True, (255,255,255))
	screen.blit(speedLabel, (55, 120))
	screen.blit(airLabel, (15, 260))
	screen.blit(oilLabel, (630, 120))
	screen.blit(volumeLabel,(665, 260))

## function to render data outlines
def renderRecs():
	recDataOutlineSpeed  = pygame.Rect((10,145), (175, 100))
	recDataOutlineIntake = pygame.Rect((10, 285), (175, 100))
	recDataOutlineOil = pygame.Rect((600, 145), (175, 100))
	recDataOutlineMAF = pygame.Rect((600, 285), (175, 100))
	# recTachOutline =

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
