from django.utils.translation import ugettext_lazy

from django.contrib.admin import AdminSite
from adminplus.sites import AdminSitePlus

from .models import *

class MyAdminSite(AdminSitePlus):
    # Text at the end of each page's <title>.
    site_title = ugettext_lazy('Nmemorial Admin')

    # Text in each page's <h1>.
    site_header = ugettext_lazy('Nmemorial Admin')

    # Text at the top of the admin index page.
    index_title = ugettext_lazy('Nmemorial Admin')


admin_site = MyAdminSite()


admin_site.register(Access)
admin_site.register(Memorial)
admin_site.register(DocumentGallery)
admin_site.register(PhotoGallery)
admin_site.register(ResetPwd)
admin_site.register(VideoGallery)


'''
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_url', 'content')

admin_site.register(Site, SiteAdmin)
'''