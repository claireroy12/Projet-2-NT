import praw
import pandas as pd
from datetime import datetime

# Variable global
CLIENT_ID = "rsaZdvLrhQqsjDPpPKX6AA"
CLIENT_SECRET = "CeBJaz94VwiVdA26cSK3k38StvJx5w"
USER_AGENT = "StardewScraping (by u/Either-Location-4670)"
SUBREDDIT_NAME = "askreddit"   # peut etre changer pour le sub voulue
OUTPUT_FILE = "posts.csv"
TARGET_COUNT = 2500


# initialisation de l'API
reddit = praw.Reddit(
client_id="rsaZdvLrhQqsjDPpPKX6AA",
client_secret="CeBJaz94VwiVdA26cSK3k38StvJx5w",
user_agent="StardewScraping (by u/Either-Location-4670)"
)

subreddit = reddit.subreddit(SUBREDDIT_NAME)


# collecte des posts
posts = []
def collect(generator, source):
    """Ajoute les posts d'un générateur à la liste"""
    for post in generator:
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
            "image_url": post.url if post.url.endswith((".jpg", ".png", ".gif")) else None,
            "source": source
        })


print("[*]Récupération des posts...")

# Diverses sources pour maximiser la variété
collect(subreddit.hot(limit=1000), "hot")
print("[+] Récupération des posts hot complete")

collect(subreddit.new(limit=1000), "new")
print("[+] Récupération des posts new complete")

for tf in ["day", "week", "month", "year", "all"]:
    collect(subreddit.top(time_filter=tf, limit=1000), f"top-{tf}")
print("[+] Récupération des posts top complete")


# SUPPRESSION DES DOUBLONS
print("[*]suppression des doublons...")
df = pd.DataFrame(posts)
df = df.drop_duplicates(subset="id", keep="first")
print("[+] suppression des doublons complete")


print(f"[+] Nombre de posts uniques collectés : {len(df)}")

# Vérifie si on atteint le quota
if len(df) < TARGET_COUNT:
    print(f"[x]Seulement {len(df)} posts uniques trouvés. ")
    print("[x]Choisis un subreddit plus actif ou augmente les filtres.")
    raise ValueError(
        f"[x]Seulement {len(df)} posts uniques trouvés. "
        f"[x]Choisis un subreddit plus actif ou augmente les filtres."
    )


# EXPORT CSV
df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
print(f"[+] Exporté dans {OUTPUT_FILE} avec {len(df)} lignes (UTF-8 avec accents).")
