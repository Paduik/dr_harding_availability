The Three Hour Dr. Harding Availability Web App

Overview: Flask based web app displaying Dr. Harding's availability for annual physicals. Users can select a date and confirm their appointment. (Very basic, built in three hours.)

Instructions: 
1. Clone repo:<br>
   git clone https://github.com/Paduik/dr_harding_availability.git<br>
   cd dr_harding_availability <br>
2. Build and run Docker container:<br> 
   docker build -t my-flask-app .<br>
   docker run -p 5000:5000 my-flask-app<br>
3. Go to http://127.0.0.1:5000/ to play around with the demo. (http://127.0.0.1:5000/)

Project and File Structure:<br> 
-'app': Flask app<br>
-'templates': HTML templates<br>
-'static': Static files - css, js<br>
-'Dockerfile': Congiguration to build the Docker image<br>
-'requirements.txt': Python dependencies<br> 

Author: Luke Trenshaw