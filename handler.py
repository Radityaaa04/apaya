import runpod

def handler(job):
    """
    Handler function for RunPod Serverless
    
    Args:
        job (dict): The job object containing input data
        
    Returns:
        dict: The result to be returned to the client
    """
    # Get the job input
    job_input = job["input"]
    
    # Extract parameters from input
    prompt = job_input.get("prompt", "default prompt")
    
    # Your processing logic goes here
    # For now, just return a test response
    result = {
        "message": "Handler is working!",
        "prompt_received": prompt,
        "status": "success"
    }
    
    return result

# Start the serverless worker
runpod.serverless.start({"handler": handler})
