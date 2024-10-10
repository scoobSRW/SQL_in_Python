import mysql.connector
from mysql.connector import Error


#connect 2 db
def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='Fitness_db',
            user='root',
            password='Actually_Not_Gonna_List_Just_Know_It_Worked_4_Me')
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None


#add member
def add_member():
    member_id = input("Enter Member ID: ")
    name = input("Enter Member Name: ")
    age = input("Enter Member Age: ")

    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            insert_query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (member_id, name, age))
            connection.commit()
            print("Member added successfully.")
        except Error as e:
            print(f"Failed to add member: {e}")
        finally:
            cursor.close()
            connection.close()


#add workout sesh
def add_workout_session():
    member_id = input("Enter Member ID: ")
    date = input("Enter Session Date (YYYY-MM-DD): ")
    time = input("Enter Session Time (e.g., 10:00 AM): ")
    activity = input("Enter Activity (e.g., Yoga): ")

    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            insert_query = """INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity)
                              VALUES (%s, %s, %s, %s)"""
            cursor.execute(insert_query, (member_id, date, time, activity))
            connection.commit()
            print("Workout session added successfully.")
        except Error as e:
            print(f"Failed to add workout session: {e}")
        finally:
            cursor.close()
            connection.close()


# update member age
def update_member_age():
    member_id = input("Enter Member ID: ")
    new_age = input("Enter New Age: ")

    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            check_query = "SELECT * FROM Members WHERE id = %s"
            cursor.execute(check_query, (member_id,))
            result = cursor.fetchone()

            if result:
                update_query = "UPDATE Members SET age = %s WHERE id = %s"
                cursor.execute(update_query, (new_age, member_id))
                connection.commit()
                print("Member's age updated successfully.")
            else:
                print("Member not found.")
        except Error as e:
            print(f"Failed to update member: {e}")
        finally:
            cursor.close()
            connection.close()


#delete sesh
def delete_workout_session():
    session_id = input("Enter Session ID: ")

    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            check_query = "SELECT * FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(check_query, (session_id,))
            result = cursor.fetchone()

            if result:
                delete_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
                cursor.execute(delete_query, (session_id,))
                connection.commit()
                print("Workout session deleted successfully.")
            else:
                print("Session not found.")
        except Error as e:
            print(f"Failed to delete session: {e}")
        finally:
            cursor.close()
            connection.close()


#get members in age range
def get_members_in_age_range():
    start_age = input("Enter Start Age: ")
    end_age = input("Enter End Age: ")

    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s"
            cursor.execute(query, (start_age, end_age))
            results = cursor.fetchall()

            if results:
                print("Members between the ages", start_age, "and", end_age)
                for row in results:
                    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
            else:
                print("No members found in the specified age range.")
        except Error as e:
            print(f"Failed to retrieve members: {e}")
        finally:
            cursor.close()
            connection.close()


# main loop playaaa
def main():
    while True:
        print("\n--- Gym Management System ---")
        print("1. Add a Member")
        print("2. Add a Workout Session")
        print("3. Update Member Age")
        print("4. Delete a Workout Session")
        print("5. Get Members in Age Range")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_member()
        elif choice == '2':
            add_workout_session()
        elif choice == '3':
            update_member_age()
        elif choice == '4':
            delete_workout_session()
        elif choice == '5':
            get_members_in_age_range()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
