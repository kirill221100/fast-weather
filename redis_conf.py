from core.config import Config as cfg
import aioredis

redis = aioredis.from_url(cfg.redis_url, decode_responses=True, password=cfg.redis_password)