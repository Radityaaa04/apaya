FROM pytorch/pytorch:2.1.0-cuda11.8-devel

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    wget \
    curl \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install \
    transformers \
    diffusers \
    accelerate \
    torch-audio \
    opencv-python \
    pillow \
    numpy \
    gradio \
    huggingface-hub

# Clone Wan Video repository (adjust if needed)
RUN git clone https://github.com/Wan-AI/Wan2.1-VACE-14B.git

# Set environment variables
ENV PYTHONPATH=/workspace
ENV HF_HOME=/workspace/cache

# Expose port for web interface
EXPOSE 7860

# Default command
CMD ["python", "-c", "print('Wan Video environment ready!')"]
