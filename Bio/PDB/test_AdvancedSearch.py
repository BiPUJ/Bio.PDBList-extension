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

    def test_search_by_mixed_criterias(self):
        as_prop = PDB.AdvancedSearch.AdvancedSearch()
        as_prop.structure_title(PDB.AdvancedSearch.StructComparator.Starts_with, 'DNA')
        as_prop.number_of_chains_ba('5', '6')
        as_prop.send()

        self.assertEqual(4, len(as_prop.search))

    def test_download_by_criterias(self):
        as_prop = PDB.AdvancedSearch.AdvancedSearch()
        as_prop.pdb_id_s('2fl0')
        as_prop.send()
        as_prop.download("pdb", False, None)

        dir_path = os.getcwd() + os.path.sep + 'fl'
        path = dir_path + os.path.sep + 'pdb2fl0.ent'
        exists = os.path.isfile(path)

        self.assertEqual(exists, True)

        shutil.rmtree(dir_path)

if __name__ == '__main__':
    unittest.main()
