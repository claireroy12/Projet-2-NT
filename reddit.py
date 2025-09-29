import praw
import datetime
from datetime import datetime

reddit = praw.Reddit(
client_id="rsaZdvLrhQqsjDPpPKX6AA",
client_secret="CeBJaz94VwiVdA26cSK3k38StvJx5w",
user_agent="StardewScraping (by u/Either-Location-4670)"
)



posts = []
for post in reddit.subreddit("QuebecLibre").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "subreddit": str(post.subreddit),
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })
    print(post.title + " - " + str(post.score))




# Export CSV
#pd.DataFrame(posts).to_csv("../data/posts.csv", index=False, encoding="utf-8")