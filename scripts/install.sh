cd ../

echo "Creating a VirtualEnv"
echo ""
virtualenv venv

echo "Activating VirtualEnv"
echo ""
source ./venv/bin/activate
echo ""

#Run all pip install
echo "Installing requirements for Python"
pip install -r requirements.txt
echo ""

#Create the database
#TODO

echo ""
echo "Flushing Database"
echo ""
python manage.py flush #Clear the database on reinstall


echo ""
echo "Writing Data to Database"
echo ""
#run the init store script
cd scripts/
python initstore.py
cd ../

echo ""
echo "Starting Django Server"
python manage.py runserver

