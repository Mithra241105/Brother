# Brothers Day Wish Script

def wish_brother(name):
    message = f"Happy Brothers Day, {name}!\nYou are not just my brother, but also my best friend.\nThank you for always being there for me.\nWishing you lots of happiness and success!"
    print(message)

if __name__ == "__main__":
    brother_name = input("Enter your brother's name: ")
    wish_brother(brother_name)