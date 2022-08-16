# rss-digest-flask

Take a source RSS feed and return a digest RSS feed.

## URL Arguments

| Argument          | Mandatory? | Default Value | Behavior                        |
| ----------------- | ---------- | ------------- | ------------------------------- |
| ?url              | Y          | None          | Source RSS URL                  |
| ?feed-description | N          | None          | Feed description                |
| ?feed-icon        | N          | Project logo  | Feed icon URL                   |
| ?feed-icon-alt    | N          | None          | Feed icon alt-text              |
| ?feed-title       | N          | Untitled Feed | Feed title                      |
| ?item-title       | N          | Untitled Item | Item title                      |
| ?latest           | N          | None          | Max oldest article (in seconds) |

`?itemTitle` input replaces `_date` with the current date.
