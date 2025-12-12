# Kideny-Disease-Classification-Deep-Learning-Project

# Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py

How to run?

STEPS:

Clone the repository
    https://github.com/kirankarakalli/Kideny-Disease-Classification-Deep-Learning-Project.git

STEP 01- Create a conda environment after opening the repository
    conda create -n cnncls python=3.8 -y
    conda activate cnncls

STEP 02- install the requirements
    pip install -r requirements.txt

# Finally run the following command
python main.py


Create ECR repo to store/save docker image
    - Save the URI: 032068930445.dkr.ecr.us-east-1.amazonaws.com/kidney



sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker