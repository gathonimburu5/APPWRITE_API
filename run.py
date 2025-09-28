import uvicorn
import webbrowser

if __name__ == "__main__":
    # url = "http://127.0.0.1:8030/docs"
    # webbrowser.open(url)
    uvicorn.run("application.main:app", host="127.0.0.1", port=8030, reload=True)