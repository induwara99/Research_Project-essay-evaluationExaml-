conda create --name examl python==3.8

conda activate examl

pip install --ignore-installed opencv-python nltk pywsd scikit-learn flask Flask-Cors PyPDF2 textwrap3 transformers pke-tool flashtext sentence_transformers spacy pydot bertopic pandas rake-nltk protobuf==3.20.0

conda install -c numba numba==0.56.2

python -m spacy download en_core_web_sm