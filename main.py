# importing and initiating the program
import pygame
import sys
from Planet import *

pygame.init()
pygame.font.init()

password = "hapaxlogonamanon"

# defining the colours
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 145, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
grey = (220, 220, 220)
l_blue = (28, 222, 229)
d_grey = (105, 105, 105)
yellow = (245, 245, 66)

screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Solar System")
icon = pygame.image.load("Solar.jpg")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

Mercury = planetstats(screen, 60, "Mercury", 3, d_grey, 70, 20, 50, 500, 250, 100, 20)
Venus = planetstats(screen, 70, "Venus", 3, red, 60, 20, 55, 500, 250, 60, 20)
Earth = planetstats(screen, 90, "Earth", 10, l_blue, 50, 20, 50, 500, 250, 100, 20)
Mars = planetstats(screen, 120, "Mars", 7, orange, 40, 20, 50, 500, 250, 50, 20)
Jupiter = planetstats(screen, 170, "Jupiter", 40, grey, 30, 20, 50, 500, 250, 80, 20)
Saturn = planetstats(screen, 240, "Saturn", 25, yellow, 20, 20, 50, 500, 250, 70, 20)
Ur_anus = planetstats(screen, 300, "Uranus", 20, l_blue, 15, 20, 50, 500, 250, 60, 20)
Neptune = planetstats(screen, 350, "Neptune", 20, blue, 10, 20, 50, 500, 250, 10, 20)


def menu():
    global event
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        # registers mouse position
        mouseposition = pygame.mouse.get_pos()
        print(mouseposition)

        pygame.draw.rect(screen, red, [80, 255, 175, 60], 2)
        pygame.draw.rect(screen, blue, [500, 255, 150, 60], 2)

        if event.type == pygame.MOUSEBUTTONDOWN and 114 < mouseposition[0] < 192 and 368 < mouseposition[1] < 418:
            mercurytab()

        if event.type == pygame.MOUSEBUTTONDOWN and 206 < mouseposition[0] < 220 and 368 < mouseposition[1] < 418:
            venustab()

        if event.type == pygame.MOUSEBUTTONDOWN and 280 < mouseposition[0] < 335 and 368 < mouseposition[1] < 418:
            earthtab()

        if event.type == pygame.MOUSEBUTTONDOWN and 361 < mouseposition[0] < 411 and 368 < mouseposition[1] < 418:
            marstab()

        if event.type == pygame.MOUSEBUTTONDOWN and 446 < mouseposition[0] < 508 and 368 < mouseposition[1] < 418:
            jupitertab()

        if event.type == pygame.MOUSEBUTTONDOWN and 538 < mouseposition[0] < 600 and 368 < mouseposition[1] < 418:
            saturntab()

        if event.type == pygame.MOUSEBUTTONDOWN and 623 < mouseposition[0] < 691 and 368 < mouseposition[1] < 418:
            uranustab()

        if event.type == pygame.MOUSEBUTTONDOWN and 715 < mouseposition[0] < 790 and 368 < mouseposition[1] < 418:
            neptunetab()

        if event.type == pygame.MOUSEBUTTONDOWN and 80 < mouseposition[0] < 255 and 256 < mouseposition[1] < 315:
            solarsubmenu()

        if event.type == pygame.MOUSEBUTTONDOWN and 502 < mouseposition[0] < 649 and 255 < mouseposition[1] < 315:
            instructionsubmenu()

        # changes colour of bg/drawing rectangles
        screen.fill(black)
        pygame.draw.rect(screen, red, [80, 255, 175, 60], 2)
        pygame.draw.rect(screen, blue, [500, 255, 150, 60], 2)
        # setting different fonts and adding them to the screen surface
        headingfont = pygame.font.SysFont("comicsans", 25, True, False)
        heading = headingfont.render("Solar System Main Menu!", True, white)
        screen.blit(heading, [50, 50])

        button1font = pygame.font.SysFont("comicsans", 25, True, False)
        buttontxt = button1font.render("Solar System", True, red)
        screen.blit(buttontxt, [89, 280])

        button2font = pygame.font.SysFont("comicsans", 25, True, False)
        button2txt = button2font.render("Instructions", True, blue)
        screen.blit(button2txt, [505, 270])

        menuimage = pygame.image.load("planets.jpg")
        screen.blit(pygame.transform.scale(menuimage, (300, 300)), (380, -50))

        mercury1font = pygame.font.SysFont("comicsans", 25, True, False)
        mercury1txt = mercury1font.render("Mercury", True, d_grey)
        screen.blit(mercury1txt, [115, 381])

        venus1font = pygame.font.SysFont("comicsans", 25, True, False)
        venus1txt = venus1font.render("Venus", True, red)
        screen.blit(venus1txt, [205, 381])

        earth1font = pygame.font.SysFont("comicsans", 25, True, False)
        earth1txt = earth1font.render("Earth", True, l_blue)
        screen.blit(earth1txt, [285, 381])

        mars1font = pygame.font.SysFont("comicsans", 25, True, False)
        mars1txt = mars1font.render("Mars", True, orange)
        screen.blit(mars1txt, [365, 381])

        jupiter1font = pygame.font.SysFont("comicsans", 25, True, False)
        jupiter1txt = jupiter1font.render("Jupiter", True, grey)
        screen.blit(jupiter1txt, [445, 381])

        saturn1font = pygame.font.SysFont("comicsans", 25, True, False)
        saturn1txt = saturn1font.render("Saturn", True, yellow)
        screen.blit(saturn1txt, [535, 381])

        uranus1font = pygame.font.SysFont("comicsans", 25, True, False)
        uranus1txt = uranus1font.render("Uranus", True, l_blue)
        screen.blit(uranus1txt, [625, 381])

        neptune1font = pygame.font.SysFont("comicsans", 25, True, False)
        neptune1txt = neptune1font.render("Neptune", True, blue)
        screen.blit(neptune1txt, [715, 381])

        planetsand1font = pygame.font.SysFont("comicsans", 25, True, False)
        planetsand1txt = planetsand1font.render("Neptune", True, blue)
        screen.blit(planetsand1txt, [715, 381])

        solarplanets = pygame.font.SysFont("comicsans", 40, True, False)
        solarplanetstxt = solarplanets.render("Planets!", True, white)
        screen.blit(solarplanetstxt, [310, 272])

        pygame.display.update()


