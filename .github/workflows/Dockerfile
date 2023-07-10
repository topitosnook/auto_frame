# Use an appropriate base image
FROM python:3.9

# Install Chrome dependencies
RUN apt-get update && apt-get install -y wget gnupg ca-certificates

# Add Chrome package repository
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

# Install Chrome
RUN apt-get update && apt-get install -y google-chrome-stable

# Install Chromedriver
RUN apt-get update && apt-get install -y wget unzip
RUN wget -q https://chromedriver.storage.googleapis.com/<version>/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/local/bin/
RUN rm chromedriver_linux64.zip
