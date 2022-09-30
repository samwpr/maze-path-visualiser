import pygame
import settings


class Text:
    def __init__(self, surface, text, pos, positionType="center", color=settings.DEFAULT_TEXT_COLOR,
                 font=settings.DEFAULT_FONT, fontSize=settings.DEFAULT_FONT_SIZE, underline=False, backgroundColor=None):
        """ Create the label and define the position of the text

            :param surface: place where the text will be drawn
            :param positionType: align the text to the pos with different manner (could be: center, topleft or topright)
            :param underline: sets whether the font should be rendered with an underline
            :param backgroundColor: color behind the text
        """
        self.surface = surface
        self.text = text
        self.pos = pos
        self.font = font
        self.fontSize = fontSize
        self.underline = underline
        self.color = color
        self.backgroundColor = backgroundColor
        self.positionType = positionType
        self.makeLabel(self.text)

    def makeLabel(self, text):
        """ create the label (text with the correct font and size and with an underline if needed)"""
        label = pygame.font.SysFont(self.font, self.fontSize)
        label.set_underline(self.underline)
        self.label = label.render(text, True, self.color, self.backgroundColor)
        # define the position of the label(=text)
        self.labelRect = self.label.get_rect()
        if self.positionType == "center":  # will center the text on the pos
            self.labelRect.center = self.pos
        elif self.positionType == "topleft":  # the top left of the text will be on the pos
            self.labelRect.topleft = self.pos
        elif self.positionType == "topright":  # the top right of the text will be on the pos
            self.labelRect.topright = self.pos

    def addText(self, text):
        """add some text to the preexisting text  """
        self.makeLabel(self.text + text)

    def draw(self, yOffset=0):
        labelRect = self.labelRect.copy()
        labelRect.y += yOffset
        self.surface.blit(self.label, labelRect)


