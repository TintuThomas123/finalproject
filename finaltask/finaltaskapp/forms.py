from django import forms
from finaltaskapp.models import course,order

class Dateinp(forms.DateInput):
    input_type = 'date'
class orderForm(forms.ModelForm):
    class Meta:
        model=order
        fields='__all__'
        labels={"deptname": ("Department Name"),"coursename":("Course name"),}
        widgets={'dob':Dateinp(),}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['coursename'].queryset =course.objects.none()

        if 'dept' in self.data:
           try:
                dept_id = int(self.data.get('dept'))
                self.fields['coursename'].queryset = course.objects.filter(dept_id=dept_id).order_by('course_name')
           except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['coursename'].queryset = self.instance.deptname.coursename_set.order_by('course_name')