def solarsubmenu():
    global event
    end = False
    solarsystem = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Ur_anus, Neptune]
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        mouseposition = pygame.mouse.get_pos()
        print(mouseposition)
        headingfont2 = pygame.font.SysFont("Calibri", 18, True, False)
        heading2 = headingfont2.render("The Solar System", True, red)
        screen.blit(heading2, [30, 30])

        if 53 < mouseposition[0] < 127 and 45 < mouseposition[1] < 66:
            mercurytab()

        if 53 < mouseposition[0] < 127 and 86 < mouseposition[1] < 100:
            venustab()

        if 53 < mouseposition[0] < 127 and 119 < mouseposition[1] < 133:
            earthtab()

        if 53 < mouseposition[0] < 127 and 152 < mouseposition[1] < 165:
            marstab()

        if 53 < mouseposition[0] < 127 and 185 < mouseposition[1] < 200:
            jupitertab()

        if 53 < mouseposition[0] < 127 and 217 < mouseposition[1] < 231:
            saturntab()

        if 53 < mouseposition[0] < 127 and 250 < mouseposition[1] < 264:
            uranustab()

        if 53 < mouseposition[0] < 127 and 283 < mouseposition[1] < 300:
            neptunetab()

        screen.fill(black)

        spaceimage = pygame.image.load("outerspace.jpg")
        screen.blit(pygame.transform.scale(spaceimage, (1000, 500)), (0, 0))

        pygame.draw.rect(screen, blue, [10, 380, 70, 60], 2)
        pygame.draw.circle(screen, orange, (500, 250), 50)

        planetstats.drawplanetboi(Mercury)
        planetstats.drawplanetboi(Venus)
        planetstats.drawplanetboi(Earth)
        planetstats.drawplanetboi(Mars)
        planetstats.drawplanetboi(Jupiter)
        planetstats.drawplanetboi(Saturn)
        planetstats.drawplanetboi(Ur_anus)
        planetstats.drawplanetboi(Neptune)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            for planet in solarsystem:
                planet.speedup()

        if keys[pygame.K_DOWN]:
            for planet in solarsystem:
                planet.slowdown()

        if keys[pygame.K_SPACE]:
            for planet in solarsystem:
                planet.stop()

        if keys[pygame.K_b]:
            for planet in solarsystem:
                planet.bigger()

        if keys[pygame.K_s]:
            for planet in solarsystem:
                planet.smaller()

        if keys[pygame.K_c]:
            for planet in solarsystem:
                planet.crazy()

        mercuryfont = pygame.font.SysFont("comicsans", 25, True, False)
        mercurytxt = mercuryfont.render("Mercury", True, d_grey)
        screen.blit(mercurytxt, [50, 50])

        venusfont = pygame.font.SysFont("comicsans", 25, True, False)
        venustxt = venusfont.render("Venus", True, red)
        screen.blit(venustxt, [50, 83])

        earthfont = pygame.font.SysFont("comicsans", 25, True, False)
        earthtxt = earthfont.render("Earth", True, l_blue)
        screen.blit(earthtxt, [50, 116])

        marsfont = pygame.font.SysFont("comicsans", 25, True, False)
        marstxt = marsfont.render("Mars", True, orange)
        screen.blit(marstxt, [50, 149])

        jupiterfont = pygame.font.SysFont("comicsans", 25, True, False)
        jupitertxt = jupiterfont.render("Jupiter", True, grey)
        screen.blit(jupitertxt, [50, 182])

        saturnfont = pygame.font.SysFont("comicsans", 25, True, False)
        saturntxt = saturnfont.render("Saturn", True, yellow)
        screen.blit(saturntxt, [50, 215])

        uranusfont = pygame.font.SysFont("comicsans", 25, True, False)
        uranustxt = uranusfont.render("Uranus", True, l_blue)
        screen.blit(uranustxt, [50, 248])

        neptunefont = pygame.font.SysFont("comicsans", 25, True, False)
        neptunetxt = neptunefont.render("Neptune", True, blue)
        screen.blit(neptunetxt, [50, 281])

        solarbuttonfont = pygame.font.SysFont("comicsans", 20, True, False)
        solarbuttontxt = solarbuttonfont.render("Return", True, blue)
        screen.blit(solarbuttontxt, [22, 400])

        if event.type == pygame.MOUSEBUTTONDOWN and 10 < mouseposition[0] < 80 and 380 < mouseposition[1] < 445:
            menu()

        pygame.display.update()


