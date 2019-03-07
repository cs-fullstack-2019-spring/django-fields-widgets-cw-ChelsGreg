from django import forms
from .models import SuperHeroApp

# choices
RICH_POWER_CHOICES = (
    ('rich', 'Rich'),
    ('superpower', 'Superpower'),
)

# choices
SUPER_POWER_CHOICES = (
    ('flight', 'Flight'),
    ('speed', 'Speed'),
    ('telekenetic', 'Telekenetic'),
    ('healing', 'Healing'),
    ('invisibility', 'Invisibility'),
    ('time travel', 'Time Travel'),

)

# choices
GOOD_BAD_CHOICES = (
    ('good', 'Good'),
    ('kinda good', 'Kinda Good'),
    ('lukewarm', 'Lukewarm'),
    ('sorta evil', 'Sorta Evil'),
    ('hell hot', 'Hell Hot'),
)

# form for model
class SuperForm(forms.ModelForm):
    class Meta:
        model = SuperHeroApp
        fields = "__all__"
        # labels for form questions
        labels ={
            "name": "Name",
            "cityorigin": "City/Origin/Planet",
            "richpower": "Are you rich, or have superpowers?",
            "whichPower": "If superpower, which one(s)?",
            "goodEvil": "On a scale of Heaven and Hell, which are you?",
            "examples": "Give us 3 examples of when you used your super hero abilities:",
        }
        # to show specific widget types for form questions
        widgets = {
            "richpower": forms.RadioSelect(choices=RICH_POWER_CHOICES),
            "whichPower": forms.CheckboxSelectMultiple(choices=SUPER_POWER_CHOICES),
            "goodEvil": forms.Select(choices=GOOD_BAD_CHOICES),

        }