# PDF-Query

A chatbot to answer questions from the context of a PDF.
Includes a command line loop to enter queries and display answers.

## Installing Dependencies

Create a virtual environment using:

```sh
python -m venv .venv
```

Activate the virtual environment:

```sh
source .venv/bin/activate
```

Install the dependencies from `requirements.txt`:

```sh
pip install -qr requirements.txt
```

To deactivate the virtual environment, use:

```sh
deactivate
```

## Initializing Configurations

Create `configs.py` in the project directory and copy contents from [this](configs_template.py) file.
Replace the values with your own before running the program.

## Entering the Query loop

After activating the virtual environment and initializing the configurations, run the following to enter the query loop (make sure you are in the project directory):

```sh
python .
```

You can exit the program at any time by hitting `Ctrl-D`, or change the current PDF by typing "CHANGE PDF" (these instructions are also shown at the beginning of the program).
