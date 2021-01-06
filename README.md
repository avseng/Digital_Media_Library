# Digital_Media_Library
Google Chromecast, RFID and raspberry pi based digital media library

1. Installing rasbian os
2. update and upgrade the os.
3. Install Node-Red

	bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
	sudo systemctl enable nodered.service

4. Install apache web server.

	sudo apt install apache2 -y

5. provide permission to /var/www/html directory.

	sudo chmod -R 777 /var/www/html/*

6. create folder for audio playlist and videos.
7. craete mapping.csv under /home/pi
8. copy the exec.sh to /home/pi directory.
9. open node red in the web browser.
10. install below nodes

	a. node-red-contrib-castv2
	b. node-red-contrib-rc522
	c. node-red-dashboard
	d. Simplecast
	
11. import the JSON and deploy
