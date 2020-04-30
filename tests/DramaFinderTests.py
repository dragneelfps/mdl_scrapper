import unittest

from mdl_scrapper import DramaFinder


class DramaFinderTests(unittest.TestCase):

    @unittest.skip("for manual testing")
    def test_all_results(self):
        finder = DramaFinder("love")
        res = finder.find_next()
        i = 0
        while not res.is_empty() and i < 4:
            print(res)
            res = finder.find_next()
            i += 1
