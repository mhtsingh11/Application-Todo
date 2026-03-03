import funtions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

print("----Hello and welcome to Members program----")

while True:
    option = input("------You can add, edit, show, remove, quit ------\n")
    content = []
    if option.startswith('add'):
        writeMe = input("Add members to add: ")

        #Read the members.txt file and add the content which is
        #already there into content list so it can be written later
        content.append(funtions.read_members_file())

        #Open members.txt and write the existing and new content to the file
        content.append(writeMe + "\n")

        funtions.write_lines_members_file(content)

        with open("members.txt", "r") as fileRead:
            print(fileRead.read())

    elif option.startswith('edit'):
        try:
            index = int(input("Enter index for member which you need to edit: "))

            content = funtions.read_lines_members_file()

            content[index-1] = input("Enter new value : ") + "\n"
            funtions.write_lines_members_file(content)

        except IndexError:
            print(f"The edit index is out of bonds , please enter value below : {len(content)}")
            continue

    elif option.startswith('show'):
        content = funtions.read_lines_members_file()

        print("|Index - Member|")
        for i , member in enumerate(content):
            row = f"|{i+1}-{member.strip('\n')}|"
            print(row.strip())

    elif option.startswith('remove'):
        try:
            index = int(input("Enter index of member which you need to remove : "))
            content = funtions.read_lines_members_file()

            removedItem = content[index-1]
            content.pop(index-1)

            funtions.write_lines_members_file(content)

            print(f"The removed member from list is {removedItem}")
        except IndexError:
            print(f"The edit index is out of bonds , please enter value below : {len(content)}")
            continue

    elif option.startswith('quit'):
        break

    else:
        print("You entered a wrong option, please try again!")

print("Thank you, Byeeee !!!")