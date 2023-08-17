from setuptools import setup

package_json = {
    "dependencies": {
        "@mapbox/leaflet-pip": "^1.1.0",
        "aos": "2.3.4",
        "baguettebox.js": "1.11.1",
        "bootstrap-autocomplete": "2.3.7",
        "bootstrap": "^5.1.3",
        "bootstrap-icons": "1.10.3",
        "datatables.net-bs5": "^1.13.6",
        "datatables.net-plugins": "^1.13.6",
        "datatables.net-buttons-bs5": "^2.3.6",
        "datatables.net-responsive-bs5": "^2.4.1",
        "datatables.net-searchbuilder-bs5": "^1.4.2",
        "datatables.net-searchpanes-bs5": "^2.1.2",
        "leaflet-imageoverlay-rotated": "^v0.2.1",
        "leaflet-draw": "^1.0.4",
        "leaflet-groupedlayercontrol": "^0.6.1",
        "leaflet.fullscreen": "2.2.0",
        "leaflet.markercluster": "^1.5.3",
        "leaflet": "^1.7.1",
        "jquery": "^3.7.0",
        "jquery-ui-dist": "^1.13.1",
        "popper.js": "1.16.0",
        "muuri": "^0.9.5"
    }
}

setup(
    name='tib',
    setup_requires=['calmjs'],
    package_json=package_json,
    py_modules=[]
)
