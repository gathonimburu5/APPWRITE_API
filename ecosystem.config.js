module.exports = {
    apps: [
        {
            name: "appwrite-api",

            cwd: "C:/Users/PAUL/Desktop/angular_project/APPWRITE_API",

            script: "C:/Users/PAUL/Desktop/angular_project/APPWRITE_API/env/Scripts/uvicorn.exe",

            args: "-m uvicorn application.main:app --host 0.0.0.0 --port 8030",

            interpreter: "none",

            watch: false,

            autorestart: true
        }
    ]
}