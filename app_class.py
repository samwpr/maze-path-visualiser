import pygame
import os
import sys
import settings
from mainMenu import MainMenu
from aboutPage import AboutPage
from smartSolverPage import SmartSolverPage
from mazeGeneratorPage import MazeGeneratorPage


class App:
    def __init__(self):
        # Setup pygame/window
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 32)  # windows position on the user screen
        pygame.init()
        pygame.display.set_caption(settings.WINDOW_NAME)  # name of the app window
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), 0, 32)

        # creation of the pages
        self.mainMenu = MainMenu(self.screen)
        self.aboutPage = AboutPage(self.screen)
        self.mazeGeneratorPage = MazeGeneratorPage(self.screen)
        self.smartSolverPage = SmartSolverPage(self.screen, self.mazeGeneratorPage)

    def checkQuit(self, events):
        """ Checks if the user wants to close the app"""
        for event in events:
            if event.type == pygame.QUIT:  # checks if the user is pressing on the window close button
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # checks if the user is pressing the ESC key
                    pygame.quit()
                    sys.exit()

    def getEvents(self):
        """ pygame.event.get() should only be called one time in the loop and will be used several time throughout
                the program
            :return: the user events (for example the key pressed, mouse click...)
        """
        return pygame.event.get()

    def isLeftMouseButtonPressed(self, events):
        """
            :param events: all user events
            :return: True if the left mouse button is pressed
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return True
        return False

    def scrollValue(self, events):
        """
        :param events: all user events
        :return: 1 if scroll down, -1 if scroll up
        """
        for event in events:
            if event.type == pygame.MOUSEWHEEL:
                return event.y
        return 0

    def run(self):
        """ Makes the app run"""
        state = "mainMenu"

        while True:
            # get the events and quit the app if needed
            events = self.getEvents()
            isLeftMouseButtonPressed = self.isLeftMouseButtonPressed(events)
            self.checkQuit(events)

            # makes the main menu functional
            if state == "mainMenu":
                nextState = self.mainMenu.run(isLeftMouseButtonPressed)
                if nextState == "mazeGenerator":
                    # reset the Maze Generator page
                    self.mazeGeneratorPage.bigReset()
                    self.mazeGeneratorPage.mazeNumber = 1

            # makes the about page functional
            elif state == "aboutPage":
                nextState = self.aboutPage.run(isLeftMouseButtonPressed)

            # makes the main menu functional
            elif state == "mazeGenerator":
                nextState = self.mazeGeneratorPage.run(isLeftMouseButtonPressed)
                if nextState == "smartSolver":
                    self.smartSolverPage.reset()  # reset the Smart Solver page

            # makes the smart solver page functional
            elif state == "smartSolver":
                nextState = self.smartSolverPage.run(isLeftMouseButtonPressed, self.scrollValue(events))

            else:  # error message if the state does not exist
                print(f"The state {state} does not exist")
                break

            state = nextState if nextState is not None else state  # change to the new state if it is not None

            # update the screen
            pygame.display.update()
            self.screen.fill(settings.BACKGROUND_COLOR)
