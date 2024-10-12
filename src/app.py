from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
from PIL import Image
import io
import base64
from model import load_model, predict
from utils import postprocess_mask

app = FastAPI()

# Load the pre-trained model
model = load_model()

@app.post("/segment/")
async def segment_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    
    # Perform segmentation
    mask = predict(model, image)
    
    # Postprocess the mask
    result_mask = postprocess_mask(mask)
    
    # Convert the mask to a base64 encoded string
    mask_image = Image.fromarray((result_mask * 255).astype(np.uint8))
    buffered = io.BytesIO()
    mask_image.save(buffered, format="PNG")
    mask_base64 = base64.b64encode(buffered.getvalue()).decode()
    
    return JSONResponse(content={"segmentation_mask": mask_base64})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)