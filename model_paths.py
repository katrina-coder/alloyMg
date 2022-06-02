import joblib
import pickle
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=UserWarning)
    UTS_model = joblib.load(f"{model_dir}/UTS")
    YS_model= joblib.load(f"{model_dir}/YS")
    duct_model = joblib.load(f"{model_dir}/ductility")
        



if 'google.colab' in str(get_ipython()):
    model_dir = "MgAlloyPublic/models"
else:
    model_dir = "models"

    
    
    
models = {"elongation": duct_model, 
          "tensile": UTS_model,
          "yield": YS_model
          }

