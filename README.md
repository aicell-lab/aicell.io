# AICell Lab Website


Visit here: https://aicell.io

## Development

Run the following command:
```
hugo serve
```


### Build Error
If you came across the following error:
```
Error: command error: failed to create config from modules config: unknown output format "redirects" for kind "home"
```

Do the following:
```bash
rm -rf $TMPDIR/hugo_cache/
hugo mod get
hugo server
```

See here: https://wowchemy.com/docs/hugo-tutorials/troubleshooting/#error-failed-to-resolve-output-format
### Update publications

Run the following command:
```
curl "https://scholar.googleusercontent.com/citations?view_op=export_citations&user=bJBzM18AAAAJ&citsig=AMD79ooAAAAAY7soJbArD3N0mT3AJqRk4wy8NX2ommv7&hl=en" -o assets/publications.bib
```

Optionally, go to [google scholar page](https://scholar.google.co.uk/citations?user=bJBzM18AAAAJ&hl=en) and select all the publications, click `EXPORT` and choose `BibTex`, save the content as 'publication.bib' file and save into `assets/publication.bib`.

To convert the format, run the following command:
```
pip3 install -U academic
academic import --bibtex assets/publications.bib
```
This will regenerate `publication` folder.

See [here](https://wowchemy.com/docs/content/publications/) for more details.

## Acknowledgements

This website is built with [wowchemy](https://wowchemy.com/)
