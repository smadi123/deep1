
1. Build the Image with the name "ollama-deepseek"
##################################################

**	To build the Docker image, navigate to the directory containing the Dockerfile and run the following command:

$	docker build -t deepseek-v2:tagName /home/smadi/projects/deep1

$	docker build -t ollama-deepseek:latest .

------------------------------------------------------------------

2. # run the ollama-deepseek container

	docker run -p -p 11434:11434  5000:5000 deepseekv2
$	docker run -d -p 11434:11434 --name deepseekv2 deepseek-v2:latest

------------------------------------------------------------------

3. # Run Streamlit app

Navigate to .venv bin folder and run (source activate)
cd ~/python-projects/qa_app/.venvQAapp/bin
$	source activate

Install Requirments
$	pip install -r requirements.txt 

run the App
$	streamlit run ./streamlit/app.py