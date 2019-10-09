from ase.build import molecule, fcc111, add_adsorbate
from ase.visualize import view
import ase.dft.kpoints
from sparc.sparc_core import SPARC

class CO_PE:
	def calc_CO(self, molecules):
		# molecules = molecule('CO')
		# molecules.center()
		calc = SPARC(
             KPOINT_GRID=[1,1,1],
             h = 0.2,
             EXCHANGE_CORRELATION = 'GGA',
             TOL_SCF=1e-5,
             RELAX_FLAG=1,
             PRINT_FORCES=1,
             PRINT_RELAXOUT=1)
		molecules.set_calculator(calc)
		E_gas = molecules.get_potential_energy()
		return E_gas

# kpts = ase.dft.kpoints.monkhorst_pack([4, 4, 1]) + [0.2, 0.15, 0.12]
molecules = molecule('CO')
molecules.center()
slab = fcc111('Pt', size = (2, 2, 4), vacuum = 10)
c = FixAtoms(indices = [molecule.index for molecule in slab if molecule.index > 7])
slab.set_constraint(c)

# set up the calculator
calc = SPARC(
             KPOINT_GRID=[1,1,1],
             h = 0.2,
             EXCHANGE_CORRELATION = 'GGA',
             TOL_SCF=1e-5,
             RELAX_FLAG=1,
             PRINT_FORCES=1,
             PRINT_RELAXOUT=1)

calc2 = SPARC(
             KPOINT_GRID=[4,4,1],
             h = 0.2,
             EXCHANGE_CORRELATION = 'GGA',
             TOL_SCF=1e-5,
             RELAX_FLAG=1,
             PRINT_FORCES=1,
             PRINT_RELAXOUT=1)

molecules.set_calculator(calc)
slab.set_calculator(calc2)

E_gas = molecules.get_potential_energy()
E_slab = slab.get_potential_energy()

add_adsorbate(slab, molecules, 2.3,'hcp')
E_slab_ads = slab.get_potential_energy()

E_ads = E_slab_ads - E_slab - E_gas
print(E_ads)