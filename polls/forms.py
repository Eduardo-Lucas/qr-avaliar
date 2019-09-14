from django.forms import ModelForm, inlineformset_factory
from polls.models import Question, Choice


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('question_text', )


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text', 'votes', )


QuestionChoiceFormSet = inlineformset_factory(Question, Choice,
                                              form=ChoiceForm, extra=2)
