from folium import LatLngPopup
from jinja2 import Template


class LatLngPopupModified(LatLngPopup):
    """
    When one clicks on a Map that contains a LatLngPopup,
    a popup is shown that displays the latitude and longitude of the pointer.
    """
    _template = Template(u"""
            {% macro script(this, kwargs) %}
                var {{this.get_name()}} = L.popup();
                function latLngPop(e) {
                    {{this.get_name()}}
                        .setLatLng(e.latlng)
                        .setContent("Your place coordinates are: " +
                                    "<br>Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn({{this._parent.get_name()}});
                    parent.document.getElementById("id_lng").value = e.latlng.lng.toFixed(4);
                    parent.document.getElementById("id_lat").value = e.latlng.lat.toFixed(4);
                    }
                {{this._parent.get_name()}}.on('click', latLngPop);
            {% endmacro %}
            """)  # noqa

    def __init__(self):
        super(LatLngPopupModified, self).__init__()
        self._name = 'LatLngPopupModified'