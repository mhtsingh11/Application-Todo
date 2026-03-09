def read_lines_members_file():
    with open("members.txt", "r") as fileReadL:
        content_local = fileReadL.readlines()
        return content_local

def write_lines_members_file(writecontent):
    with open("members.txt", "w") as fileWrite:
        fileWrite.writelines(writecontent)