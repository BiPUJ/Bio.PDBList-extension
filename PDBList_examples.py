from Bio.PDB.PDBList import PDBList

pdblist = PDBList()
pdblist.retrieve_pdb_file("127d")  # downloads structure 127D in PDBx/mmCif format
pdblist.retrieve_pdb_file("127d", file_format="pdb")  # downloads structure 127D in PDB format
pdblist.retrieve_pdb_file("127d", file_format="xml")  # downloads structure 127D in PDBML/XML format
pdblist.retrieve_pdb_file("127d", file_format="mmtf")  # downloads structure 127D in mmtf format
pdblist.retrieve_pdb_file("3k1q", file_format="bundle")  # downloads large structure 3K1Q in pdb-like bundle
pdblist.retrieve_pdb_file("347d", obsolete=True)  # downloads obsolete structure 347D in PDBx/mmCif format
pdblist.download_pdb_files("1esy", "127D")  # downloads structures 127D and 1ESY in PDBx/mmCif format
pdblist.download_entire_pdb()  # downloads entire PDB database in PDBx/mmCif format
pdblist.update_pdb()  # performs weekle update of the database