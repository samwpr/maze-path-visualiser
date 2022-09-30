
# ----- Colors Settings ----- #
LIGHT_GRAY = "#FAFAFA"  # Background
DARK_BLUE = "#004AAD"  # Title & Starting Square
BLACK = "#0B0B0B"  # all dark color text
BLUE = "#0357C8"  # buttons
GRAY = "#797979"  # Home Button in Maze Generator & Smart Solver
LIGHT_BLUE = "#5CE1E6"  # Explored Path
RED = "#FF1616"  # Smart Solver Title
LIGHT_RED = "#FF5757"  # Smart Solver Button
YELLOW = "#FFDE59"  # Solution Path
WHITE = (255, 255, 255)

MAZE_COLOR = {0: WHITE, 1: GRAY, 2: DARK_BLUE, 3:LIGHT_RED}  # color of the maze tiles, 0: path, 1: wall, 2: start, 3: goal


# ----- Screen Settings ----- #
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 680
BACKGROUND_COLOR = LIGHT_GRAY
WINDOW_NAME = "maze & smart solver"


# ----- Fonts Settings ----- #
DEFAULT_FONT = None
DEFAULT_FONT_SIZE = 24
DEFAULT_TEXT_COLOR = BLACK

# ----- Report settings ----- #
SCROLL_SPEED = 18  # negative number to reverse the scroll direction


# ----- Buttons Settings ----- #
DEFAULT_BUTTON_SIZE = (206, 45)  # default width and height of the buttons
DEFAULT_BUTTON_COLOR = BLUE
DEFAULT_BUTTON_SELECTED_COLOR = LIGHT_BLUE
DEFAULT_ROUNDED_CORNER = 12  # default rounded corners value (0 to deactivate)
DEFAULT_OUTLINE_RADIUS = 1  # will make an outline of X px when the mouse is over the button
DEFAULT_OUTLINE_COLOR = GRAY
DEFAULT_BUTTON_TEXT_COLOR = LIGHT_GRAY
DEFAULT_BUTTON_FONT = DEFAULT_FONT
DEFAULT_BUTTON_FONT_SIZE = 28
DEFAULT_BUTTON_ZOOM_FACTOR = 2  # will make the button text bigger when the mouse is over the button (0 or False to deactivate)


# ----- Panel Settings ----- #
PANEL_WIDTH = 280  # width of the panel which contains the stats and buttons


# ----- Maze Settings ----- #
MAZE_ANIMATION_SPEED = 0.009  # every X s a new tile of the maze path / explored path will be reveled
MAX_MAZE_SIZE = 25

