from os import environ


# BOT CONFIG
API_ID = environ.get("API_ID", 28542813)  # api id
API_HASH = environ.get("API_HASH", "02ce7c339f7776844ff4ab03da338ccd")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "7150456941:AAHpwRti35c-XCcZvSpyNDgr4lvaH0io6nI")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST", "redis-15567.c52.us-east-1-4.ec2.redns.redis-cloud.com")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT", 15567)  # redis port
REDIS_PASSWORD = environ.get(
    "REDIS_PASSWORD", "hZptmo0IxaOZG2zzAyweAoJ6W4mpv8pg"
)  # redis password


ADMINS = [6231550362]
OWNER_ID = 6231550362  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = -1002002020654  # CHAT WHERE YOU WANT TO STORE VIDEOS
USER_CHANNEL = -1002002020654
DUMP_CHANNEL = -1002002020654


# Config
COOKIE = environ.get("COOKIE", "PANWEB=1; csrfToken=Aib-iThW-6-vc1tk3h76BHvZ; browserid=VHTZhOscJptCPoAVrDLdoD1gE4lErsXeDB_Elcc-lc9HczX1PYC3w_9zDIQ=; lang=en; bid_n=18f753c1c3635204fd4207; ab_sr=1.0.1_MDljNmU5NWRlMTlkN2RlOWMzNzVhNzI1MmZlMWE5NTQzODQzM2IwZDNjZGI0ODVlM2FmMDhmMWMxMDVjMDc0NDI0YzMyMjFjZTIyYTJhNjczN2NhZGMzYWQxYzQwZGQ1YWRiOWI3ZjU4NWQ3MDZiY2NjMDM5NGRlZWU5YjNhYzRkMmVjYmFkZGE0ZTA5YjRmNmRlMDg3Y2IwYzA3NmVhZg==; ndus=Yz_k7K3teHuiq2aTON0jEAxh4uwhaNMK0pAXVnb-; ndut_fmt=67039EAB0C881A957473530301AC907BE9BC8FD2BB007C2D112CF229CBE20EFA")
