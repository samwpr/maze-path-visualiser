import gui
import settings

class MainMenu:
    def __init__(self, screen):
        # image
        self.logoImage = gui.Image(screen, "assets/images/Logo.png", (settings.SCREEN_WIDTH // 2, -20), size=(600, 338))

        # creation of the texts
        self.mainMenuTexts = []  # all the menu texts will be put in this list

        self.mainMenuTexts.append(gui.Text(screen, text="The A{mazing} Maze", pos=(settings.SCREEN_WIDTH // 2, 340),
                                           fontSize=int(settings.DEFAULT_FONT_SIZE * 1.5)))

        self.mainMenuTexts.append(gui.Paragraph(screen, xPos=None, yStartPos=380,
                                                text="To help teachers be more effective in their class\n"
                                                     "To help students learn interactively and quickly"))

        self.mainMenuTexts.append(gui.Text(screen, text= "The A{gile} Team",
                                           pos=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 20),
                                           color=settings.GRAY, fontSize=20))

        # creation of the buttons
        self.mazeGeneratorButton = gui.Button(screen, pos=(settings.SCREEN_WIDTH // 2, 520),
                                              text="START")

        # self.smartSolverButton = gui.Button(screen, pos=(settings.SCREEN_WIDTH // 2 + 135, 480), text="Smart Solver")

        self.aboutPageButton = gui.Button(screen, pos=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 90),
                                          color=settings.BACKGROUND_COLOR,
                                          text="About The Game", textColor=settings.BLACK, textUnderline=True,
                                          outlineActivate=False)

    def run(self, isLeftMouseButtonPressed):
        """Makes the main menu functional"""
        # draws the image
        self.logoImage.draw()

        # draws the texts
        for text in self.mainMenuTexts:
            text.draw()

        # draw the buttons and makes them clickable
        if self.mazeGeneratorButton.run(isLeftMouseButtonPressed):  # redirect the user to the MazeGenerator page
            return "mazeGenerator"

        # self.smartSolverButton.run(isLeftMouseButtonPressed)  # not needed any more

        if self.aboutPageButton.run(isLeftMouseButtonPressed):  # redirect the user to the about page
            return "aboutPage"

