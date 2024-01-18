# FLINT-precondition-labelling
Automatically extract preconditions for FLINT frames from Dutch sources of norms.



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
flask --app act_frame_extractor_server run

```



## Report:
- [view only](https://www.overleaf.com/read/vwhrjrsnsxrj#6d5464)

## TODO's:
- [Project Board](https://github.com/users/JuliusHuizing/projects/1/views/1)
- 
