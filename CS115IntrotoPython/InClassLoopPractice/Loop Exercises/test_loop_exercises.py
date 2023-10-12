import unittest
import loop_exercises

class Test(unittest.TestCase):

    def test01(self):
        self.assertEqual(loop_exercises.questifyAlt([]), [])
        self.assertEqual(loop_exercises.questifyAlt(['yeah']), ['yeah?'])
        self.assertEqual(loop_exercises.questifyAlt(['yeah', 'really', 'no way']), ['yeah?', 'really?', 'no way?'])

    def test02(self):
        self.assertEqual(loop_exercises.catenateLoop([]), '')
        self.assertEqual(loop_exercises.catenateLoop(['this']), 'this')
        self.assertEqual(loop_exercises.catenateLoop(['this', 'function', 'actually', 'works']), 'thisfunctionactuallyworks')

    def test03(self):
        self.assertEqual(loop_exercises.letterScoreLoop('a', loop_exercises.scrabbleScores), 1)
        self.assertEqual(loop_exercises.letterScoreLoop('f', loop_exercises.scrabbleScores), 4)
        self.assertEqual(loop_exercises.letterScoreLoop('q', loop_exercises.scrabbleScores), 10)
        self.assertEqual(loop_exercises.letterScoreLoop('z', loop_exercises.scrabbleScores), 10)

    def test04(self):
        self.assertEqual(loop_exercises.wordScoreLoop('', loop_exercises.scrabbleScores), 0)
        self.assertEqual(loop_exercises.wordScoreLoop('test', loop_exercises.scrabbleScores), 4)
        self.assertEqual(loop_exercises.wordScoreLoop('zebra', loop_exercises.scrabbleScores), 16)
        self.assertEqual(loop_exercises.wordScoreLoop('manufacturing', loop_exercises.scrabbleScores), 21)

    def test05(self):
        self.assertEqual(loop_exercises.wordsWithScoreLambda([], loop_exercises.scrabbleScores), [])
        self.assertEqual(loop_exercises.wordsWithScoreLambda(['a'], loop_exercises.scrabbleScores), [['a', 1]])
        self.assertEqual(loop_exercises.wordsWithScoreLambda(['python', 'is', 'awesome'], loop_exercises.scrabbleScores), [['python', 14], ['is', 2], ['awesome', 12]])
        self.assertEqual(loop_exercises.wordsWithScoreLambda(loop_exercises.aDictionary, loop_exercises.scrabbleScores), [['a', 1], ['am', 4], ['at', 2], ['apple', 9], ['bat', 5], ['bar', 5], ['babble', 12], ['can', 5], ['foo', 6], ['spam', 8], ['spammy', 15], ['zzyzva', 39]])

    def test06(self):
        self.assertEqual(loop_exercises.wordsWithScoreLoop([], loop_exercises.scrabbleScores), [])
        self.assertEqual(loop_exercises.wordsWithScoreLoop(['a'], loop_exercises.scrabbleScores), [['a', 1]])
        self.assertEqual(loop_exercises.wordsWithScoreLoop(['python', 'is', 'awesome'], loop_exercises.scrabbleScores), [['python', 14], ['is', 2], ['awesome', 12]])
        self.assertEqual(loop_exercises.wordsWithScoreLoop(loop_exercises.aDictionary, loop_exercises.scrabbleScores), [['a', 1], ['am', 4], ['at', 2], ['apple', 9], ['bat', 5], ['bar', 5], ['babble', 12], ['can', 5], ['foo', 6], ['spam', 8], ['spammy', 15], ['zzyzva', 39]])

if __name__ == "__main__":
    unittest.main()