def instructionsubmenu():
    global event
    screen.fill(black)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        background = pygame.image.load("space.jpg")

        screen.blit(background, (0, 0))

        instructionsinfofont = pygame.font.SysFont("comicsans", 25, True, False)
        instructionsinfo = instructionsinfofont.render(
            "space bar to stop planets up arrow to speed up planets down arrow to slow planets", True, white)
        screen.blit(instructionsinfo, [50, 83])

        instructionsinfofont = pygame.font.SysFont("comicsans", 25, True, False)
        instructionsinfo2 = instructionsinfofont.render("b to increase radius s to decrease check nasa for real facts",
                                                        True, white)
        screen.blit(instructionsinfo2, [50, 115])

        instructionstitlefont = pygame.font.SysFont("comicsans", 40, True, False)
        instructionstitletxt = instructionstitlefont.render("Instructions", True, white)
        screen.blit(instructionstitletxt, [450, 22])

        mouseposition = pygame.mouse.get_pos()
        print(mouseposition)

        pygame.draw.rect(screen, white, [80, 350, 175, 60], 2)

        instructionsbuttonfont = pygame.font.SysFont("comicsans", 40, True, False)
        instructionsbuttontxt = instructionsbuttonfont.render("Return", True, white)
        screen.blit(instructionsbuttontxt, [103, 365])

        if event.type == pygame.MOUSEBUTTONDOWN and 83 < mouseposition[0] < 252 and 348 < mouseposition[1] < 403:
            menu()

        pygame.display.update()


def mercurytab():
    global event
    screen.fill(black)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        mercuryimage = pygame.image.load("mercury.png")
        screen.blit(pygame.transform.scale(mercuryimage, (1000, 500)), (0, 0))

        mercuryinfofont = pygame.font.SysFont("comicsans", 25, True, False)
        mercuryinfo = mercuryinfofont.render("smol", True, d_grey)
        screen.blit(mercuryinfo, [50, 83])

        mercurytitlefont = pygame.font.SysFont("comicsans", 40, True, False)
        mercurytitletxt = mercurytitlefont.render("Mercury", True, d_grey)
        screen.blit(mercurytitletxt, [450, 22])

        mouseposition = pygame.mouse.get_pos()
        print(mouseposition)

        pygame.draw.rect(screen, white, [400, 420, 175, 60], 2)

        instructionsbuttonfont = pygame.font.SysFont("comicsans", 40, True, False)
        instructionsbuttontxt = instructionsbuttonfont.render("Return", True, grey)
        screen.blit(instructionsbuttontxt, [430, 430])

        if event.type == pygame.MOUSEBUTTONDOWN and 403 < mouseposition[0] < 576 and 422 < mouseposition[1] < 480:
            menu()

        pygame.display.update()


