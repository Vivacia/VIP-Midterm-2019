from ase.build import molecule, fcc111, add_adsorbate
from ase.visualize import view
import ase.dft.kpoints
from sparc.sparc_core import SPARC
import CO_PE
import Pt_PE
import combined_PE

molecules = molecule('CO')
molecules.center()
slab = fcc111('Pt', size = (2, 2, 4), vacuum = 10)
c = FixAtoms(indices = [molecule.index for molecule in slab if molecule.index > 7])
slab.set_constraint(c)

E_gas = CO_PE.calc_CO(molecules)
E_slab = Pt_PE.calc_Pt(slab)
E_slab_ads = combined_PE.calc_combined(slab, molecules)
E_ads = E_slab_ads - E_slab - E_gas
print(E_ads)