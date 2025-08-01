import runpod
import torch
import os
import base64
import io
from PIL import Image

# Global variables
model = None
device = None

def load_model():
    """Load Wan Video model"""
    global model, device
    
    if model is None:
        print("Loading Wan Video model...")
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device: {device}")
        
        try:
            # For now, we'll use a placeholder
            # Later replace with actual Wan Video model loading
            from diffusers import StableDiffusionPipeline
            
            model = StableDiffusionPipeline.from_pretrained(
                "runwayml/stable-diffusion-v1-5",
                torch_dtype=torch.float16,
                safety_checker=None,
                requires_safety_checker=False
            ).to(device)
            
            print("Model loaded successfully!")
            
        except Exception as e:
            print(f"Error loading model: {e}")
            return None
    
    return model

def generate_video(prompt, num_frames=16, width=512, height=512):
    """Generate video from prompt"""
    model = load_model()
    
    if model is None:
        return {"error": "Model failed to load"}
    
    try:
        # For now, generate a single image (placeholder for video)
        # Later this will be replaced with actual video generation
        image = model(
            prompt=prompt,
            width=width,
            height=height,
            num_inference_steps=20,
            guidance_scale=7.5
        ).images[0]
        
        # Convert to base64
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        img_base64 = base64.b64encode(buffer.getvalue()).decode()
        
        return {
            "status": "success",
            "image": img_base64,
            "prompt": prompt,
            "width": width,
            "height": height
        }
        
    except Exception as e:
        return {"error": str(e)}

def handler(job):
    """Main handler function"""
    try:
        # Get input
        job_input = job.get("input", {})
        
        prompt = job_input.get("prompt", "A beautiful landscape")
        num_frames = job_input.get("num_frames", 16)
        width = job_input.get("width", 512)
        height = job_input.get("height", 512)
        
        # Generate
        result = generate_video(prompt, num_frames, width, height)
        
        return result
        
    except Exception as e:
        return {
            "error": str(e),
            "status": "failed"
        }

# Start serverless
if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
