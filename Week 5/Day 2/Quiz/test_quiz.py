import unittest
from unittest.mock import patch
from quiz import get_username, update_score, shuffle_questions, ask_question, save_score, initialize_high_scores_file

class TestQuiz(unittest.TestCase):

    @patch('builtins.input', return_value='test_user')
    def test_get_username(self, mock_input):
        self.assertEqual(get_username(), 'test_user')

    def test_update_score_correct(self):
        self.assertEqual(update_score(True, 0), 5)

    def test_update_score_incorrect(self):
        self.assertEqual(update_score(False, 0), -2)

    def test_shuffle_questions(self):
        questions = {"Q1": {}, "Q2": {}, "Q3": {}}
        shuffled = shuffle_questions(questions)
        self.assertEqual(set(shuffled), set(questions.keys()))
        self.assertNotEqual(shuffled, list(questions.keys()))

    @patch('builtins.input', side_effect=['1'])
    def test_ask_question(self, mock_input):
        question = "Test question?"
        choices = ["Choice1", "Choice2", "Choice3", "Choice4"]
        self.assertEqual(ask_question(question, choices), 1)

    def test_save_score(self):
        test_file = 'test_high_scores.txt'
        save_score('test_user', 10, test_file)
        with open(test_file, 'r') as f:
            lines = f.readlines()
        self.assertIn('Username: test_user, Score: 10\n', lines)
        
    def test_initialize_high_scores_file(self):
        test_file = 'test_high_scores.txt'
        initialize_high_scores_file()
        with open(test_file, 'r') as f:
            header = f.readline().strip()
        self.assertEqual(header, 'Username: Score')

if __name__ == '__main__':
    unittest.main()
