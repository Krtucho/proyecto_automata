# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', 'examples/system/', 'system.kfb'):
           [1672942282.3184533, 'system.fbc'],
         ('', 'examples/system/', 'bc_system.krb'):
           [1672942282.4625692, 'bc_system_bc.py'],
        },
        compiler_version)