def venustab():
    global event
    screen.fill(black)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        venusimage = pygame.image.load("venus.jpg")
        screen.blit(pygame.transform.scale(venusimage, (1000, 500)), (0, 0))

        venusinfofont = pygame.font.SysFont("comicsans", 25, True, False)
        venusinfo = venusinfofont.render("pretty sure there's a song about this one", True, red)
        screen.blit(venusinfo, [50, 83])

        venustitlefont = pygame.font.SysFont("comicsans", 40, True, False)
        venustitletxt = venustitlefont.render("Venus", True, red)
        screen.blit(venustitletxt, [450, 22])

        mouseposition = pygame.mouse.get_pos()
        print(mouseposition)

        pygame.draw.rect(screen, red, [400, 420, 175, 60], 2)

        instructionsbuttonfont = pygame.font.SysFont("comicsans", 40, True, False)
        instructionsbuttontxt = instructionsbuttonfont.render("Return", True, red)
        screen.blit(instructionsbuttontxt, [430, 430])

        if event.type == pygame.MOUSEBUTTONDOWN and 403 < mouseposition[0] < 576 and 422 < mouseposition[1] < 480:
            menu()

        pygame.display.update()


def earthtab():
    global event
    screen.fill(black)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        earthimage = pygame.image.load("earth.jpg")
        screen.blit(pygame.transform.scale(earthimage, (1000, 500)), (0, 0))

        earthinfofont = pygame.font.SysFont("comicsans", 25, True, False)
        earthinfo = earthinfofont.render("It means dirt we literally live on a planet called dirt", True, l_blue)
        screen.blit(earthinfo, [50, 83])

        earthtitlefont = pygame.font.SysFont("comicsans", 40, True, False)
        earthtitletxt = earthtitlefont.render("Earth", True, l_blue)
        screen.blit(earthtitletxt, [450, 22])
        mouseposition = pygame.mouse.get_pos()
        print(mouseposition)

        pygame.draw.rect(screen, l_blue, [400, 420, 175, 60], 2)

        instructionsbuttonfont = pygame.font.SysFont("comicsans", 40, True, False)
        instructionsbuttontxt = instructionsbuttonfont.render("Return", True, l_blue)
        screen.blit(instructionsbuttontxt, [430, 430])

        if event.type == pygame.MOUSEBUTTONDOWN and 403 < mouseposition[0] < 576 and 422 < mouseposition[1] < 480:
            menu()

        pygame.display.update()


def marstab():
    global event
    screen.fill(black)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        marsinfofont = pygame.font.SysFont("comicsans", 25, True, False)

        marsimage = pygame.image.load("mars.jpg")
        screen.blit(pygame.transform.scale(marsimage, (1000, 500)), (0, 0))

        marsinfo = marsinfofont.render("Elon's favorite", True, orange)
        screen.blit(marsinfo, [50, 83])

        marstitlefont = pygame.font.SysFont("comicsans", 40, True, False)
        marstitletxt = marstitlefont.render("Mars", True, orange)
        screen.blit(marstitletxt, [450, 22])
        mouseposition = pygame.mouse.get_pos()
        print(mouseposition)

        pygame.draw.rect(screen, orange, [400, 420, 175, 60], 2)

        instructionsbuttonfont = pygame.font.SysFont("comicsans", 40, True, False)
        instructionsbuttontxt = instructionsbuttonfont.render("Return", True, orange)
        screen.blit(instructionsbuttontxt, [430, 430])

        if event.type == pygame.MOUSEBUTTONDOWN and 403 < mouseposition[0] < 576 and 422 < mouseposition[1] < 480:
            menu()

        pygame.display.update()


