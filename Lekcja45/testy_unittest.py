import io
import unittest
from unittest.mock import patch

import main

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main.add(1, 2), 3)
        self.assertNotEqual(main.add(1, 2), 5)
    def test_main2(self):
        self.assertFalse(main.if_palindrom("kajakllll"))

    @patch('sys.stdout', new_callable=io.StringIO) # import io <- dopisać na początku
    # from unittest.mock import patch <- dopisać na początku
    def test_divide_exception(self, mock_stdout):
        main.divide(1, 0)
        self.assertEqual(mock_stdout.getvalue(), "Dzielenie przez 0\n")

    def test_sorted_list(self):
        self.assertEqual(main.sort_strings_by_length(['kot', 'pies', 'dziobak']),
                         ['kot', 'pies', 'dziobak'])
        self.assertEqual(main.sort_strings_by_length(['dziobak', 'pies', 'kot']),
                         ['kot', 'pies', 'dziobak'])


if __name__ == '__main__':
    unittest.main()