module.exports = {
    apps: [
        {
            name: "appwrite-api",
            cwd: "C:/Users/PAUL/Desktop/angular_project/APPWRITE_API",
            script: "run.py",
            args: "application.main:app --host 0.0.0.0 --port 8030",
            interpreter: "C:/Users/PAUL/Desktop/angular_project/APPWRITE_API/env/Scripts/python.exe",
            watch: false,
            autorestart: true,
            env: {
                FLASK_ENV: "development",
                FLASK_DEBUG: "1"
            }
        }
    ]
}