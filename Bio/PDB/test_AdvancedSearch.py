import unittest
import PDB.PDBList
import PDB.AdvancedSearch
import os.path
import shutil

class AdvancedSearchTest(unittest.TestCase):
    def test_search_by_pdb_id(self):
        as_prop = PDB.AdvancedSearch.AdvancedSearch()
        as_prop.pdb_id_s('2fl0')
        as_prop.send()
        self.assertTrue('2FL0' in as_prop.search)

    def test_search_by_mixed_criteria(self):
        """
        On 11.06.2016 given criteria gave result of 4 structures ['1JBN', '1PAR', '2DNJ', '2K2N'] so test expects them
        as result.
        """
        as_prop = PDB.AdvancedSearch.AdvancedSearch()
        as_prop.structure_title(PDB.AdvancedSearch.StructComparator.Starts_with, 'DNA')
        as_prop.number_of_chains_ba('5', '6')
        as_prop.send()

        print(as_prop.search)
        self.assertEqual(4, len(as_prop.search))

    def test_download_by_criteria(self):
        """
        On 11.06.2016 given criteria gave result of 4 structures ['1JBN', '1PAR', '2DNJ', '2K2N'] so test expects them
        as result.
        """
        as_prop = PDB.AdvancedSearch.AdvancedSearch()
        as_prop.structure_title(PDB.AdvancedSearch.StructComparator.Starts_with, 'DNA')
        as_prop.number_of_chains_ba('5', '6')
        as_prop.send()

        print(as_prop.search)
        as_prop.download("pdb", False, None)

        dir_path = os.getcwd() + os.path.sep + 'jb'
        path = dir_path + os.path.sep + 'pdb1jb7.ent'
        exists_1jb7 = os.path.isfile(path)
        self.assertEqual(exists_1jb7, True)
        shutil.rmtree(dir_path)

        dir_path = os.getcwd() + os.path.sep + 'pa'
        path = dir_path + os.path.sep + 'pdb1par.ent'
        exists_1par = os.path.isfile(path)
        self.assertEqual(exists_1par, True)
        shutil.rmtree(dir_path)

        dir_path = os.getcwd() + os.path.sep + 'dn'
        path = dir_path + os.path.sep + 'pdb2dnj.ent'
        exists_2dnj = os.path.isfile(path)
        self.assertEqual(exists_2dnj, True)
        shutil.rmtree(dir_path)

        dir_path = os.getcwd() + os.path.sep + 'k1'
        path = dir_path + os.path.sep + 'pdb2k1n.ent'
        exists_2k1n = os.path.isfile(path)
        self.assertEqual(exists_2k1n, True)
        shutil.rmtree(dir_path)

if __name__ == '__main__':
    unittest.main()
