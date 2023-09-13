from django import forms
g=[('Male','Male'),('Female','Female')]

c=[('python','Python'),('Django','Django'),('API','API'),('Flask','Flask')]




class RegiForm(forms.Form):

    Name=forms.CharField(max_length=100)
    Age=forms.IntegerField()
    Password=forms.CharField(widget=forms.PasswordInput)
    #Gender=forms.ChoiceField(choices=g)
    Gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect,required=False)
    #Course=forms.MultipleChoiceField(choices=c)
    Course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)

   
