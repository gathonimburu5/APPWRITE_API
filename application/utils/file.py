from fastapi import UploadFile
import os
import uuid

UPLOAD_DIR = os.path.join("static", "upload", "users")
DEFAULT_IMG = "profile.png"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def upload_profile(file: UploadFile = None) -> str:
    try:
        if file:
            _, ext = os.path.splitext(file.filename)
            ext = ext.lower()
            allowed_ext = [".jpg", ".jpeg", ".png", ".gif"]
            if ext not in allowed_ext:
                raise ValueError("unsupported file type")
            filename = f"{uuid.uuid4().hex}{ext}"
            file_path = os.path.join(UPLOAD_DIR, filename)
            with open(file_path, "wb") as buffer:
                buffer.write(file.file.read())
            return filename
        else:
            return DEFAULT_IMG
    except Exception as e:
        print(f"error occurred while uploading image: {e}")
        return DEFAULT_IMG