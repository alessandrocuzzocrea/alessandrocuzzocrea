import feedparser

# URL of the RSS feed
rss_url = "https://alessandrocuzzocrea.com/feed.xml"

# Parse the RSS feed
feed = feedparser.parse(rss_url)

# Prepare the file content
file_content = "### Latest articles\n\n"

# Get the latest 5 articles
latest_articles = feed.entries[:5]

for entry in latest_articles:
    title = entry.title
    link = entry.link
    file_content += f"- #### [{title}]({link})\n"

# Write the content to a file
with open("README.md", "w", encoding="utf-8") as file:
    file.write(file_content)

print("Latest articles have been saved to 'README.md'")
