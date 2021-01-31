WORK_DIR="face_detection"
service nginx restart
cd ${WORK_DIR}
python manage.py migrate
python manage.py init_admin_user
python manage.py runserver
