import connect4, numpy, unittest
from unittest.mock import patch
from io            import StringIO
 
def metadata_of(array): 
    return [ type(array), array.ndim, array.shape, array.size, array.dtype ]

class TestConnect(unittest.TestCase):

    def test_setup_game_board(self):
        testArray      = connect4.create_board()
        expectedArray  = numpy.zeros( (6,7) )

        actualArrayMetadata   = metadata_of(testArray)
        expectedArrayMetadata = metadata_of(expectedArray)

        self.assertEqual(actualArrayMetadata, expectedArrayMetadata)

    def test_prompt_player_for_move(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:            
            currentPlayer  = 1
            expectedOutput = f'Player {currentPlayer}, make your selection (1-7):'
            
            connect4.prompt_player(currentPlayer)
            actualOutput = fakeOutput.getvalue().strip()

            self.assertEqual(actualOutput, expectedOutput)

    def test_initialization_of_gameVariables(self):
        gameVariables = connect4.gameVariables()
        expectedArray = numpy.zeros( (6,7) )

        actualArrayMetadata   = metadata_of(gameVariables.board)
        expectedArrayMetadata = metadata_of(expectedArray)

        self.assertEqual(actualArrayMetadata        , expectedArrayMetadata)    # Footnote 1
        self.assertEqual(gameVariables.gameOver     , False)
        self.assertEqual(gameVariables.turnNumber   , 1)
        self.assertEqual(gameVariables.currentPlayer, 1)

        # FOOTNOTES:
        #   1.  This duplicates test_setup_game_board.
        #       Is it possible to reuse any code?

    def test_game_loop_exits_program_if_game_over(self):
        gameVariables = connect4.gameVariables()
        gameVariables.gameOver = True

        with self.assertRaises(SystemExit):
            connect4.game_loop_step(gameVariables)

    def test_game_loop_prompts_player_for_move(self):
        gameVariables  = connect4.gameVariables()
        expectedOutput = 'Player 1, make your selection (1-7):'

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            connect4.game_loop_step(gameVariables)
            actualOutput = fakeOutput.getvalue().strip()

            self.assertEqual(actualOutput, expectedOutput)
        
        # ENDNOTES:
        #   1.  Like test_initialization_of_gameVariables duplicates test_setup_game_board,
        #       this duplicates test_prompt_player_for_move. 
        #       Is there a place for code reuse here?

    def test_game_loop_iterates_gameVariables(self):
        gameVariables = connect4.gameVariables()
        
        with patch('sys.stdout', new=StringIO()) as fakeOutput: # Footnote 1
            # == FIRST ITERATION == #
            expectedTurnNumber    = 2
            expectedCurrentPlayer = 2
            
            connect4.game_loop_step(gameVariables)              # Footnote 2
            actualTurnNumber    = gameVariables.turnNumber
            actualCurrentPlayer = gameVariables.currentPlayer

            self.assertEqual(actualTurnNumber   , expectedTurnNumber)
            self.assertEqual(actualCurrentPlayer, expectedCurrentPlayer)

            # == SECOND ITERATION == #
            expectedTurnNumber    = 3
            expectedCurrentPlayer = 1
            
            connect4.game_loop_step(gameVariables)
            actualTurnNumber    = gameVariables.turnNumber
            actualCurrentPlayer = gameVariables.currentPlayer

            self.assertEqual(actualTurnNumber   , expectedTurnNumber)
            self.assertEqual(actualCurrentPlayer, expectedCurrentPlayer)
        
        # FOOTNOTES:
        #   1.  Without this, running the game loop will print to the console.
        #   2.  There is duplication here; an opportunity for refactoring?

if __name__ == '__main__':
    unittest.main()