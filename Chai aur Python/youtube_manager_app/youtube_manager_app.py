import json



def load_data(filename):
    try:
        with open(filename, "r") as file:
            test = json.load(file)
            print(test)
            return test
    except FileNotFoundError:
        return []

def save_data_helper(filename, videos):
    with open(filename, "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} Duration: {video['time']}")
    print("*" * 70)

def add_video(filename, videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(filename, videos)
    
def update_videos(filename, videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))

    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {"name": name, "time": time}
        save_data_helper(filename, videos)
    else:
         print("Invalid video index selected")

def delete_video(filename, videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))

    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(filename, videos)
    else:
        print("Invalid video index selected")



def main():

    filename = "youtube.txt"
    videos = load_data(filename)
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        choice = input("Enter your choice: ")
        print(videos)
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(filename, videos)
            case "3":
                update_videos(filename, videos)
            case "4":
                delete_video(filename,  videos)
            case "5":
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()