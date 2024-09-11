from setup import OURCURSOR,OURDB
class Course:
    def __init__(self,name,duration):
        self.name = name
        self.duration = duration
        # self.save_to_db()
        pass

    @classmethod
    def create_table(cls):
        """
        a method to create a relational database table for course class
        """
        sqlstatement = "CREATE TABLE IF NOT EXISTS courses(id INTEGER PRIMARY KEY, name TEXT, duration TEXT);"
        OURCURSOR.execute(sqlstatement)
        OURDB.commit()
        return "Courses table created successfully"
    
    def save_to_db(self):
        """
        instance method that saves the instance to DB
        """
        sqlstatement = "INSERT INTO courses (name, duration) VALUES (?,?);"
        OURCURSOR.execute(sqlstatement,(self.name,self.duration))
        OURDB.commit()
        return f"{self.name} has been created successfully"
    
    @classmethod
    def create_and_save(cls, name, duration):
        """
        a class method that will initialize and save an instance to db
        """
        # sd = Course("Software engineering","tyuio")
        # sd.save_to_db()
        new_course = Course(name, duration)
        new_course.save_to_db()
        return new_course

    
    pass

