pip install -r requirements.txt
python3.9 manage.py migrate
python3.9 manage.py loaddata core/fixtures/cargo.json 
python3.9 manage.py loaddata core/fixtures/funcionalidades.json
python3.9 manage.py loaddata core/fixtures/funcionario.json 
python3.9 manage.py loaddata core/fixtures/servico.json 
python3.9 manage.py loaddata core/fixtures/user.json
python3.9 manage.py loaddata core/fixtures/feedbacks.json

python3.9 manage.py collectstatic