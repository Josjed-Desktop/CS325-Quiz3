def main():
    print("Welcome to a basic Python Program")
    x = 4
    y = 13
    y = x + y
    print(y)
    
    computerCourses = ["CS286", "CS325", "CS140", "CS150", "CS234", "CS111", "CS150"]
    
    for z in computerCourses:
        if z == "CS150":
            break
        else:
            print(z + "Course")
    
if __name__ == "__main__":
    main()  