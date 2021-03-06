# twipy

I decided to write a small Python script to be called each time I initiate R in the Terminal.
The script grabs the most recent status from [@RLangTip](https://twitter.com/RLangTip) using the Python Twitter API wrapper [tweepy](https://github.com/tweepy/tweepy) and displays it after (or instead of) the regular R startup message.

![twipy screenshot](./R_screenshot.png)

The script requires that you edit your `.Rprofile` by adding the following:

```
.First <- function() {
	system('clear')  # comment out to keep the regular R startup message
	startup <- system("python /path/to/twipy.py", intern=TRUE)
	message(startup)
	rm(startup)
}
```

If you already have a `.First` function just add the contents to the end.

In addition to editing your `.Rprofile`, you must edit `twipy.py` using your own consumer key/secret for the [Twitter API](https://dev.twitter.com).
