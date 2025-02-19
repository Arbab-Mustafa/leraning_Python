from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import pymongo
from bson import ObjectId  # Import to handle ObjectId conversion

# MongoDB Connection
MONGO_URI = "mongodb+srv://me:Ns2Jd8zrfRB4JxxD@cluster0.lf78r.mongodb.net/reactjs?retryWrites=true&w=majority"
client = pymongo.MongoClient(MONGO_URI)
db = client["reactjs"]  # Database Name
collection = db["users"]  # Collection Name


# Function to convert MongoDB documents to JSON serializable format
def json_serializer(data):
    if isinstance(data, list):  # If data is a list of documents
        return [
            {
                **doc,
                "_id": str(doc["_id"]),  # Convert _id to string
                "course": str(doc["course"]) if "course" in doc else None  # Convert course if it exists
            }
            for doc in data
        ]
    elif isinstance(data, dict):  # If data is a single document
        data["_id"] = str(data["_id"])
        if "course" in data:
            data["course"] = str(data["course"])
        return data
    return data


class SimpleAPI(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """Handle CORS Preflight"""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        """Handle GET request to fetch data from MongoDB"""
        if self.path == "/api/users":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            # Fetch data from MongoDB
            users = list(collection.find({}))  

            # Convert ObjectId fields to strings
            users = json_serializer(users)

            self.wfile.write(json.dumps(users).encode("utf-8"))
        else:
            self.send_error(404, "Not Found")


if __name__ == "__main__":
    port = 8000
    server = HTTPServer(("0.0.0.0", port), SimpleAPI)
    print(f"Server running on port {port}...")
    server.serve_forever()
