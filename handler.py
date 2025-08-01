import runpod
import torch
from diffusers import DiffusionPipeline
import base64
import io
from PIL import Image
import os

# Global variable to store the model
pipe = None

def load_model():
    """Load the Wan Video model"""
    global pipe
    if pipe is None:
        print("Loading Wan Video model...")
        # Adjust model path/name based on actual Wan Video implementation
        pipe = DiffusionPipeline.from_pretrained(
            "Wan-AI/Wan2.1-VACE-14B",
            torch_dtype=torch.float16,
            device_map="auto"
        )
        print("Model loaded successfully!")
    return pipe

def generate_video(prompt, num_frames=16, width=720, height=480):
    """Generate video from text prompt"""
    model = load_model()
    
    # Generate video
    result = model(
        prompt=prompt,
        num_frames=num_frames,
        width=width,
        height=height,
        num_inference_steps=50
    )
    
    return result

def handler(event):
    """Main handler function for RunPod"""
    try:
        # Get input from event
        input_data = event["input"]
        prompt = input_data.get("prompt", "A beautiful sunset over mountains")
        num_frames = input_data.get("num_frames", 16)
        width = input_data.get("width", 720)
        height = input_data.get("height", 480)
        
        # Generate video
        video_result = generate_video(prompt, num_frames, width, height)
        
        # Process and return result
        return {
            "status": "success",
            "message": "Video generated successfully",
            "prompt": prompt,
            "frames": num_frames
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# Initialize RunPod serverless
runpod.serverless.start({"handler": handler})
