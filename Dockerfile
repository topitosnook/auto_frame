  # Use an official Python runtime as a parent image
   FROM python:3.8

   # Set the working directory in the container to /app
   WORKDIR /automation_framework

  # Add the current directory contents into the container at /app
   ADD . /automation_framework

   # Install any needed packages specified in requirements.txt
   RUN pip install --no-cache-dir -r requirements.txt

   # Install wget
   RUN apt-get update && apt-get install -y wget

   # Install Chrome
   RUN wget https://dl.google.com/chrome/mac/universal/stable/CHFA/googlechrome.dmg
   RUN dpkg -i googlechrome.dmg; apt-get -fy install

   # Install ChromeDriver
   RUN wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_mac_arm64.zip
   RUN unzip chromedriver_mac_arm64.zip
   RUN mv chromedriver /usr/bin/chromedriver
   RUN chown root:root /usr/bin/chromedriver
   RUN chmod +x /usr/bin/chromedriver

   # Run app.py when the container launches
   CMD ["python", "runner.py"]