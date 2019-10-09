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
