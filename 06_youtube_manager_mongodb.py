from pymongo import MongoClient
from bson import ObjectId

try:
    conn_string = "mongodb+srv://jaimindave:jaimindave477@youtubemanager.qp5of.mongodb.net/?retryWrites=true&w=majority&appName=YoutubeManager"
    client = MongoClient(conn_string, tlsAllowInvalidCertificates = True)
    # Not a good idea to include id and password in code files
except:
    raise Exception("Did not connect to Database")
    
db = client["ytmanager"]
video_collection = db["videos"]

def list_videos():
    try:
        for video in video_collection.find():
            print(f"\nID: {video['_id']}")
            print(f"Name: {video['name']}")
            print(f"Duration: {video['duration']}")
    except Exception as e:
        print(f"Error listing videos: {e}")

def add_video(name, duration):
    try:
        video_collection.insert_one({"name": name, "duration": duration})
        print("\nVideo added successfully !")
    except Exception as e:
        print(f"Error: {e}")

def update_video(id, new_name, new_duration):
    try:
        video_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"name": new_name, "duration": new_duration}}
            )
        print(f"\nVideo with the ID: {id} is updated successfully !")
    except Exception as e:
        print(f"Error: {e}")

def delete_video(id):
    try:
        video_collection.delete_one({"_id": ObjectId(id)})
        print(f"\nVideo with the ID: {id} was deleted successfully !")
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        print("\nYoutube Manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update video details")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter video name: ")
                duration = input("Enter video duration: ")
                add_video(name, duration)
            case '3':
                id = input("Enter video id: ")
                if video_collection.find_one({'_id': ObjectId(id)}):
                    print(video_collection.find_one({'_id': ObjectId(id)}))
                    new_name = input("Enter new name: ")
                    new_duration = input("Enter new duration: ")
                    update_video(id, new_name, new_duration)
                else:
                    print(f"Video with the ID: {id} was not found on Database !")
            case '4':
                id = input("Enter video id: ")
                if video_collection.find_one({'_id': ObjectId(id)}):
                    delete_video(id)
                else:
                    print(f"Video with the ID: {id} was not found on Database !")
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()