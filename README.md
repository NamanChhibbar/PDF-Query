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

## Entering the Query loop

After installing the dependencies and activating the virtual environment, run the following (make sure you are in the project directory):

```sh
python .
```

You can exit the program at any time by hitting `Ctrl-D`, or change the current PDF by typing "CHANGE PDF" (these instructions are also shown at the beginning of the program).
