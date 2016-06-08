import unittest
import PDB.PDBList
import os.path
import shutil

class PDBListTest(unittest.TestCase):
    def test_download_mmcif(self):
        download = PDB.PDBList()
        download.download_mmcif_file('2fl0', False, None)
        dir_path = os.getcwd() + os.path.sep + 'fl'
        path = dir_path + os.path.sep + '2fl0.cif'
        exists = os.path.isfile(path)

        self.assertEqual(exists, True)

        shutil.rmtree(dir_path)

    def test_download_big_pdb_file_compressed(self):
        download = PDB.PDBList()
        download.download_big_pdb_file('3j92', False, None, False)
        dir_path = os.getcwd() + os.path.sep + 'j9'
        path = dir_path + os.path.sep + '3j92-pdb-bundle.tar'
        exists = os.path.isfile(path)

        self.assertEqual(exists, True)

        shutil.rmtree(dir_path)

    def test_download_big_pdb_file_decompressed(self):
        download = PDB.PDBList()
        download.download_big_pdb_file('3j92', False, None, True)
        dir_path = os.getcwd() + os.path.sep + 'j9'
        path = dir_path + os.path.sep + '3j92-pdb-bundle.tar.gz'
        exists = os.path.isfile(path)

        self.assertEqual(exists, True)

        shutil.rmtree(dir_path)

if __name__ == '__main__':
    unittest.main()
