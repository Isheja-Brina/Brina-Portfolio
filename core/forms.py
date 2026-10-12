from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Your name",
        widget=forms.TextInput(attrs={
            "placeholder": "Enter your full name",
            "class": "form-input",
        })
    )

    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={
            "placeholder": "you@example.com",
            "class": "form-input",
        })
    )

    subject = forms.ChoiceField(
        label="What is this about?",
        choices=[
            ("recommendation", "Book recommendation"),
            ("feedback", "Website feedback"),
            ("support", "Help and support"),
            ("other", "Something else"),
        ],
        widget=forms.Select(attrs={"class": "form-input"})
    )

    message = forms.CharField(
        label="Your message",
        widget=forms.Textarea(attrs={
            "placeholder": "Write your message here...",
            "class": "form-input",
            "rows": 5,
        })
    )