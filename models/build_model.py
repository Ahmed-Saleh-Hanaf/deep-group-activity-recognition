from models.baseline_1 import ImageClassification

def get_model(config):
    config = config["MODEL"]["NAME"]
    if(config.NAME == 'imageclassification'):
        model = ImageClassification(config.NUM_CLASSES, config.PRETRAINED)
        return model
    else:
        raise ValueError("Unknown model")
    
    