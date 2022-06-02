import joblib
import pickle
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=UserWarning)
    UTS = joblib.load(f"{model_dir}/UTS")
    YS = joblib.load(f"{model_dir}/YS")
    duct = joblib.load(f"{model_dir}/ductility")
        



if 'google.colab' in str(get_ipython()):
    model_dir = "MgAlloyPublic/models"
else:
    model_dir = "models"

    
    
    
models = {"elongation": duct), 
          "tensile": UTS),
          "yield": YS)
          }

