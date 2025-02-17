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

------------------------------------------------------------------

Run Streamlit app as Microservices
==================================

To create a `docker-compose.yml` file that runs two containers (one for the Ollama server and one for the Streamlit app) and allows them to communicate, you can use the following configuration:


.. code-block:: yaml

services:
  ollama:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "11434:11434"
    volumes:
      - /local/repository:/root/.ollama
      - /data:/data
    networks:
      - app-network

  streamlit:
    build:
      context: ./app
      dockerfile: Dockerfile
    ports:
      - "8501:8501"
    depends_on:
      - ollama
    networks:
      - app-network

networks:
  app-network:
    driver: bridge


In this `docker-compose.yml` file:

- The `ollama` service builds the Docker image using the Dockerfile in the root directory and exposes port `11434`.
- The `streamlit` service builds the Docker image using the Dockerfile in the app directory and exposes port `8501`.
- The `depends_on` directive ensures that the `streamlit` service starts after the `ollama` service.
- Both services are connected to a custom network named `app-network` to enable communication between them.

To run the services, navigate to the project directory and use the following command:

.. code-block:: bash

	docker-compose up --build

This command will build the images and start the containers. You can then access the Streamlit app in your browser at `http://localhost:8501`.

# Create volume for model persistence                                                                            

.. code-block:: bash

	docker volume create ollama-data                                                                                        

# Build custom image

.. code-block:: bash

	docker build -t deepseek-ollama -f ollama/Dockerfile .


# Run container with volume

.. code-block:: bash

	docker run -d \
  	--name ollama \
  	-v ollama-data:/root/.ollama \
  	-p 11434:11434 \
  	deepseek-ollama

# Download and persist model

.. code-block:: bash

	docker exec ollama ollama pull deepseek-r1:14b

.. code-block:: bash

	docker exec -it ollama ollama list 
