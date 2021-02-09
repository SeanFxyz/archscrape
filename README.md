# archscrape

Given any number of URLs as commandline arguments (they should all be archive.org pages starting with `https://archive.org/details/...`) this script will return a list of file download links, filtered by the file types specified in the `ftypes` tuple.

This is not a very sophisticated tool, just something I threw together quickly to get a job done.

This script only outputs a list of links to files. How to download those files is up to you. I recommend something like this if you prefer curl:

```
archscrape.py https://archive.org/details/commentariescjul00cmob | xargs -n1 curl -LO
```

Or, if you prefer GNU wget:

```
archscrape.py https://archive.org/details/commentariescjul00cmob | xargs wget -N
```
