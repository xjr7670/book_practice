from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=32, verbose_name='团体名称')
    group_script = models.CharField(max_length=60, verbose_name='备注')

    def __str__(self):
        return f'<{self.group_name}>'


class Employee(models.Model):
    name = models.CharField(max_length=32, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    dep_id = models.IntegerField(verbose_name='部门ID')

    def __repr__(self):
        return f'<{self.name}, {self.email}>'


class Employee2(models.Model):
    name = models.CharField(max_length=32, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    dep = models.ForeignKey(to="Department", on_delete=models.CASCADE)
    group = models.ManyToManyField(to="Group")
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    info = models.OneToOneField(to="EmployeeInfo", on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return f'<{self.name}, {self.email}>'


class Department(models.Model):
    dep_name = models.CharField(max_length=32, verbose_name='部门名称')
    dep_script = models.CharField(max_length=60, verbose_name='备注')

    def __repr__(self):
        return f'<{self.dep_name}>'


class EmployeeInfo(models.Model):
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)

    def __repr__(self):
        return f'<{self.phone}>'


