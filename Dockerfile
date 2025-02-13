# Stage 1: Pull the model
FROM ollama/ollama:latest as builder

# Install any necessary dependencies
RUN apt-get update && apt-get install -y curl

# Start Ollama server in the background
RUN mkdir -p /root/.ollama
RUN nohup ollama serve > /var/log/ollama.log 2>&1 & \
    # Wait for Ollama server to start
    sleep 10 && \
    # Pull the DeepSeek model
    ollama pull deepseek-r1:8b && \
    # Give some time for the model to be fully downloaded and processed
    sleep 30

# Stage 2: Create the final image
FROM ollama/ollama:latest

# Copy the downloaded model from the builder stage
COPY --from=builder /root/.ollama /root/.ollama

# Expose the default Ollama port
EXPOSE 11434

# Map a local repository to persist and save a local copy of the model
VOLUME ["/local/repository:/root/.ollama"]

# Set the entrypoint to start the Ollama server
ENTRYPOINT ["ollama"]
CMD ["serve"]
