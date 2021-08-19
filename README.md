# practice-problems
djlksajda

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation
Fork this [remote repository](linkhere) and clone a remote copy on your local computer.

Navigate to the local copy from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd practice-problems
```

Use Anaconda to create and activate a new virtual environment called "practive-probs-env":

```sh
conda create -n practice-probs-env python=3.8 # (first time only)
conda activate practice-probs-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

## Setup

In your local repository's root directory, create a new file called ".env". Go [Genius' API client management page](http://genius.com/api-clients) and create an account if you don't already have one. Update the contents of the ".env" file to record your client id and client secret.

    client_id="YOUR_APP_CLIENT_ID"
    client_secret="YOUR_APP_CLIENT_SECRET"

## Usage

Run the ____ script:

```py
python app.py
```

If running the program through Heroku, follow [this repo's](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/clis/heroku.md) README file.

## Testing

Running all tests:

```sh
pytest
```