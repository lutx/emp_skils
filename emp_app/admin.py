from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Employee, Technology, EmpTech



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'work_experience', 'bio', 'image', 'technology')
    search_fields = ('first_name', 'work_experience')

    def image(self, obj):
        return mark_safe('<img src="{employee_skils/images/emp}" width="{300px}" height={300px} />'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
        )
        )

    def __str__(self):
        return "<Employee: {} {}>".format(self.first_name, self.last_name)

class TechnologyAdmin(admin.ModelAdmin):
    fields = ['tech_name', 'description', 'logo']
    list_display = ('tech_name', 'description', 'logo')
    search_fields = ('tech_name', 'description')





class EmpTechAdmin(admin.ModelAdmin):
    #fields = ['technology.tech_name', 'employee.first_name']
    model = EmpTech
    list_display = ('Technology', 'name', 'skil_level')
    search_fields = ('employee', 'skil_level')

    def Technology(self, obj):
        return obj.technology.tech_name

    def name(self, obj):
        return obj.employee.first_name

    Technology.admin_order_field = 'technology'  # Allows column order sorting
    name.admin_order_field = 'employee'
    #get_name.short_description = 'Author Name'  # Renames column head


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(EmpTech, EmpTechAdmin)