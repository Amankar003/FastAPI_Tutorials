from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, utils
from auth_database import get_db


SECRET_KEY = "KUEY3iUMKeesNus7lTrQYR8szXlGQkB07Uz9yOrPx78"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
