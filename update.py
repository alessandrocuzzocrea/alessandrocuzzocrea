import feedparser

# URL of the RSS feed
rss_url = "https://alessandrocuzzocrea.com/feed.xml"

# Parse the RSS feed
feed = feedparser.parse(rss_url)

# print(feed)

# Print basic feed information
# print(f"Feed Title: {feed.feed.title}")
# print(f"Feed Link: {feed.feed.link}")
# print(f"Feed Description: {feed.feed.description}")

# Loop through and print each entry in the feed
for entry in feed.entries:
    print("\n---")
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}")
    # print(f"Published: {entry.published}")
    # print(f"Summary: {entry.summary}")
