from fastapi import APIRouter, HTTPException, FastAPI, Depends
from surrealdb import Surreal, AsyncSurreal
from surrealdb.types import RecordID
import os

router = APIRouter(
    prefix="/db",
    tags=["db"],
)


# use signin instead of sign_in, its wrong in the docs ...
# Original 100% working code:
@router.post("/person")
async def test_person():
    try:
        async with AsyncSurreal(url="wss://quick-nebula-06bs6bc0h9uhjbjniqaseloagg.aws-euw1.surreal.cloud") as db:

            try:
                # Select namespace and database
                await db.use("Backbone", "Backbone")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"ns, db: {str(e)}")


            try:
                # Sign in to the database
                await db.signin({
                    "username": 'admin',
                    "password": 'ktET]xzP$2neuR#'
                })
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"signin3: {str(e)}")

            try:
                # Create a record
                await db.create(RecordID("person", "2"), {
                    "name": "Hans",
                    "Shoes": 2,
                })
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Create record: {str(e)}")

            # Select a specific record
            try:
                result = await db.select(RecordID("person", "2"))
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Select record: {str(e)}")

            return {"status": "success", "result": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")




# Version 2:
# (extracted get_db)

async def get_db():
    """Database dependency that provides a connected and authenticated SurrealDB instance"""
    db = None
    try:
        print("This is the updated db connection 2")
        db = AsyncSurreal(url="wss://quick-nebula-06bs6bc0h9uhjbjniqaseloagg.aws-euw1.surreal.cloud")
        
        # Connect to the database
        await db.connect()
        
        # Select namespace and database
        await db.use("Backbone", "Backbone")

        # Sign in to the database
        await db.signin({
            "username": 'admin',
            "password": 'ktET]xzP$2neuR#'
        })

        yield db
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")
    finally:
        # Always close the connection when the dependency is done
        if db:
            try:
                await db.close()
            except Exception as e:
                print(f"Warning: Error closing database connection: {str(e)}")

@router.post("/person")
async def test_person(db: AsyncSurreal = Depends(get_db)):
    """Test endpoint for creating and selecting a person record"""
    try:
        # Create a record
        await db.create(RecordID("person", "3"), {
            "name": "Hans",
            "Shoes": 2,
        })

        # Select a specific record
        result = await db.select(RecordID("person", "3"))

        return {"status": "success", "result": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database operation failed: {str(e)}")


# Version 3:
# (with env variables)

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

@router.post("/person")
async def test_person(db: AsyncSurreal = Depends(get_db)):
    """Test endpoint for creating and selecting a person record"""
    try:
        # Create a record
        await db.create(RecordID("person", "6"), {
            "name": "Hans",
            "Shoes": 2,
        })

        # Select a specific record
        result = await db.select(RecordID("person", "6"))

        return {"status": "success", "result": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database operation failed: {str(e)}")







