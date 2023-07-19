#Build the project

echo "Building the project"
python3 -m pip install -r requirements.txt

echo "Make migration...."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
echo "END migration"

echo "Collect statistics..."
python3 manage.py collectstatic --noinput --clear
echo "END collect statics"
