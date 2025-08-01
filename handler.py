#!/usr/bin/env python3
import runpod
import json

def handler(job):
    """
    This is the handler function that will be called by the serverless worker.
    """
    try:
        # Get the input from the job
        job_input = job.get("input", {})
        
        # Extract parameters
        prompt = job_input.get("prompt", "A beautiful landscape")
        
        # For now, return a simple response
        # Later you can add Wan Video model here
        result = {
            "status": "success",
            "message": "Handler is working correctly!",
            "received_prompt": prompt,
            "note": "Ready for Wan Video integration"
        }
        
        return result
        
    except Exception as e:
        return {
            "status": "error", 
            "error": str(e)
        }

# Start the serverless worker
runpod.serverless.start({"handler": handler})