class Paragraph:
    """ Create a multi-line text"""

    def __init__(self, surface, xPos, yStartPos, text, lineSpacing=12, color=settings.DEFAULT_TEXT_COLOR,
                 font=settings.DEFAULT_FONT, fontSize=settings.DEFAULT_FONT_SIZE, underline=False, backgroundColor=None):
        """
            :param xPos: the x position of the text, if xPos=None the line will be center on the screen
            :param yStartPos: the y start pos of the text
            :param text: String that can contain \n to start a new line
            :param lineSpacing: additional space between lines
            :param backgroundColor: color behind the text
        """
        self.paragraph = []
        yOffset = 0
        for nb, line in enumerate(text.split("\n")):  # create every line of the paragraph
            yPos = yStartPos + nb * lineSpacing + yOffset
            if xPos is None:  # will center the line on the screen
                self.paragraph.append(Text(surface, line, (settings.SCREEN_WIDTH // 2, yPos), positionType="center",
                                           color=color, font=font, fontSize=fontSize, underline=underline, backgroundColor=backgroundColor))
            else:  # the line will start at the xPos coord
                self.paragraph.append(Text(surface, line, (xPos, yPos), positionType="topleft",
                                           color=color, font=font, fontSize=fontSize, underline=underline, backgroundColor=backgroundColor))
            yOffset += self.paragraph[-1].label.get_height() / 2  # add the height of the line to the yOffset

    def addText(self, *text):
        """ add some text to the end of the lines
            for example addText("a", "bb") will add "a" at the end of the first line and "bb" to the second

            :param text: text that will be added to the line of the paragraph, if text = None, it will not change the text
            :return:
        """
        for lineNb, line in enumerate(text):
            if line is None:
                continue
            self.paragraph[lineNb].addText(str(line))

    def resetText(self):
        """ remove all text that has been added with the method addText
        """
        for line in self.paragraph:
            line.addText("")

    def getLastLineYPos(self):
        return self.paragraph[-1].pos[1]

    def draw(self, yOffset=0):
        for line in self.paragraph:
            line.draw(yOffset)


class Button:
    def __init__(self, surface, pos, color=settings.DEFAULT_BUTTON_COLOR, rectSize=settings.DEFAULT_BUTTON_SIZE,
                 text="",
                 textColor=settings.DEFAULT_BUTTON_TEXT_COLOR, textUnderline=False, font=settings.DEFAULT_BUTTON_FONT,
                 fontSize=settings.DEFAULT_BUTTON_FONT_SIZE, roundedCornerRadius=settings.DEFAULT_ROUNDED_CORNER,
                 outlineActivate=True, outlineRadius=settings.DEFAULT_OUTLINE_RADIUS,
                 outlineColor=settings.DEFAULT_OUTLINE_COLOR, zoomFactor=settings.DEFAULT_BUTTON_ZOOM_FACTOR):
        """ Create the button rect, text and outline
            :param pos: define the X and Y pos of the button (the button will be center on the X pos)
            :param rectSize: define the size of the button: (width, height)
            :param roundedCornerRadius: makes rounded corners to the button rect(0 to deactivate)
            :param outlineActivate: will make the button outline when the mouse is over the button
            :param outlineRadius: will make an outline of X px when the mouse is over the button
            :param outlineColor: color of the outline when the mouse is over the button
            :param zoomFactor: will make the text bigger when the mouse is over the button (0 or False to deactivate)
        """
        self.surface = surface
        self.color = color
        self.roundedCornerRadius = roundedCornerRadius  # makes rounded corners (0 to deactivate)
        self.zoomFactor = zoomFactor
        self.isSelected = False

        self.rect = pygame.rect.Rect((pos[0] - rectSize[0] // 2, pos[1]),
                                     rectSize)  # button rect (contain the x, y, width and height of a rectangle)

        self.text = Text(surface, text, self.rect.center, positionType="center", color=textColor, font=font,
                         fontSize=fontSize, underline=textUnderline)
        self.zoomText = Text(surface, text, self.rect.center, positionType="center", color=textColor, font=font,
                             fontSize=fontSize+zoomFactor, underline=textUnderline)

        self.outlineActivate = outlineActivate  # will make the button outline if the mouse is over the button
        self.outlineColor = outlineColor
        self.outlineRect = pygame.rect.Rect((pos[0] - rectSize[0] // 2 - outlineRadius, pos[1] - outlineRadius),
                                            (rectSize[0] + 2 * outlineRadius, rectSize[1] + 2 * outlineRadius))

    def isMouseOnButton(self):
        """:return: 1 if the mouse is over the button
        """
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def draw(self):
        # draw the outline
        if self.outlineActivate and self.isMouseOnButton():
            pygame.draw.rect(self.surface, self.outlineColor, self.outlineRect, border_radius=self.roundedCornerRadius)
        # draw the rectangle
        if self.isSelected:
            color = settings.DEFAULT_BUTTON_SELECTED_COLOR
        else:
            color = self.color
        pygame.draw.rect(self.surface, color, self.rect, border_radius=self.roundedCornerRadius)
        # draw the text
        if self.zoomFactor and self.isMouseOnButton():
            self.zoomText.draw()
        else:
            self.text.draw()

    def run(self, isLeftMouseButtonPressed):
        """makes the button functional
        :return: True if the button is pressed
        """
        self.draw()
        if self.isMouseOnButton() and isLeftMouseButtonPressed:
            return True


class Image:
    def __init__(self, surface, path, pos, positionType="centerx", size="default", convert="alpha", flip=False):
        """ Load and scale an image
        :param surface: where to draw the image
        :param path: path of the image
        :param pos: position of the image
        :param positionType: "centerx" -> center the image X coord on the position
        :param size: "default" -> will not change the size, (width, height) -> will scale the image
        """
        self.surface = surface
        self.image = self.load(path, size, convert, flip)

        if positionType == "centerx":  # center the image X coord on the position
            pos = list(pos)
            pos[0] -= self.image.get_width() // 2
        self.pos = pos

    def load(self, path, size="default", convert="alpha", flip=False):
        if convert == "alpha":
            image = pygame.image.load(path).convert_alpha()
        else:
            image = pygame.image.load(path).convert()
        if flip:
            image = pygame.transform.flip(image, True, False)
        if size != "default":
            image = self.scale(image, size)

        return image

    def scale(self, image, size):
        return pygame.transform.smoothscale(image, size)

    def draw(self):
        self.surface.blit(self.image, self.pos)
