# Image Servers

Run a single object image server with:
```bash
./single_object_server.py -w 800 --bgr "59, 66, 197" --flipy --http_file /Users/pambrose/git/FRC-2018/html/single-image.html --draw_contour
```


Run a multiple object image server with:
```bash
./multi_object_server.py -w 800 --bgr "59, 66, 197" --flipy --http_file /Users/pambrose/git/FRC-2018/html/single-image.html --draw_contour
```


### CLI Options

| Option         | Description                                        | Default        |
|:---------------|----------------------------------------------------|----------------|
| --bgr          | BGR target value                                   |                |
| -u, --usb      | Use USB Raspi camera                               | false          |
| -w, --width    | Image width                                        | 400            |
| -e, --percent  | Middle percent                                     | 15             |
| --min          | Minimum target pixel area                          | 100            |
| --range        | HSV Range                                          | 20             |
| --leds         | Enable Blinkt led feedback                         | false          |
| --display      | Display image                                      | false          |
| -x, --flipx    | Flip image on X axis                               | false          |
| -y, --flipy    | Flip image on Y axis                               | false          |
| -t, --http     | HTTP hostname:port                                 | localhost:8080 |
| --delay        | HTTP delay secs                                    | 0.25           |
| -i, --file     | HTTP template file                                 |                |
| -p, --port     | gRPC server port                                   | 50051          |
| --verbose-http | Enable verbose HTTP log                            | false          |
| -v, --verbose  | Enable debugging output                            | false          |
| -h, --help     | Summary of options                                 |                |

