## FIFO Pipe Reader

### Usage

Run *fifo_pip_reader.py* with:
```bash
python fifo_pipe_reader.py --camera_name "Front Camera" --template ~git/FRC-2018/html/single-image.html --fifo /Users/pambrose/git/FRC-2018/python/jpg_pipe -x 800 -y 600
```

### CLI Options

| Option         | Description                                        | Default        |
|:---------------|----------------------------------------------------|----------------|
| -f, --fifo     | FIFO pipe filename (required)                      |                |
| -t, --template | HTTP template file (required)                      |                |
| --http         | HTTP port                                          | 8080           |
| --delay        | HTTP delay secs                                    | 0.25           |
| -x, --image_x  | Image x pixels                                     | 640            |
| -y, --image_y  | Image y pixels                                     | 480            |
| -c, --camera_name | Camera name displayed on web page               | ""             |
| --http_verbose | Enable verbose HTTP log                            | false          |
| -v, --verbose  | Enable debugging output                            | false          |
| -h, --help     | Summary of options                                 |                |
