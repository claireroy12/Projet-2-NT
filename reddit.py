import praw
import datetime
from datetime import datetime
import pandas as pd

reddit = praw.Reddit(
client_id="rsaZdvLrhQqsjDPpPKX6AA",
client_secret="CeBJaz94VwiVdA26cSK3k38StvJx5w",
user_agent="StardewScraping (by u/Either-Location-4670)"
)



posts = []

print(" Récupération des posts de quebec libre...")
for post in reddit.subreddit("QuebecLibre").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })

print(" Récupération des posts de canada...")
for post in reddit.subreddit("canada").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })

print(" Récupération des posts de ask a canadian...")
for post in reddit.subreddit("AskACanadian").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })

print(" Récupération des posts de personnal finance canada...")
for post in reddit.subreddit("PersonalFinanceCanada").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })

print(" Récupération des posts de quebec city...")
for post in reddit.subreddit("Quebeccity").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })

print(" Récupération des posts de brossard...")
for post in reddit.subreddit("brossard").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })

print(" Récupération des posts de canada politics...")
for post in reddit.subreddit("CanadaPolitics").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })




print(" Récupération des posts de quebec...")
for post in reddit.subreddit("Quebec").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })

print(" Récupération des posts de quebec finance...")
for post in reddit.subreddit("QuebecFinance").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })

print(" Récupération des posts de montreal...")
for post in reddit.subreddit("Montreal").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })


print(" Récupération des posts de sherbrooke...")
for post in reddit.subreddit("Sherbrooke").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })

print(" Récupération des posts de trois-rivières...")
for post in reddit.subreddit("troisrivieres").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })

print(" Récupération des posts de rimouski...")
for post in reddit.subreddit("Rimouski").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })

print(" Récupération des posts de Laval...")
for post in reddit.subreddit("Laval").top(limit=2500): # récupérer 3000 posts pour être sûr
    posts.append({
    "id": post.id,
    "titre": post.title,
    "auteur": str(post.author) if post.author else None,
    "flair": post.link_flair_text,
    "score": int(post.score),
    "upvote_ratio": float(post.upvote_ratio),
    "nb_commentaires": int(post.num_comments),
    "texte": post.selftext,
    "date_creation": datetime.fromtimestamp(post.created_utc).isoformat(),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })




# Export CSV
pd.DataFrame(posts).to_csv("posts.csv", index=False, encoding="utf-8-sig", sep=";")
print("Exporté posts.csv! :)")