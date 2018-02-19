# chaves

A web YouTube player that shows predefined videos in random order, but respecting sequenced videos.
This means that if some videos don't make sense for viewers if not played in a specific ordering, it will be respected.

[https://chaves.rgm.io/](Live demo)


## Configuration

Create a settings file similar to this one:

```python
TITLE = 'Chaves player'

VIDEOS = [
    [
        '2rdfuZPqSk4',  # Chaves - Nem todos os bons negócios são negócios da China - parte 1 (1977)
        'K6UF19LSDg8',  # Chaves - Refrescos numa fria - parte 2 (1977)
        '0yfr3FJ-EKc',  # Chaves - A insônia do Seu Madruga - parte 3 (1977)
    ], [
        'AOln4MoD-RA',  # Chaves - Bilhetes trocados (1977)
    ],
]
```

Make sure to always populate the `VIDEOS` list with lists of YouTube IDs, even if a video is not part of a sequence.

In this example, the first 3 videos will always be played in sequence. The player will always start with the first video of the first sequence or with the other video, that is not part of the sequence.

Save this file as `chaves.cfg`.


## How to run

### Development

```
$ pip install -r requirements.txt
$ CHAVES_CONFIG=chaves.cfg FLASK_APP=chaves.py flask run
```

### Production

```
$ pip install -r requirements.txt
$ pip install gunicorn
$ CHAVES_CONFIG=chaves.cfg gunicorn --bind 127.0.0.1:$PORT --workers $NUM_WORKERS chaves:app
```

You should define `$PORT` and `$NUM_WORKERS` according to your system, and configure nginx to proxy requests to `$PORT`.
