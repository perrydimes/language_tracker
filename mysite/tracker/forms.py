from django.forms import ModelForm, DateInput
from tracker.models import Entry, Tag

class EntryForm(ModelForm):
  class Meta:
    model = Entry
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'date': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EntryForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    #datetime.strptime(d, '%b %d %Y %I:%M%p')
    #self.fields['date'].input_formats = ('%Y-%m-%d',)
