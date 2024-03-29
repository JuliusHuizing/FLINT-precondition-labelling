# FLINT-Frame-Service
Automatically extract FLINT ACT frames from Dutch sources of norms.

## Usage

### Configuring your environment
- add a .env file to the root directory with the following keys:
```
OPENAI_SECRET_KEY=<YOUR_SECRET_KEY_HERE>
```

### Getting started

- install and activate python 3.9.0*
- install poetry if new to poetry: https://python-poetry.org/docs/#installation
- (`poetry env use /full/path/to/python`)
- `poetry config virtualenvs.in-project true`
- `poetry install`
- Go to project settings of your editor and set the created virtual environment as project interpreter
- **Important:** this tool uses python 3.8 or higher because the transformers and the matplotlib package only support python 3.8 or higher. Running
  FlintFiller-srl with a lower python version results in an error.


### Using the Act Frame Extractor Microservice
To start running the microservice for extracting act frames from user inputs, run:

```bash
flask --app flint_frame_service run
```
And request a response like:

```bash
curl -X POST http://127.0.0.1:5000/extract-act-frame \
-H "Content-Type: application/json" \
-d '{"article_string": "personal data shall be processed lawfully."}'
```

**Note** that by default, the server mimics processing time by sleeping for 5 - 10 seconds before returning a response. If you want disable this behavior, change the key of your request type to "debug":

```bash
curl -X POST http://127.0.0.1:5000/extract-act-frame \
-H "Content-Type: application/json" \
-d '{"debug": "personal data shall be processed lawfully."}'
```


## Report:
- [view only](https://www.overleaf.com/read/vwhrjrsnsxrj#6d5464)

