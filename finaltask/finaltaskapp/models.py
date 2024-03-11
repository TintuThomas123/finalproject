from django.db import models

 # Create your models here.

class department(models.Model):
    dept_name=models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name

class course(models.Model):
    dept=models.ForeignKey(department,on_delete=models.CASCADE)
    course_name=models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class order(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=100,choices=(('Female','Female'), ('Male','Male'),('Others','Others')),default=False)
    phno=models.IntegerField()
    mailid=models.EmailField()
    address=models.CharField(max_length=100)
    deptname=models.ForeignKey(department,on_delete=models.SET_NULL,blank=True,null=True,help_text="select Department")
    coursename=models.ForeignKey(course,on_delete=models.SET_NULL,blank=True,null=True)
    purpose=models.CharField(max_length=100,choices=(('for enquiry','for enquiry'), ('return','return'),('place order','place order')),default=False)

    exam_pappers=models.BooleanField(default=False)
    pen=models.BooleanField(default=False)
    notebook=models.BooleanField(default=False)
    def __str__(self):
        return self.name

