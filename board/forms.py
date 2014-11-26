from django import forms
from board.models import Service
from django.conf import settings
from bugzilla import Bugzilla
from datetime import datetime


class BugzillaForm(forms.Form):
        service = forms.ModelChoiceField(queryset=Service.objects.all())
        message = forms.CharField(widget=forms.Textarea)

        def submit(self):
            today = datetime.now().strftime('%Y-%m-%d %H:%M')
            bugzilla = Bugzilla(url=settings.BUGZILLA_URL)
            bugzilla.login(user=settings.BUGZILLA_USERNAME,
                           password=settings.BUGZILLA_PASSWORD)

            message = self.cleaned_data['message']
            service = self.cleaned_data['service'].name

            summary = '[dashboard] {0} Issue with {1}'.format(today, service)

            description = ("[dashboard]\n"
                           "Date: {0}\n"
                           "Message: {1}\n".format(today, message))

            bug = bugzilla.build_createbug(product=settings.BUGZILLA_PRODUCT,
                                           component=settings.BUGZILLA_COMPONENT,
                                           summary=summary,
                                           op_sys='All',
                                           platform='All',
                                           description=description,
                                           version='unspecified',
                                           )

            result = bugzilla.createbug(bug)
            return result.id
