from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
import folium
from .addition_funcs import LatLngPopupModified
from .models import Memory
from .forms import MemoryForm

# adds additional functional to folium map (ability to save coordinates to the BD)
folium.LatLngPopup = LatLngPopupModified


def index(request):
    """Welcome page."""
    return render(request, 'main/index.html')


class Places(LoginRequiredMixin, ListView):
    """Users page with a list of all their memories."""
    model = Memory
    template_name = 'main/list_entry.html'
    context_object_name = "memories"
    # set up pagination - 3 entries on a page
    paginate_by = 3

    def get_queryset(self):
        """Show only memories, created by their owner."""
        if self.request.user:
            return Memory.objects.filter(owner=self.request.user).order_by('-date_added')


class Memories(LoginRequiredMixin, DetailView):
    """Page: detail view a memory."""
    model = Memory
    template_name = 'main/detail_entry.html'
    context_object_name = "place"

    def get_queryset(self):
        """Show only memories, created by their owner."""
        return Memory.objects.filter(owner=self.request.user).order_by('-date_added')

    def get_context_data(self, *, object_list=None, **kwargs):
        """Show map."""
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
        folium.Marker(location=[latitude, longitude],
                                    popup=popup,
                                    tooltip=f"Click me to get place name ! Full memory: {text}").add_to(m)
        folium.LatLngPopup().add_to(m)
        m = m._repr_html_()
        context['map'] = m
        return context


class MemoryUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Page: Update memory (for memory owner only)."""
    model = Memory
    form_class = MemoryForm
    template_name = 'main/update_entry.html'
    context_object_name = "place"
    # allow_empty = False
    success_url = reverse_lazy("main:places")
    success_message = 'Memory has been successfully updated!'

    def get_queryset(self):
        """Show only memories, created by their owner."""
        return Memory.objects.filter(owner=self.request.user).order_by('-date_added')

    def get_context_data(self, *, object_list=None, **kwargs):
        """Show map"""
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
        folium.Marker(location=[latitude, longitude],
                                    popup=popup,
                                    tooltip=f"Click me to get place name ! Full memory: {text}").add_to(m)
        folium.LatLngPopup().add_to(m)
        m = m._repr_html_()
        context['map'] = m
        return context


@login_required
def add_memory(request):
    """Page: Add a new memory."""
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            new_memory = form.save(commit=False)
            new_memory.owner = request.user
            new_memory.slug = slugify(new_memory.place) if slugify(new_memory.place) != '' else 'NoName'
            new_memory.save()
            messages.success(request, "The memory has been successfully added!")
            return HttpResponseRedirect(reverse('main:places'))
        else:
            messages.error(request, "Something went wrong, please check all the data add fill form again")

    form = MemoryForm()
    latitude = 0
    longitude = 0
    m = folium.Map([latitude, longitude], zoom_start=5)
    test = folium.Html('<strong>New place</strong>', script=True)
    popup = folium.Popup(test, max_width=2650)
    folium.Marker(location=[latitude, longitude],
                                popup=popup,
                                tooltip="Click me ").add_to(m)
    folium.LatLngPopup().add_to(m)
    m = m._repr_html_()

    context = {'map': m, 'form': form}
    return render(request, 'main/add_entry.html', context)


class MemoryDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Page: Delete memories."""
    model = Memory
    template_name = 'main/delete_entry.html'
    success_url = reverse_lazy("main:places")
    success_message = 'Memory about the place has been successfully deleted!'
    context_object_name = "place"

    def get_queryset(self):
        """Show only memories, created by their owner"""
        return Memory.objects.filter(owner=self.request.user).order_by('-date_added')


def page_not_found(request, exception):
    """Page not found."""
    # Переменная exception содержит отладочную информацию,
    # выводить её в шаблон пользовательской страницы 404 мы не станем
    return render(request, "404.html", {"path": request.path}, status=404)


def server_error(request):
    """In case of a server error."""
    return render(request, "500.html", status=500)
