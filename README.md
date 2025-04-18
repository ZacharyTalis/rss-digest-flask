# rss-digest-flask

Convert a source RSS feed into a periodic digest RSS feed.

[Live demo available here (no uptime guarantee).](https://plus.cerisetalis.com/digest/)

## Local testing

For local testing, change directory to `rss-digest` and run `flask run --debug`.

## Deployment

1. Install the `ca-certificates` package.
2. In the main directory, run `python3 -m venv venv && . venv/bin/activate`.
3. Run `pip install .` to install the dependencies defined by `setup.py`.
4. Add and enable a new systemd service based off of `ref/rss-digest-flask.service`.
5. Configure an nginx site using the route information provided by `ref/nginx.txt`.
6. Reboot and enjoy :3

## URL Arguments

| Argument          | Mandatory? | Default Value | Behavior                                                                            |
| ----------------- | ---------- | ------------- | ----------------------------------------------------------------------------------- |
| ?url              | Y          | None          | Direct link to the source feed.                                                     |
| ?feed-description | N          | None          | Description of your digest feed.                                                    |
| ?feed-icon        | N          | Project logo  | Direct link to your digest feed's icon.                                             |
| ?feed-icon-alt    | N          | None          | Description of your digest feed's icon.                                             |
| ?feed-title       | N          | Untitled Feed | Title of your digest feed.                                                          |
| ?item-title       | N          | Untitled Item | Title of articles in your digest feed. Feed replaces `_date` with the current date. |
| ?latest           | N          | None          | Max oldest article to include (in seconds). 1 day = 86400 seconds.                  |

All input needs `&` escaped to `%26`, and ` ` (a space) escaped to `%20`.
