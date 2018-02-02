# Color Selector

Run a color selector with:
```bash
./color_selector.py -w 800  
```

### CLI Options

| Option         | Description                                        | Default        |
|:---------------|----------------------------------------------------|----------------|
| -u, --usb      | Use USB Raspi camera                               | false          |
| -w, --width    | Image width                                        | 400            |
| --display      | Display image                                      | false          |
| -x, --flipx    | Flip image on X axis                               | false          |
| -y, --flipy    | Flip image on Y axis                               | false          |
| --http         | HTTP hostname:port                                 | localhost:8080 |
| --delay        | HTTP delay secs                                    | 0.25           |
| -i, --file     | HTTP template file                                 |                |
| --verbose-http | Enable verbose HTTP log                            | false          |
| -v, --verbose  | Enable debugging output                            | false          |
| -h, --help     | Summary of options                                 |                |

### Display Keystrokes

| Keystroke  | Action                                             |
|:----------:|----------------------------------------------------|
| c          | Print current BGR value to console                 |
| k          | Move ROI up                                        |
| j          | Move ROI down                                      |
| h          | Move ROI left                                      |
| k          | Move ROI right                                     |
| -          | Decrease ROI size                                  |
| +          | Increase ROI size                                  |
| w          | Decrease image size                                |
| W          | Increase image size                                |
| r          | Reset ROI size and image size                      |
| q          | Quit                                               |
