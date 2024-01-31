# Use Ubuntu 20.04 as base image
FROM ubuntu:20.04

# Install sysbench packages
RUN apt-get update && \
    apt-get install -y sysbench && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# CMD instruction
CMD ["/bin/bash"]

