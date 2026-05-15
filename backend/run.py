import os

from app import create_app


app = create_app() # Instancia

if __name__ == "__main__":
    port = int(os.getenv("PORT", 17001))
    app.run(debug=True, port=port)