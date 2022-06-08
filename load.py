import os 

def load_trained_model() :
  weight_file = f"{os.getcwd()}\\new_model_phase2.hdf5"
  assert os.path.isfile(weight_file), "ERROR: fail to locate the pretrained weight file"

  


  # TODO create_model, then add weight to it and then return modelcreate



