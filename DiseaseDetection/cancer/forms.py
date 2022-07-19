from django.forms import ModelForm
from .models import LungCancerText
from .models import BrestCancerText

class LungCancerTextForm(ModelForm):
  class Meta:
    model = LungCancerText
    fields = "__all__"
    exclude = ["user"]
  
  def __init__(self, *args, **kwargs):
        super(LungCancerTextForm, self).__init__(*args, **kwargs)
        for _,field in self.fields.items():
          field.widget.attrs.update({'class': 'focus:ring-indigo-500 focus:border-indigo-500 flex-1 block w-full rounded-none rounded-r-md sm:text-sm border-gray-300 p-2'})
          
class BrestCancerForm(ModelForm):
  class Meta:
    model = BrestCancerText
    fields = "__all__"
    exclude = ["user"]
  
  def __init__(self, *args, **kwargs):
        super(BrestCancerForm, self).__init__(*args, **kwargs)
        for _,field in self.fields.items():
          field.widget.attrs.update({'class': 'focus:ring-indigo-500 focus:border-indigo-500 flex-1 block w-full rounded-none rounded-r-md sm:text-sm border-gray-300 p-2'})