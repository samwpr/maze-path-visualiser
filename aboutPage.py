import gui
import settings


class AboutPage:
    def __init__(self, screen):
        # creation of the image
        self.logoImage = gui.Image(screen, "assets/images/Logo.png", (settings.SCREEN_WIDTH // 2, -20), size=(600, 338))
        # creation of the texts
        self.aboutPageTexts = []

        self.aboutPageTexts.append(gui.Text(screen, text="About The Game", pos=(settings.SCREEN_WIDTH // 2, 340),
                                            fontSize=int(settings.DEFAULT_FONT_SIZE * 1.5)))

        self.aboutPageTexts.append(gui.Paragraph(screen, xPos=None, yStartPos=380,
                                                 text="Data Structures and Algorithms is considered the hardest module in Computer Science\n\n"
                                                      "It is difficult as the concepts are abstract and complex. However it is an important topic as it is frequently asked during interviews.\n"
                                                      "Having a good understanding will also allow programmers to write good, clean and efficient code.\n\n"
                                                      "We hope through our game we can help students visualise and interact with the concepts taught in their class and coding careers."
                                                      ))

        self.aboutPageTexts.append(
            gui.Text(screen, text="The A{gile} Team", pos=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 20),
                     color=settings.GRAY, fontSize=20))
        # creation of the button
        self.homeButton = gui.Button(screen, pos=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 100),
                                     text="Home")

    def run(self, isLeftMouseButtonPressed):
        # image
        self.logoImage.draw()
        # texts
        for text in self.aboutPageTexts:
            text.draw()
        # button
        if self.homeButton.run(isLeftMouseButtonPressed):  # redirect the user to the main menu page
            return "mainMenu"

