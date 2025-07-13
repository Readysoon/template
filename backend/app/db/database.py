from fastapi import APIRouter, HTTPException, FastAPI, Depends
from surrealdb import Surreal, AsyncSurreal
import os

router = APIRouter(
    prefix="/db",
    tags=["db"],
)

DATABASE_URL = os.getenv("SURREALDB_URL")
DATABASE_USER = os.getenv("SURREALDB_USER")
DATABASE_PASS = os.getenv("SURREALDB_PASS")
DATABASE_NAMESPACE = os.getenv("SURREALDB_NAMESPACE")
DATABASE_NAME = os.getenv("SURREALDB_DATABASE")

async def get_db():
    """Database dependency that provides a connected and authenticated SurrealDB instance"""
    db = None
    try:
        print("This is the updated db connection 3")
        print(DATABASE_URL, DATABASE_USER, DATABASE_PASS, DATABASE_NAMESPACE, DATABASE_NAME)
        
        # Initialize the database connection
        db = AsyncSurreal(DATABASE_URL)
        
        # Connect to the database
        await db.connect()
        
        # Select namespace and database
        await db.use(DATABASE_NAMESPACE, DATABASE_NAME)

        # Sign in to the database
        await db.signin({
            "username": DATABASE_USER,
            "password": DATABASE_PASS
        })

        yield db
        
    except Exception as e:
        print(f"Database connection error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")
    finally:
        # Always close the connection when the dependency is done
        if db is not None:
            try:
                await db.close()
            except Exception as e:
                print(f"Warning: Error closing database connection: {str(e)}")







