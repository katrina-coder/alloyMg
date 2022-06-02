import joblib
import pickle




if 'google.colab' in str(get_ipython()):
    model_dir = "alloyMg/models"
else:
    model_dir = "models"

models = {"elongation": joblib.load(f"{model_dir}/ductility"),
          "tensile": joblib.load(f"{model_dir}/UTS"),
          "yield": joblib.load(f"{model_dir}/YS")
          }

