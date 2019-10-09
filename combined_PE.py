from ase.build import molecule, fcc111, add_adsorbate
from ase.visualize import view
import ase.dft.kpoints
from sparc.sparc_core import SPARC
from ase.constraints import FixAtoms

class combined_PE:
	def calc_combined(self, slab, molecules):
		# slab = fcc111('Pt', size = (2, 2, 4), vacuum = 10)
		calc2 = SPARC(
             KPOINT_GRID=[4,4,1],
             h = 0.2,
             EXCHANGE_CORRELATION = 'GGA',
             TOL_SCF=1e-5,
             RELAX_FLAG=1,
             PRINT_FORCES=1,
             PRINT_RELAXOUT=1)
		slab.set_calculator(calc2)
		add_adsorbate(slab, molecules, 2.3,'hcp')
		E_slab_ads = slab.get_potential_energy()
		return E_slab_ads