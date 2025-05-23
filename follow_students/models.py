from django.db import models

# Create your models here.
class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_rol

class Permiso(models.Model):
    nombre_permiso = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_permiso

class User(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE) 

    def __str__(self):
        return self.username

class RolPermiso(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)

class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.code
      
class Major(models.Model):
    name = models.CharField(max_length=255)
    price= models.IntegerField()

    def __str__(self):
        return self.name

class Donor(models.Model):
    cedula = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mail = models.EmailField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Amount(models.Model):
    code = models.CharField(max_length=20, unique=True, default = "23")
    transport = models.IntegerField()
    alimentation = models.IntegerField()
    academic = models.IntegerField()

    def __str__(self):
         text ="{}".format(self.code)
         return text
    
class ScholarshipGoal(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class ScholarshipGoalAssociation(models.Model):
    scholarship = models.ForeignKey('Scholarship', on_delete=models.CASCADE)
    goal = models.ForeignKey(ScholarshipGoal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.scholarship.name} - {self.goal.description}"

class Scholarship(models.Model):
    code  = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    amount = models.ForeignKey(Amount, on_delete=models.CASCADE)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    assigned_students = models.PositiveIntegerField(default=0)
    academic_percentage = models.IntegerField(default = 70)
    transportation= models.IntegerField(default = 1000000)
    image = models.CharField(max_length= 255 ,default = "favicon_ICESI.png")
    goals = models.ManyToManyField(ScholarshipGoal, through=ScholarshipGoalAssociation, blank=True)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    date = models.DateField()
    icfes = models.IntegerField()
    cedula = models.CharField(max_length=20)
    code = models.CharField(max_length=20, unique=True)
    mail = models.EmailField()
    scholarship = models.ForeignKey(Scholarship, on_delete=models.SET_NULL, null=True, blank=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    aux_transportation = models.CharField(max_length=100, unique= False , default=0)
    aux_academic = models.CharField(max_length=100, unique= False , default=0)

    def has_scholarships(self):
        return self.scholarship is not None
    
    def get_scholarship_goals(self):
        if self.scholarship:
            return self.scholarship.goals.all()
        return []
    
    def __str__(self):
        return self.name
      
class Scholarship_expense(models.Model):
    student = models.ForeignKey(Student, null=True, on_delete= models.CASCADE, unique = False)
    scholarship = models.ForeignKey(Scholarship, null = True, on_delete= models.CASCADE, unique = False)
    money_quantity = models.FloatField()
    accumulated_time = models.IntegerField()
    class Time_way(models.TextChoices):
        DIAS = "1", "Dias"
        MES = "2", "Mes"
        ANIO = "3", "Año"

    selected_time = models.CharField(
        max_length = 2,
        choices = Time_way.choices,
        default = Time_way.DIAS 
    )
    type_mount = models.CharField(max_length = 20, unique = False)

    def __str__(self):
        text = self.estudiante.codigo
        return text

class SupportCenter(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Consult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    support_center = models.ForeignKey(SupportCenter, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    outcome = models.TextField()
    
    def __str__(self):
        return f'Consulta realizada por {self.student.name} el {self.date}'

class Grade(models.Model):
    grade = models.FloatField()
    state= models.BooleanField(default=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.student.code


class NonAcademicActivity(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
      
class RegisNonAcademicActivity(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    activity = models.ForeignKey(NonAcademicActivity, on_delete=models.CASCADE)
    assistance_days = models.CharField(max_length=100)

    def __str__(self):
        return f'Registro de {self.student.name} en {self.activity.name}'

class Notification(models.Model):
     name=models.TextField(default="Notificacion")
     student = models.ForeignKey(Student, on_delete=models.CASCADE)
     description=models.TextField()
     state= models.BooleanField(default=True)
     
     def __str__(self):
        name=self.name
        return name