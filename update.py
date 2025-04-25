import feedparser

rss_url = "https://alessandrocuzzocrea.com/feed.xml"

feed = feedparser.parse(rss_url)

file_content = "### Latest articles\n\n"

latest_articles = feed.entries[:5]

for entry in latest_articles:
    title = entry.title
    link = entry.link
    file_content += f"- #### [{title}]({link})\n"

with open("README.md", "w", encoding="utf-8") as file:
    file.write(file_content)

print("Latest articles have been saved to 'README.md!'")
