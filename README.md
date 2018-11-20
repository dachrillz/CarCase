# CAR CASE!

# Requirements
    1. To run this locally you need bash, Python3, pip3, virtualenv and postgresql installed. 

# Install
    1. In theory one only needs to run ./install.sh inside the /scripts/ folder

# Deployed version
    1. With a high likelihood there will be problems running this software locally, since that is how software generally
    works today. Therefore this code is also deployed on the following ip address: [165.227.169.249:8000](http://165.227.169.249:8000/)
    2. This way one only needs a web browser to access the website.

# Some notes on the deployed version
    1. At endpoint /docs/ there is documentation on all the calls that can be made. 
    2. Don't use the login/logout buttons that the swagger documentation framework shows. They don't lead anywhere
    3. There is an admin user with login: chrille, pass: hej123 that can be used to create other users.
    4. There is a normal user with login: kalle, pass hej123 that can be used to see what a user of the website will see currently.