def jupitertab():
    global event
    screen.fill(black)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        jupiterimage = pygame.image.load("jupiter.jpg")
        screen.blit(pygame.transform.scale(jupiterimage, (1000, 500)), (0, 0))

        jupiterinfofont = pygame.font.SysFont("comicsans", 25, True, False)
        jupiterinfo = jupiterinfofont.render("Big Lol", True, grey)
        screen.blit(jupiterinfo, [50, 83])

        jupitertitlefont = pygame.font.SysFont("comicsans", 40, True, False)
        jupitertitletxt = jupitertitlefont.render("Jupiter", True, grey)
        screen.blit(jupitertitletxt, [450, 22])
        mouseposition = pygame.mouse.get_pos()
        print(mouseposition)

        pygame.draw.rect(screen, grey, [400, 420, 175, 60], 2)

        instructionsbuttonfont = pygame.font.SysFont("comicsans", 40, True, False)
        instructionsbuttontxt = instructionsbuttonfont.render("Return", True, grey)
        screen.blit(instructionsbuttontxt, [430, 430])

        if event.type == pygame.MOUSEBUTTONDOWN and 403 < mouseposition[0] < 576 and 422 < mouseposition[1] < 480:
            menu()

        pygame.display.update()


def saturntab():
    global event
    screen.fill(black)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        saturninfofont = pygame.font.SysFont("comicsans", 25, True, False)

        saturnimage = pygame.image.load("saturn.jpg")
        screen.blit(pygame.transform.scale(saturnimage, (1000, 500)), (0, 0))

        saturninfo = saturninfofont.render("Saturn's only defining feature is large rings lol", True, yellow)
        screen.blit(saturninfo, [50, 83])

        saturntitlefont = pygame.font.SysFont("comicsans", 40, True, False)
        saturntitletxt = saturntitlefont.render("Saturn", True, yellow)
        screen.blit(saturntitletxt, [450, 22])
        mouseposition = pygame.mouse.get_pos()
        print(mouseposition)

        pygame.draw.rect(screen, yellow, [400, 420, 175, 60], 2)

        instructionsbuttonfont = pygame.font.SysFont("comicsans", 40, True, False)
        instructionsbuttontxt = instructionsbuttonfont.render("Return", True, yellow)
        screen.blit(instructionsbuttontxt, [430, 430])

        if event.type == pygame.MOUSEBUTTONDOWN and 403 < mouseposition[0] < 576 and 422 < mouseposition[1] < 480:
            menu()

        pygame.display.update()


def uranustab():
    global event
    screen.fill(black)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        uranusimage = pygame.image.load("uranus.jpg")
        screen.blit(pygame.transform.scale(uranusimage, (1000, 500)), (0, 0))

        uranusinfofont = pygame.font.SysFont("comicsans", 25, True, False)
        uranusinfo = uranusinfofont.render("too easy", True, l_blue)
        screen.blit(uranusinfo, [50, 83])

        uranustitlefont = pygame.font.SysFont("comicsans", 40, True, False)
        uranustitletxt = uranustitlefont.render("Uranus", True, l_blue)
        screen.blit(uranustitletxt, [450, 22])
        mouseposition = pygame.mouse.get_pos()
        print(mouseposition)

        pygame.draw.rect(screen, l_blue, [400, 420, 175, 60], 2)

        instructionsbuttonfont = pygame.font.SysFont("comicsans", 40, True, False)
        instructionsbuttontxt = instructionsbuttonfont.render("Return", True, l_blue)
        screen.blit(instructionsbuttontxt, [430, 430])

        if event.type == pygame.MOUSEBUTTONDOWN and 403 < mouseposition[0] < 576 and 422 < mouseposition[1] < 480:
            menu()

        pygame.display.update()


def neptunetab():
    global event
    screen.fill(black)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        neptuneimage = pygame.image.load("neptune.jpg")
        screen.blit(pygame.transform.scale(neptuneimage, (1000, 500)), (0, 0))

        neptuneinfofont = pygame.font.SysFont("comicsans", 25, True, False)
        neptuneinfo = neptuneinfofont.render("cold and that", True, blue)
        screen.blit(neptuneinfo, [50, 83])

        neptunetitlefont = pygame.font.SysFont("comicsans", 40, True, False)
        neptunetitletxt = neptunetitlefont.render("Neptune", True, blue)
        screen.blit(neptunetitletxt, [450, 22])
        mouseposition = pygame.mouse.get_pos()
        print(mouseposition)

        pygame.draw.rect(screen, blue, [400, 420, 175, 60], 2)

        instructionsbuttonfont = pygame.font.SysFont("comicsans", 40, True, False)
        instructionsbuttontxt = instructionsbuttonfont.render("Return", True, blue)
        screen.blit(instructionsbuttontxt, [430, 430])

        if event.type == pygame.MOUSEBUTTONDOWN and 403 < mouseposition[0] < 576 and 422 < mouseposition[1] < 480:
            menu()

        pygame.display.update()


menu()


