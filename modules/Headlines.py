import feedparser

feed = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml?edition=us')
feed.entries[0]