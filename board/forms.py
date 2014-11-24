from django import forms
from board.models import Service
from django.conf import settings
from bugzilla import Bugzilla


class BugzillaForm(forms.Form):
        name = forms.CharField(label='Your name', max_length=100)
        email = forms.EmailField()
        service = forms.ModelChoiceField(queryset=Service.objects.all())
        message = forms.CharField()

        def submit(self):
            bugzilla = Bugzilla(url=settings.BUGZILLA_URL)
            bugzilla.login(user=settings.BUGZILLA_USERNAME,
                           password=settings.BUGZILLA_PASSWORD)

            name = self.cleaned_data['name']
            email = self.cleaned_data['email']
            message = self.cleaned_data['message']
            service = self.cleaned_data['service'].name

            summary = '[dashboard] Issue with {0}'.format(service)

            description = ("From Dashboard:\n"
                           "Name: {0}\n"
                           "Email: {1}\n"
                           "Message: {2}\n".format(name, email, message))

            bug = bugzilla.build_createbug(product=settings.BUGZILLA_PRODUCT,
                                           component=settings.BUGZILLA_COMPONENT,
                                           summary=summary,
                                           op_sys='All',
                                           platform='All',
                                           description=description,
                                           version='unspecified',
                                           )

            result = bugzilla.createbug(bug)
            print result.id
