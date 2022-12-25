from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify

from .forms import MemoryForm
from django.contrib.auth.decorators import login_required
from .models import Memory
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

from django.http import Http404, HttpResponseRedirect
import folium


from branca.element import MacroElement           # delete it
from jinja2 import Template                       # delete it


def index(request):
    """Welcome page"""
    return render(request, 'main/index.html')


class Places(ListView):
    """Users page with a list of all their memories"""
    model = Memory
    template_name = 'main/list_entry.html'
    # все данные по умолчанию находятся в переменной "object_list" (использовать её в template.py)
    # переопределить имя переменной "object_list" чтобы в template использовать переменную 'news' если нам так УДОБНЕЕ.
    context_object_name = "memories"
    # несуществующие страницы(в списке такого значения нет) будут показаны как 404
    # allow_empty = False


class Memories(DetailView):
    model = Memory
    template_name = 'main/detail_entry.html'
    context_object_name = "place"
    # allow_empty = False


# class LatLngPopup(MacroElement):
#     """
#     When one clicks on a Map that contains a LatLngPopup,
#     a popup is shown that displays the latitude and longitude of the pointer.
#     """
#     _template = Template(u"""
#             {% macro script(this, kwargs) %}
#                 var {{this.get_name()}} = L.popup();
#                 function latLngPop(e) {
#                     {{this.get_name()}}
#                         .setLatLng(e.latlng)
#                         .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
#                                     "<br>Longitude: " + e.latlng.lng.toFixed(4))
#                         .openOn({{this._parent.get_name()}});
#                     parent.document.getElementById("id_lng").value = e.latlng.lng.toFixed(4);
#                     parent.document.getElementById("id_lat").value = e.latlng.lat.toFixed(4);
#                     }
#                 {{this._parent.get_name()}}.on('click', latLngPop);
#             {% endmacro %}
#             """)  # noqa
#
#     def __init__(self):
#         super(LatLngPopup, self).__init__()
#         self._name = 'LatLngPopup'


class MemoryUpdate(SuccessMessageMixin, UpdateView):
    """Page: Update memory (for memory owner only)"""
    model = Memory
    form_class = MemoryForm
    template_name = 'main/update_entry.html'
    context_object_name = "place"
    allow_empty = False
    success_url = reverse_lazy("main:places")
    success_message = 'Memory has been successfully updated!'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # getting coordinates for already existing point
        if self.object.latitude and self.object.longitude:
            latitude = self.object.latitude
            longitude = self.object.longitude
        else:
            latitude = 0
            longitude = 0
        # Getting place name
        if self.object.place:
            place = self.object.place

        # Getting place name
        if self.object.text:
            text = self.object.text

        m = folium.Map([latitude, longitude], zoom_start=5)
        test = folium.Html(f'<strong>{place}</strong>', script=True)
        popup = folium.Popup(test, max_width=2650)
        folium.RegularPolygonMarker(location=[latitude, longitude],
                                    popup=popup,
                                    tooltip=f"Click me to get place name ! Full memory: {text}").add_to(m)
        folium.LatLngPopup().add_to(m)
        m = m._repr_html_()
        context['map'] = m
        return context


# class MemoryAdd(SuccessMessageMixin, CreateView, PermissionRequiredMixin):
#     """Page: Add new memories """
#     #permission_required = 'news.can_delete_news_article'
#
#     model = Memory
#     form_class = MemoryForm
#     template_name = 'main/add_entry.html'
#     success_url = reverse_lazy("main:places")
#     success_message = f'Memory about the place has been successfully added!'
#     context_object_name = "place"
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         latitude = 0
#         longitude = 0
#         m = folium.Map([latitude, longitude], zoom_start=5)
#         test = folium.Html(f'<strong>New place</strong>', script=True)
#         popup = folium.Popup(test, max_width=2650)
#         folium.RegularPolygonMarker(location=[latitude, longitude],
#                                     popup=popup,
#                                     tooltip=f"Click me ").add_to(m)
#         folium.LatLngPopup().add_to(m)
#         m = m._repr_html_()
#         context['map'] = m
#         return context


def add_memory(request):

    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            new_memory = form.save(commit=False)
            new_memory.owner = request.user
            new_memory.slug = slugify(new_memory.place)
            new_memory.save()
            return HttpResponseRedirect(reverse('main:places'))
        else:
            error = 'Something went wrong, please check all the data add fill form again.'

    form = MemoryForm()
    latitude = 0
    longitude = 0
    m = folium.Map([latitude, longitude], zoom_start=5)
    test = folium.Html(f'<strong>New place</strong>', script=True)
    popup = folium.Popup(test, max_width=2650)
    folium.RegularPolygonMarker(location=[latitude, longitude],
                                popup=popup,
                                tooltip=f"Click me ").add_to(m)
    folium.LatLngPopup().add_to(m)
    m = m._repr_html_()
    context = {'map': m, 'form': form}
    return render(request, 'main/add_entry.html', context)








class MemoryDelete(SuccessMessageMixin, DeleteView, PermissionRequiredMixin):
    """Page: Delete memories """
    #permission_required = 'news.can_delete_news_article'

    model = Memory
    template_name = 'main/delete_entry.html'
    success_url = reverse_lazy("main:places")
    success_message = f'Memory about the place has been successfully deleted!'
    context_object_name = "place"




