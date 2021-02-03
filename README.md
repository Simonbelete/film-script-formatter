# Film Script Formatter

Rule based film script formatter, since it is rule based and the library is not fully tested it's accuracy is probably around `90-95%`

dataset [https://imsdb.com/]()


## Usage

### Requirements

* `>= python3.7`

```python

from film_script_formatter.film_script_formatter import FilmScriptFormatter

filmScriptFormatter = FilmScriptFormatter(filename = 'examples/coco.txt')

filmScriptFormatter.actors(output = 'examples/coco_actors.json')

```

### Running Examples

Create virtual environment

```bash
$ python3 -m venv venv
```

Activate the virtual environment

```bash
$ source venv/bin/activate
```

Install requirements (Optional)

```bash
$ pip install -r requirements-dev.txt
```

Runn individual examples 

```bash
(venv) $ python -m examples.coco_example
```


### Testing

```bash
$ pytest
```

