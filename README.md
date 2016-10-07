# Bio.PDBList-extension

### Updated and extended module PDBList from the biopython package.

Changes applied:
1. Possibility to download structures in PDBx/mmCif, PDB, PDBML/XML and
mmtf formats (both from function and from command line)
2. Possibility to download large structures in PDB-like formatted bundles
3. New function: download specified set of structures
4. Code is now python 3.x compatible
5. Unit tests added
6. Corrected the issue with downloading the same file into different directories
7. Some minor updates

NOTE. The default download format changed from (deprecated) PDB to
(recommended by RCSB) PDBx/mmCIf.

Usage:

    from Bio.PDB.PDBList import PDBList
    pdblist = PDBList()
    pdblist.retrieve_pdb_file("127d")  # downloads structure 127D in PDBx/mmCif format
    pdblist.retrieve_pdb_file("127d", file_format = "pdb")  # downloads structure 127D in PDB format
    pdblist.retrieve_pdb_file("127d", file_format = "xml")  # downloads structure 127D in PDBML/XML format
    pdblist.retrieve_pdb_file("127d", file_format = "mmtf")  # downloads structure 127D in mmtf format
    pdblist.retrieve_pdb_file("3k1q", file_format = "bundle")  # downloads large structure 3K1Q in pdb-like bundle
    pdblist.retrieve_pdb_file("347d", obsolete=True)  # downloads obsolete structure 347D in PDBx/mmCif format
    pdblist.download_pdb_files("1esy", "127D")  # downloads structures 127D and 1ESY in PDBx/mmCif format
    pdblist.download_entire_pdb()  # downloads entire PDB database in PDBx/mmCif format
    pdblist.update_pdb()  # performs weekle update of the database
    
    

The module can be also call from the command line:

    PDBList.py update <pdb_path> [options]   - write weekly PDB updates to
                                               local pdb tree.
    PDBList.py all    <pdb_path> [options]   - write all PDB entries to
                                               local pdb tree.
    PDBList.py obsol  <pdb_path> [options]   - write all obsolete PDB
                                               entries to local pdb tree.
    PDBList.py <PDB-ID> <pdb_path> [options] - retrieve single structure
    PDBList.py (<PDB-ID1>,<PDB-ID2>,...) <pdb_path> [options] - retrieve a set
                                               of structures

    Options:
       -d       A single directory will be used as <pdb_path>, not a tree.
       -o       Overwrite existing structure files.
       -pdb     Downloads structures in PDB format
       -xml     Downloads structures in PDBML (XML) format
       -mmtf    Downloads structures in mmtf format

    Maximum one format can be specified simultaneously (if more selected, only
    the last will be considered). By default (no format specified) structures are
    downloaded as PDBx/mmCif files.
