cd ../

echo "Creating a VirtualEnv"
echo ""
virtualenv -p python3 venv

echo "Activating VirtualEnv"
echo ""
source ./venv/bin/activate
echo ""

#Run all pip install
echo "Installing requirements for Python"
pip install -r requirements.txt
echo ""

#################
# Database
#################

psql -U postgres << END_OF_SCRIPT

DROP   DATABASE django;
CREATE DATABASE django;

CREATE USER django WITH PASSWORD 'a6a06b71e36fa6a80b8a9eb665e208ee';

ALTER ROLE django SET client_encoding TO 'utf8';
ALTER ROLE django SET default_transaction_isolation TO 'read committed';
ALTER ROLE django SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE django TO django;
END_OF_SCRIPT
echo ""

echo "Finished Database section"

echo ""
echo "Flushing Database"
echo ""
python manage.py flush #Clear the database on reinstall

echo ""
echo "Migrating to Database"
echo ""
python manage.py makemigrations
python manage.py migrate


echo ""
echo "Creating Super User... "
echo ""
python manage.py createsuperuser


#echo ""
#echo "Writing Data to Database"
#echo ""
#run the init store script
#cd scripts/
#python initstore.py
#cd ../

echo ""
echo "Starting Django Server"
python manage.py runserver

