var map = L.map('map').setView([30, 0], 2);

L.control.scale().addTo(map);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

L.geoJSON(gisData).addTo(map);

map.fitBounds(L.geoJSON(gisData).getBounds(), {
    maxZoom: 13
});

var layerGroup = L.geoJSON(gisData, {
    onEachFeature: function (feature, layer) {
        console.log(feature)
        layer.bindPopup('<b>' + entityName + '</b><p><b>' + feature.title + ':</b> ' + feature.description + '</p>');
    }
}).addTo(map);


// Define base layers
const OpenStreetMap_HOT = L.tileLayer(
    "https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png",
    {
        maxZoom: 25,
        maxNativeZoom: 20,
        attribution:
            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>',
    }
);
const OpenStreetMap = L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
        attribution:
            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 25,
        maxNativeZoom: 19,
    }
);
const Esri_WorldImagery = L.tileLayer(
    "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    {
        attribution:
            "&copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community",
        maxZoom: 25,
        maxNativeZoom: 19,
    }
);
const TopoOsm = L.tileLayer.wms("http://ows.mundialis.de/services/service?", {
    layers: "TOPO-OSM-WMS",
    attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 25,
    maxNativeZoom: 19,
});
const baseMaps = {
    Landscape: OpenStreetMap_HOT,
    Streetmap: OpenStreetMap,
    Satellite: Esri_WorldImagery,
    Topography: TopoOsm,
};
baseMaps.Landscape.addTo(map);
const control = L.control.groupedLayers(baseMaps).addTo(map);