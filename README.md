The Three Hour Dr. Harding Availability Web App

Overview: Flask based web app displaying Dr. Harding's availability for annual physicals. Users can select a date and confirm their appointment. (Very basic, built in three hours.)

Instructions: 
1. Clone repo: 
   git clone https://github.com/Paduik/dr_harding_availability.git
   cd dr_harding_availability 
2. Build and run Docker container: 
   docker build -t my-flask-app .
   docker run -p 5000:5000 my-flask-app
3. Go to http://127.0.0.1:5000/ to play around with the demo. (http://127.0.0.1:5000/)

Project and File Structure: 
-'app': Flask app
-'templates': HTML templates
-'static': Static files - css, js
-'Dockerfile': Congiguration to build the Docker image
-'requirements.txt': Python dependencies 

Author: Luke Trenshaw