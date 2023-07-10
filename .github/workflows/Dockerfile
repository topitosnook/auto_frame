# Use an appropriate base image
FROM mcr.microsoft.com/m1/apple-silicon:11.0.0

# Download and install Chrome
RUN curl -o /tmp/chrome.dmg -L https://dl.google.com/chrome/mac/stable/GGRO/googlechrome.dmg && \
    hdiutil attach /tmp/chrome.dmg && \
    cp -r "/Volumes/Google Chrome/Google Chrome.app" /Applications/ && \
    hdiutil detach "/Volumes/Google Chrome" && \
    rm /tmp/chrome.dmg

# Download and install Chromedriver
RUN curl -o /usr/local/bin/chromedriver -L https://chromedriver.storage.googleapis.com/<version>/chromedriver_mac64.zip && \
    unzip /usr/local/bin/chromedriver -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver
    echo 'export PATH="/webdrivers/chromedriver:$PATH"' >> $GITHUB_ENV

    
