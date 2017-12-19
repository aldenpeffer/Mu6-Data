# Mu6-Data

`populate.py` takes arguments via the config file `populate.conf`

This script recursively traverses the JSON objects in the files indicated by `populate.conf`, creating entities at the designated endpoint using the designated MIME type.

As there are dependencies in any system, this script can store fields returned by an API for later use.

This feature works as follows:
A single `saveitem` object specifies a `path` to the field relative to the base of the JSON object, and stores it in a dictionary under name `name`. In the following example, `user.id` is a field in JSON-formatted HTTP response from the server. This is value is extracted and then saved as `artistId`.

```
{
    "path": ["user", "id"],
    "name": "artistId"
}
```

This is useful when working on a dependent entity: the key in the JSON-formatted HTTP request is replaced with the dictionary value.

```
"entity": {
    "data": "images/woodstock_album_art.jpg",
    "metadata": {
        "title": "Woodstock",
        "artistId": 0,
        "releaseDate": "1970-01-01"
    }
},
```

If the dictionary contained the value `{"artistId": 37}`, the album dependent on the newly created artist would be:

```
"entity": {
    "data": "images/woodstock_album_art.jpg",
    "metadata": {
        "title": "Woodstock",
        "artistId": 37,
        "releaseDate": "1970-01-01"
    }
},
```