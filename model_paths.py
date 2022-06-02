import joblib
import pickle
import warnings


        



if 'google.colab' in str(get_ipython()):
    model_dir = "MgAlloyPublic/models"
else:
    model_dir = "models"
    
    
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=UserWarning)
    UTS = joblib.load(f"{model_dir}/UTS")
    YS= joblib.load(f"{model_dir}/YS")
    ductility = joblib.load(f"{model_dir}/ductility")   
    
    
models = {"elongation": ductility, 
          "tensile": UTS,
          "yield": YS
          }

