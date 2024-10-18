# Use an official OpenJDK runtime as a parent image
FROM openjdk:11-jre-slim

# Set environment variables for FOP version
ENV FOP_VERSION=2.6

# Install only the necessary packages and download Apache FOP
RUN apt-get update && \
    apt-get install -y wget unzip python3 python3-pip && \
    wget http://archive.apache.org/dist/xmlgraphics/fop/binaries/fop-${FOP_VERSION}-bin.zip && \
    unzip fop-${FOP_VERSION}-bin.zip && \
    mv fop-${FOP_VERSION} /opt/fop && \
    chmod +x /opt/fop/fop/fop && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* fop-${FOP_VERSION}-bin.zip

# Set the working directory
WORKDIR /opt/fop

# Install Python and Flask
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install Flask

# Copy the Python Flask script directly into the container
COPY app.py /opt/fop/app.py
COPY templates /opt/fop/templates

# Command to run the Flask app directly
CMD ["python3", "/opt/fop/app.py"]
