Run "DeepSeek" Locally
######################

.. contents:: Install Neccessary Tools
   :local:
   :class: no-bullets

Build the Image with the name "ollama-deepseek"
===============================================

To build the Docker image, navigate to the directory containing the Dockerfile and run the following command:

.. code-block:: bash

	docker build -t deepseek-v2:tagName /home/smadi/projects/deep1

	docker build -t ollama-deepseek:latest .

------------------------------------------------------------------

Run the ollama-deepseek container
=================================

.. code-block:: bash

	docker run -d -p 11434:11434  5000:5000 deepseekv2

	docker run -d -p 11434:11434 --name deepseekv2 deepseek-v2:latest

------------------------------------------------------------------

Run Streamlit app
=================

Navigate to .venv bin folder and run (source activate)
cd ~/python-projects/qa_app/.venvQAapp/bin

.. code-block:: bash

	source activate

Install Requirments

.. code-block:: bash

	pip install -r requirements.txt 

run the App

.. code-block:: bash

	streamlit run ./streamlit/app.py
