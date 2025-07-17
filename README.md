## Just cloning and using the requirements.txt might be causing errors!!
## After cloning delete the git stuff!!!

## Git Workflow (Complete Setup)

### Clone this template and start with new history
```bash
# 1. Clone the repository with your custom name
git clone https://github.com/Readysoon/template.git my-new-project

# 2. Navigate into the new folder
cd my-new-project

# 3. Remove the existing git history
rm -rf .git

# 4. Initialize a new git repository
git init

# 5. Add all files to the new repository
git add .

# 6. Make your first commit
git commit -m "Initial commit: Based on https://github.com/Readysoon/template.git"

# 7. Add your new remote repository
git remote add origin https://github.com/Readysoon/my-new-project.git

# 8. Push to your new repository
git push -u origin main
```


### Initialize and Setup new Repository
```bash
# Initialize git repository
git init

# Set main as default branch (instead of master)
git branch -M main

# Add all files
git add .

# Initial commit
git commit -m "Initial commit"
```

### Create Remote Repository and Push
```bash
# Create remote repository on GitHub/GitLab (do this in browser first)
# Then connect and push (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git push -u origin main
```

### Alternative: One-liner for existing repos
```bash
# If you already have a remote repo created, just run:
git init && git branch -M main && git add . && git commit -m "Initial commit" && git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git && git push -u origin main
```


## Create venv
```bash
python -m venv venv
```

## activate venv
```bash
.\venv\Scripts\Activate
```

## install dependencies
```bash
pip install fastapi uvicorn surrealdb dotenv pydantic
```

## install dependencies (when installing previous requirements.txt; what you should prevent)
```bash
pip install -r requirements.txt
```

## freeze 
```bash
pip freeze > requirements.txt
```


## freeze 
```bash
deactivate
```




## Docker Part

```bash
docker-compose down
docker-compose build --no-cache
docker-compose up
```

## This error -> Restart Windows? Could also be network error:
```bash
1.929 pip._vendor.urllib3.exceptions.SSLError: [SSL: DECRYPTION_FAILED_OR_BAD_RECORD_MAC] decryption failed or bad record mac (_ssl.c:2590)
```

## 
```bash

```


## Database


## Surreal doesnt really support deploying to fly.io any more -> use Surreal Cloud for MVPs, other db providers can be chosen on a later stage

## To check credentials: login with philipp.gallaschik@code.berlin, click on the cloud db (quick-nebula in this case), "manage access" and then on System Users: "admin". 



## Signin error that cost me 3 hours
```bash
await db.signin({"user": DATABASE_USER, "pass": DATABASE_PASS})
->
await db.signin({"username": DATABASE_USER, "password": DATABASE_PASS})
```

## Surrealist

To login to the database connect to the database via HTTP and localhost:8000 and then ONLY select "Root" for authentication and Username = root, Password = root; if you select Namespace or Database for Authentication it wont work!


## Frontend

## In the project root execute (you might want to delete the frontend folder)
```bash
npx sv create frontend
```

## what to select in the sveltekit CLI
```bash
┌  Welcome to the Svelte CLI! (v0.6.13)
│
◇  Which template would you like?
│  SvelteKit minimal
│
◇  Add type checking with Typescript?
│  Yes, using Typescript syntax
│
◆  Project created
│
◇  What would you like to add to your project? (use arrow keys / space bar)
│  prettier, eslint
│
◇  Which package manager do you want to install dependencies with?
│  npm
│
◆  Successfully setup add-ons
│
◆  Successfully installed dependencies
│
◇  Successfully formatted modified files
│
◇  Project next steps ─────────────────────────────────────────────────────╮
│                                                                      	│
│  1: cd scanlytics2_FE                                                	│
│  2: git init && git add -A && git commit -m "Initial commit" (optional)  │
│  3: npm run dev -- --open                                            	│
│                                                                      	│
│  To close the dev server, hit Ctrl-C                                 	│
│                                                                      	│
│  Stuck? Visit us at https://svelte.dev/chat                          	│
│                                                                      	│
├──────────────────────────────────────────────────────────────────────────╯
│
└  You're all set!
```

## ... and create a suitable Dockerfile




