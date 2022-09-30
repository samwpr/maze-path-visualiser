import gui
import settings
import pygame
import tkinter
import tkinter.filedialog
import os
import maze


class MazeGeneratorPage:
    def __init__(self, screen):
        # initialize the needed variables
        self.showMazeGeneratorTipsAndTricks = True
        self.screen = screen
        self.maze = None
        self.isLevelPredefined = False

        # creation of the images
        self.logoImage = gui.Image(screen, "assets/images/Logo.png",
                                   (settings.PANEL_WIDTH // 2, settings.SCREEN_HEIGHT - 115),
                                   size=(249, 135))

        self.dottedGridMImage = gui.Image(screen, "assets/images/Dotted Grid (m).png", (settings.PANEL_WIDTH, 0),
                                          positionType="topleft", size=(918, 680))

        # creation of the texts
        self.titleText = gui.Text(screen, text="Maze Generator", pos=(20, 20), positionType="topleft", fontSize=32,
                                  color=settings.DARK_BLUE)

        self.panelInfosParagraph = gui.Paragraph(screen, xPos=20, yStartPos=60, fontSize=22,
                                                 text="Maze Number: \nMaze file Name: \nMaze Size: \n"
                                                      "\nStats For Nerds \nCells Explored: \nSolution Path: \nTime: ")

        self.mazeGeneratorTipsAndTricksTitleText = gui.Text(screen, text="Tips & Tricks", pos=(
            settings.PANEL_WIDTH + (settings.SCREEN_WIDTH - settings.PANEL_WIDTH) // 2, 80),
                                                            positionType="center", fontSize=72,
                                                            color=settings.DARK_BLUE,
                                                            backgroundColor=settings.WHITE)

        self.mazeGeneratorTipsAndTricksParagraph = gui.Paragraph(screen, xPos=settings.PANEL_WIDTH + 95, yStartPos=150,
                                                                 fontSize=32, color=settings.BLUE,
                                                                 backgroundColor=settings.WHITE, lineSpacing=77,
                                                                 text=
                                                                      "1.Select the level of difficulty for the maze\n"
                                                                      "2.Click on 'Generate Maze'\n"
                                                                      "3.Click on 'Solve Level'\n"
                                                                      "4.Go to 'Smart Solver' when you are ready."
                                                                 )

        self.smartSolverTipsAndTricksTitleText = gui.Text(screen, text="Tips & Tricks", pos=(
            settings.PANEL_WIDTH + (settings.SCREEN_WIDTH - settings.PANEL_WIDTH) // 2, 80),
                                                          positionType="center", fontSize=72,
                                                          color=settings.RED,
                                                          backgroundColor=settings.WHITE)

        self.smartSolverTipsAndTricksParagraph = gui.Paragraph(screen, xPos=settings.PANEL_WIDTH + 95, yStartPos=150,
                                                               fontSize=32, color=settings.LIGHT_RED,
                                                               backgroundColor=settings.WHITE, lineSpacing=77,
                                                               text="1.Click 'Generate Level From Maze Generator'\n"
                                                                    "2.Next Click 'Solve Level'\n"
                                                                    "3.Download New Level File\n"
                                                                    "4.Download Report File\n"
                                                                    "5.Go to Maze Generator to upload new Level")

        # creation of the buttons
        # maze generator buttons
        buttonYStartPos = 200  # the first button y position
        buttonsSpaces = 15  # the space between each buttons
        self.easyButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 1 + settings.DEFAULT_BUTTON_SIZE[1] * 1),
                                     text="Easy")
        self.mediumButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 2 + settings.DEFAULT_BUTTON_SIZE[1] * 2),
                                     text="Medium")
        self.hardButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 3 + settings.DEFAULT_BUTTON_SIZE[1] * 3),
                                     text="Hard")

        self.easierButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 1 + settings.DEFAULT_BUTTON_SIZE[1] * 1),
                                     text="Easier")
        self.harderButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 2 + settings.DEFAULT_BUTTON_SIZE[1] * 2),
                                      text="Harder")

        self.generateMazeButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 4 + settings.DEFAULT_BUTTON_SIZE[1] * 4),
                                             text="Generate Maze")
        self.mazeGeneratorSolveLevelButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 5 + settings.DEFAULT_BUTTON_SIZE[1] * 5),
                                                        text="Solve Level")
        self.goToSmartSolverButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 6 + settings.DEFAULT_BUTTON_SIZE[1] * 6),
                                                text="Go To Smart Solver")
        self.mazeGeneratorHomeButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 7 + settings.DEFAULT_BUTTON_SIZE[1] * 7),
                                                  text="Home", color=settings.GRAY)
        # smart solver buttons
        buttonYStartPos = 200  # the first button y position
        buttonsSpaces = 20  # the space between each buttons
        self.generateLevelFromMazeGeneratorButton = gui.Button(screen, pos=(settings.PANEL_WIDTH // 2, buttonYStartPos),
                                                               text="Generate Level From Maze Generator",
                                                               color=settings.LIGHT_RED)
        # a list containing all buttons
        self.allButtons = [self.easyButton, self.mediumButton, self.hardButton, self.generateMazeButton,
                           self.mazeGeneratorSolveLevelButton, self.goToSmartSolverButton, self.mazeGeneratorHomeButton,
                           self.generateLevelFromMazeGeneratorButton]
        self.reset()


    def bigReset(self):
        self.reset()
        self.avalideDifficultyOptions = {1: True, 2: {"easy": False, "medium": False, "hard": False}}
        self.selectedMazeDifficulty = {1: {"easy": False, "medium": False, "hard": False}, 2: {"easier": False, "harder": False} ,
                                       3: {"easier": False, "harder": False}}
        self.state = 1  # 1 for first maze option
        self.stats = {1: None, 2: None, 3: None}  # store previous maze stat


    def reset(self):
        """reset the needed variables"""
        self.maze = None
        self.panelInfosParagraph.resetText()
        self.showMazeGeneratorTipsAndTricks = True
        self.isLevelPredefined = False

        for b in self.allButtons:
            b.isSelected = False

    def createMazeFromFile(self, filePath):
        with open(filePath, 'r') as f:
            mazeBoard = [list(line.replace("\n", "")) for line in f]
            # convert all the string number to int
            for lineNb in range(len(mazeBoard)):
                for colNb in range(len(mazeBoard[lineNb])):
                    mazeBoard[lineNb][colNb] = int(mazeBoard[lineNb][colNb])
        if "/" in filePath:
            self.fileName = filePath[filePath.rindex("/") + 1: filePath.index(".txt")]  # keeps just the file name
        else:
            self.fileName = filePath
        # self.mazeNumber += 1
        # create the maze
        self.maze = maze.Maze(self.screen, mazeBoard, self.panelInfosParagraph)

    def uploadLevelFileButtonAction(self):
        """ pressing on the 'Upload Level File' button will call this method
            :return fileName: the name of the maze txt file
        """
        # txt file selection prompt
        top = tkinter.Tk()
        top.withdraw()  # hide window
        filePath = tkinter.filedialog.askopenfilename(parent=top, initialdir=os.getcwd(),
                                                      filetypes=(('text files', 'txt'),),
                                                      title="Open your maze text file")
        top.destroy()
        # create the maze board, it first open the text file and try to create the maze
        try:
            self.createMazeFromFile(filePath)
        except Exception as error:
            print(f"{error}\nThe file is not valid... Please try again")

    def run(self, isLeftMouseButtonPressed):
        """make the maze generation page functional"""

        # draws the panel background
        pygame.draw.rect(self.screen, settings.WHITE,
                         (settings.PANEL_WIDTH, 0, settings.SCREEN_WIDTH - settings.PANEL_WIDTH,
                          settings.SCREEN_HEIGHT))  # show the panel
        # image
        # self.logoImage.draw()

        # texts
        self.titleText.draw()
        self.mazeGeneratorTipsAndTricksTitleText.draw()
        self.panelInfosParagraph.draw()

        # buttons
        # first option when the user can select the "easy", "medium" or "hard" option
        if self.state == 1:
            if self.easyButton.run(isLeftMouseButtonPressed):
                if True not in self.selectedMazeDifficulty[1].values():
                    self.isLevelPredefined = True
                    self.easyButton.isSelected = True
                    self.mediumButton.isSelected = False
                    self.hardButton.isSelected = False

            elif self.mediumButton.run(isLeftMouseButtonPressed):
                if True not in self.selectedMazeDifficulty[1].values():
                    self.isLevelPredefined = True
                    self.easyButton.isSelected = False
                    self.mediumButton.isSelected = True
                    self.hardButton.isSelected = False

            elif self.hardButton.run(isLeftMouseButtonPressed):
                if True not in self.selectedMazeDifficulty[1].values():
                    self.isLevelPredefined = True
                    self.easyButton.isSelected = False
                    self.mediumButton.isSelected = False
                    self.hardButton.isSelected = True
        # second option when the user can select the "harder" or "easier" option
        elif self.state == 2:
            if self.easierButton.run(isLeftMouseButtonPressed) and True not in self.selectedMazeDifficulty[2].values():
                self.easierButton.isSelected = True
                self.harderButton.isSelected = False
            if self.harderButton.run(isLeftMouseButtonPressed) and True not in self.selectedMazeDifficulty[2].values():
                self.harderButton.isSelected = True
                self.easierButton.isSelected = False

        # third option when the user can select the "harder" or "easier" option
        elif self.state == 3:
            if self.selectedMazeDifficulty[1]["easy"] or \
                    self.selectedMazeDifficulty[1]["medium"] and self.selectedMazeDifficulty[2]["easier"] or \
                    self.selectedMazeDifficulty[1]["hard"] and self.selectedMazeDifficulty[2]["easier"]:
                if self.harderButton.run(isLeftMouseButtonPressed):
                    self.harderButton.isSelected = True
            elif self.easierButton.run(isLeftMouseButtonPressed):
                self.easierButton.isSelected = True



        # when clicked it will show the stats and maze
        if self.generateMazeButton.run(isLeftMouseButtonPressed) :
            if True not in self.selectedMazeDifficulty[1].values():  # first user option
                if self.easyButton.isSelected:
                    self.selectedMazeDifficulty[1]["easy"] = True
                    self.createMazeFromFile("assets/mazes/A-EasyOption1.txt")
                elif self.mediumButton.isSelected:
                    self.selectedMazeDifficulty[1]["medium"] = True
                    self.createMazeFromFile("assets/mazes/B-MediumOption1.txt")
                elif self.hardButton.isSelected:
                    self.selectedMazeDifficulty[1]["hard"] = True
                    self.createMazeFromFile("assets/mazes/C-HardOption1.txt")

            elif True not in self.selectedMazeDifficulty[2].values():  # second user option
                if self.easierButton.isSelected:
                    self.selectedMazeDifficulty[2]["easier"] = True
                    if self.selectedMazeDifficulty[1]["easy"] or self.selectedMazeDifficulty[1]["medium"]:
                        self.createMazeFromFile("assets/mazes/D-EasyOption2.txt")
                    elif self.selectedMazeDifficulty[1]["hard"]:
                        self.createMazeFromFile("assets/mazes/E-MediumOption2.txt")
                if self.harderButton.isSelected:
                    self.selectedMazeDifficulty[2]["harder"] = True
                    if self.selectedMazeDifficulty[1]["easy"]:
                        self.createMazeFromFile("assets/mazes/E-MediumOption2.txt")
                    if self.selectedMazeDifficulty[1]["medium"] or self.selectedMazeDifficulty[1]["hard"]:
                        self.createMazeFromFile("assets/mazes/F-HardOption2.txt")

            else:  # third option
                if self.easierButton.isSelected:
                    self.selectedMazeDifficulty[3]["easier"] = True
                    if self.selectedMazeDifficulty[1]["medium"] and self.selectedMazeDifficulty[2]["harder"]:
                        self.createMazeFromFile("assets/mazes/E-MediumOption2.txt")
                    if self.selectedMazeDifficulty[1]["hard"] and self.selectedMazeDifficulty[2]["harder"]:
                        self.createMazeFromFile("assets/mazes/E-MediumOption2.txt")
                    if self.selectedMazeDifficulty[1]["medium"] or self.selectedMazeDifficulty[1]["hard"]:
                        self.createMazeFromFile("assets/mazes/E-MediumOption2.txt")

                if self.harderButton.isSelected:
                    self.selectedMazeDifficulty[3]["harder"] = True
                    if self.selectedMazeDifficulty[1]["easy"] and self.selectedMazeDifficulty[2]["easier"]:
                        self.createMazeFromFile("assets/mazes/E-MediumOption2.txt")
                    if self.selectedMazeDifficulty[1]["easy"] and self.selectedMazeDifficulty[2]["harder"]:
                        self.createMazeFromFile("assets/mazes/F-HardOption2.txt")
                    if self.selectedMazeDifficulty[1]["medium"] and self.selectedMazeDifficulty[2]["easier"]:
                        self.createMazeFromFile("assets/mazes/E-MediumOption2.txt")
                    if self.selectedMazeDifficulty[1]["hard"] and self.selectedMazeDifficulty[2]["easier"]:
                        self.createMazeFromFile("assets/mazes/F-HardOption2.txt")

            self.generateMazeButton.isSelected = True
            self.showMazeGeneratorTipsAndTricks = False
            self.panelInfosParagraph.addText(self.mazeNumber, self.fileName,
                                             f"{len(self.maze.board[0])}x{len(self.maze.board)}")
            self.maze.show = True

        # when clicked it will show how the DFS algo works
        elif self.mazeGeneratorSolveLevelButton.run(
                isLeftMouseButtonPressed) and self.maze is not None and self.maze.show and self.mazeGeneratorSolveLevelButton.isSelected == False:
            self.maze.showDFS = True
            self.mazeGeneratorSolveLevelButton.isSelected = True
            self.maze.resetMazeAnimationTimer()

        # when clicked it will move the user to the smart solver page
        elif self.goToSmartSolverButton.run(isLeftMouseButtonPressed) and self.maze is not None and self.maze.animationTime is not None:
            self.easierButton.isSelected = False
            self.harderButton.isSelected = False
            return "smartSolver"

        # when clicked the user return to the menu
        elif self.mazeGeneratorHomeButton.run(isLeftMouseButtonPressed):  # redirect the user to the main menu page
            return "mainMenu"

        # show the tips when needed
        if self.showMazeGeneratorTipsAndTricks:
            self.dottedGridMImage.draw()
            self.mazeGeneratorTipsAndTricksTitleText.draw()
            self.mazeGeneratorTipsAndTricksParagraph.draw()

        # draw the maze when needed
        if self.maze is not None and self.maze.show:
            self.maze.draw()
