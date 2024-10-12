import numpy as np

def postprocess_mask(mask, threshold=0):
    return (mask > threshold).astype(np.uint8)