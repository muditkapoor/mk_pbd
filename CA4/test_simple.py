#Mudit Kapoor 10352635
import unittest

from process_changes import get_commits, read_file

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.log')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))
    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('Jimmy', commits[420]['author'])

if __name__ == '__main__':
    import os
    os.chdir('/Users/muditkapoor/Desktop/Big Data')
    os.getcwd()
    
    unittest.main()
