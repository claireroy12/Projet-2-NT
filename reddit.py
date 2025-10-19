import praw
import datetime
from datetime import datetime
import pandas as pd

# initialisation de l'API
reddit = praw.Reddit(
client_id="rsaZdvLrhQqsjDPpPKX6AA",
client_secret="CeBJaz94VwiVdA26cSK3k38StvJx5w",
user_agent="StardewScraping (by u/Either-Location-4670)"
)
print("[+] initialisation de l'API complete")


posts = []

# collecte des posts de tout les different sub
print("[*] Récupération des posts de canada...")
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
    "date_creation": datetime.fromtimestamp(post.created_utc),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })
print("[+] Récupération des posts de canada complete")


print("[*] Récupération des posts de ask a canadian...")
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
    "date_creation": datetime.fromtimestamp(post.created_utc),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })
print("[+] Récupération des posts de ask a canadian complete")


print("[*] Récupération des posts de personnal finance canada...")
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
    "date_creation": datetime.fromtimestamp(post.created_utc),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })
print("[+] Récupération des posts de personnal finance canada complete")


print("[*] Récupération des posts de quebec city...")
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
    "date_creation": datetime.fromtimestamp(post.created_utc),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })
print("[+] Récupération des posts de quebec city complete")


print("[*] Récupération des posts de brossard...")
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
    "date_creation": datetime.fromtimestamp(post.created_utc),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })
print("[+] Récupération des posts de brossard complete")


print("[*] Récupération des posts de canada politics...")
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
    "date_creation": datetime.fromtimestamp(post.created_utc),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })
print("[+] Récupération des posts de canada politics complete")


print("[*] Récupération des posts de quebec...")
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
    "date_creation": datetime.fromtimestamp(post.created_utc),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })
print("[+] Récupération des posts de quebec complete")


print("[*] Récupération des posts de quebec finance...")
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
    "date_creation": datetime.fromtimestamp(post.created_utc),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })
print("[+] Récupération des posts de quebec finance complete")


print("[*] Récupération des posts de montreal...")
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
    "date_creation": datetime.fromtimestamp(post.created_utc),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })
print("[+] Récupération des posts de montreal complete")


print("[*] Récupération des posts de sherbrooke...")
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
    "date_creation": datetime.fromtimestamp(post.created_utc),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })
print("[+] Récupération des posts de sherbrooke complete")


print("[*] Récupération des posts de trois-rivières...")
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
    "date_creation": datetime.fromtimestamp(post.created_utc),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })
print("[+] Récupération des posts de trois-rivières complete")


print("[*] Récupération des posts de rimouski...")
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
    "date_creation": datetime.fromtimestamp(post.created_utc),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })
print("[+] Récupération des posts de rimouski complete")


print("[*] Récupération des posts de Laval...")
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
    "date_creation": datetime.fromtimestamp(post.created_utc),
    "url": post.url,
    "image_url": post.url if post.url.endswith((".jpg", ".png")) else None
    })
print("[+] Récupération des posts de Laval complete")


# Export CSV
print("[*] Exportation des postes dans le fichie posts.csv...")
pd.DataFrame(posts).to_csv("posts.csv", index=False, encoding="utf-8-sig", sep=";")
print("[+] Exportation des postes dans le fichie posts.csv complete")

