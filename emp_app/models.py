from django.db import models
from django.utils.translation import ugettext_lazy as _
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard
from jet.dashboard.dashboard_modules import google_analytics


class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
       self.available_children.append(google_analytics.GoogleAnalyticsVisitorsTotals)
       self.available_children.append(google_analytics.GoogleAnalyticsVisitorsChart)
       self.available_children.append(google_analytics.GoogleAnalyticsPeriodVisitors)


class Technology(models.Model):

    Langs = (
        ('PHP', 'PHP'),
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('C#', 'C#'),
        ('Java', 'Java'),
        ('C', 'C'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('SQL', 'SQL'),
        ('TypeScript', 'TypeScript'),
        ('Ruby', 'Ruby'),
    )
    tech_name = models.CharField(choices=Langs, max_length=100)
    description = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='images/technology/', blank=True, null=True)

    def __str__(self):
        return "{} {} {}".format(self.tech_name, self.description, self.logo)

class Employee(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, null=True, blank=True)
    work_experience = models.IntegerField( null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='images/emp/', blank=True, null=True)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {} {} {} {} {}>".format(
            self.first_name,
            self.last_name,
            self.email,
            self.work_experience,
            self.bio,
            self.image,
            self.technology.tech_name,
            self.technology.logo)

    def __repr__(self):
        return self.__str__()



class EmpTech(models.Model):

    Skills=(
        ('Junior', 'Junior'),
        ('Mid', 'Mid'),
        ('Senior', 'Senior')
    )
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,  on_delete=models.CASCADE)
    skil_level = models.CharField(max_length=30, choices=Skills)



    def __str__(self):
        return "{} {} {}".format(
            self.technology.tech_name,
            self.employee.first_name,
            self.skil_level)