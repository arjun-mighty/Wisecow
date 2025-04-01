FROM ubuntu:22.04

# Install required packages
RUN apt-get update && \
    apt-get install -y fortune-mod cowsay netcat-openbsd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the PATH to include cowsay
ENV PATH=$PATH:/usr/games

# Copy the application
WORKDIR /app
COPY wisecow.sh .

# Make the script executable
RUN chmod +x wisecow.sh

# Expose the port
EXPOSE 4499

# Run the application
CMD ["./wisecow.sh"]