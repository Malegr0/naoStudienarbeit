# naoStudienarbeit

## Table of contents
* [About The Project](#about-the-project)
  * [Build With](#build-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#Installation)
* [Usage](#usage)

## About The Project
This project is about understanding german spoken language using the robot NAO and natural language processing. The result is going to be presented at the Berlin School
of Economics and Law. This repository represents the server-side of this project. The client-side can be found HERE. 

### Build With
This project was built using following frameworks:
  - [SpaCy](https://spacy.io/)
  - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
  - [MariaDB Connector](https://mariadb.com/de/resources/blog/how-to-connect-python-programs-to-mariadb/)

For this project we are using the german trained pipeline for spacy. Other pipelines can be found [here](https://spacy.io/usage).
Note that you can't use our database if you are using another pipeline.

## Getting Started
This project is written in python.

### Prerequisites
Pip is needed for the following installation.

### Installation
1. Clone the repo
```
git clone https://github.com/Malegr0/naoStudienarbeit.git
```
2. Install packages
```
pip install -U spacy
python -m spacy download de_core_news_sm
pip install flask
pip3 install mariadb
```

