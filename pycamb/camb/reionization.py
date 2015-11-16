'''

In order to get access to functions in the shared library
you will need to use the following pattern by using the construction

camblib.__modulename_MOD_functionname(args)

set the data type for the functions
camblib.__modulename_MOD_functionname.restype = ctype

The arguments are passed by reference

'''

from ctypes import *
from baseconfig import camblib, CAMB_Structure

# ---Variables in reionization.f90
# To set the value please just put 
# variablename.value = newvalue

# logical
include_helium_fullreion = c_bool.in_dll(camblib, "__reionization_MOD_include_helium_fullreion")
# include_helium_fullreion.value = True

# logical
Reionization_AccuracyBoost = c_bool.in_dll(camblib, "__reionization_MOD_reionization_accuracyboost")
# Reionization_AccuracyBoost.value = 1.

Rionization_zexp = c_bool.in_dll(camblib, "__reionization_MOD_rionization_zexp")


# Rionization_zexp.value = 1.5

# ---Derived Types in reionization.f90

class ReionizationParams(CAMB_Structure):
    _fields_ = [
        ("Reionization", c_int),  # logical
        ("use_optical_depth", c_int),  # logical
        ("redshift", c_double),
        ("delta_redshift", c_double),
        ("fraction", c_double),
        ("optical_depth", c_double),
        ("helium_redshift", c_double),  # helium_redshift  = 3.5_dl
        ("helium_delta_redshift", c_double),  # helium_delta_redshift  = 0.5
        ("helium_redshiftstart", c_double)  # helium_redshiftstart  = 5._dl
    ]

    def set_tau(self, tau, delta_redshift = None):
        self.use_optical_depth = True
        self.optical_depth = tau
        if delta_redshift is not None:
            self.delta_redshift = delta_redshift


class ReionizationHistory(CAMB_Structure):
    _fields_ = [
        ("tau_start", c_double),
        ("tau_complete", c_double),
        ("akthom", c_double),
        ("fHe", c_double),
        ("WindowVarMid", c_double),
        ("WindowVarDelta", c_double)
    ]
