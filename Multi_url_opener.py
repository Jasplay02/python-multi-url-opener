import webbrowser

urls = []

print("Enter URLs one by one. Press ENTER with no text to finish.")

while True:
    url = input("URL: ").strip()
    if url == "":
        break

    # Add https:// automatically if missing
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    urls.append(url)

# Open each URL in Chrome
for url in urls:
    webbrowser.get("windows-default").open(url)

print("Done! All websites opened.")
