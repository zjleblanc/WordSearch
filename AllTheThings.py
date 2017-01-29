class Commander:
    directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    answers = []
    scanners = []

    def __init__(self, puzzleToSearch, wordsToSearchFor):
        self.puzzleToSearch = puzzleToSearch
        self.wordsToSearchFor = wordsToSearchFor

class Scanner:

    def __init__(self, direction, puzzle, wordsToFind):
        self.direction = direction
        self.puzzle = puzzle
        self.wordsToFind = wordsToFind

    def scan_for_words(self):
        print('scanning for words')

    def enough_room_for_word(self):
        print('determining if there is enough room for the word to search')