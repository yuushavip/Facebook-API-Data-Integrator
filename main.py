from models import user, post

def main():
    user_info = user.get_user_info()
    print(user_info)
            
if __name__ == "__main__":
    main()