# rss-digest-flask

Convert a source RSS feed into a periodic digest RSS feed.

[Live demo available here (no uptime guarantee).](https://plus.zacharytalis.com/digest/)

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
