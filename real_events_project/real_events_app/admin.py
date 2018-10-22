from django.contrib import admin
from real_events_app.models import Profession, Place, Meeting, Staff, Referee, Member, Team, NewsPost
from django import forms
from django_summernote.widgets import SummernoteWidget  

class PlaceAdminForm(forms.ModelForm):
    class Meta:
        model = Place
        widgets = {
            'post': SummernoteWidget(),
        }
        fields = '__all__'

class MeetingAdminForm(forms.ModelForm):
    class Meta:
        model = Meeting
        widgets = {
            'post': SummernoteWidget(),
        }
        fields = '__all__'

class StaffAdminForm(forms.ModelForm):
    class Meta:
        model = Staff
        widgets = {
            'post': SummernoteWidget(),
        }
        fields = '__all__'

class RefereeAdminForm(forms.ModelForm):
    class Meta:
        model = Referee
        widgets = {
            'post': SummernoteWidget(),
        }
        fields = '__all__'

class MemberAdminForm(forms.ModelForm):
    class Meta:
        model = Member
        widgets = {
            'post': SummernoteWidget(),
        }
        fields = '__all__'

class TeamAdminForm(forms.ModelForm):
    class Meta:
        model = Team
        widgets = {
            'post': SummernoteWidget(),
        }
        fields = '__all__'
class NewsPostAdminForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        widgets = {
            'post': SummernoteWidget(),
        }
        fields = '__all__'




class PlaceAdmin(admin.ModelAdmin):
    form = PlaceAdminForm
    list_display = ('title', 'city', 'address', 'image_tag')
    readonly_fields = ('image_tag',)

class MeetingAdmin(admin.ModelAdmin):
    form = MeetingAdminForm
    list_display = ('title', 'date', 'image_tag')
    readonly_fields = ('image_tag',)

class StaffAdmin(admin.ModelAdmin):
    form = StaffAdminForm
    list_display = ('name', 'image_tag')
    readonly_fields = ('image_tag',)

class RefereeAdmin(admin.ModelAdmin):
    form = RefereeAdminForm
    list_display = ('name', 'image_tag')
    readonly_fields = ('image_tag',)

class MemberAdmin(admin.ModelAdmin):
    form = MemberAdminForm
    list_display = ('name', 'image_tag')
    readonly_fields = ('image_tag',)
class TeamAdmin(admin.ModelAdmin):
    form = TeamAdminForm
    list_display = ('title', 'image_tag')
    readonly_fields = ('image_tag',)
class NewsPostAdmin(admin.ModelAdmin):
    form = NewsPostAdminForm
    list_display = ('title', 'image_tag')
    readonly_fields = ('image_tag',)

admin.site.register(Profession)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Referee, RefereeAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(NewsPost, NewsPostAdmin)

