git clone: 
git clone https://github.com/Damir-p/cvat.ai.git

create virtualenv: python3 -m venv venv

activate virtualenv:
Linux: source venv/bin/activate
Windows: venv\Scripts\activate

requirements: 
pip install -r requirements.txt

download json file:
python download_json.py

run project:
python main.py