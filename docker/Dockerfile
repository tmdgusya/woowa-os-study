# syntax=docker/dockerfile:1
# Use a valid Ubuntu base image (e.g., Ubuntu 20.04)
FROM ubuntu:22.04

RUN mkdir /woowa
# Update package lists and upgrade installed packages, then install wget
RUN apt update && apt upgrade -y && apt install -y wget

# Downlaod python3
RUN apt install -y python3

# Donwload strace for monitoring system call
RUN apt install -y strace

# Download sysstat to check the amount of time used for system calls
RUN apt install -y sysstat

# This one install a C compilter as well as other tools that we may need to build something
RUN apt install -y build-essential

# Download and install Go
ENV GO_VERSION=1.21.4
RUN wget https://golang.org/dl/go${GO_VERSION}.linux-amd64.tar.gz -O go.tar.gz \
    && tar -C /usr/local -xzf go.tar.gz \
    && rm go.tar.gz

# Set Go environment variables
ENV PATH=$PATH:/usr/local/go/bin

# Expose port (documentation purpose only)
EXPOSE 22

# Default command to run when the container starts (replace with your application command)
CMD ["/bin/bash"]

