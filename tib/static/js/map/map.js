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
    layer.bindPopup('<b>'+entityName+'</b><p><b>'+feature.title+':</b> '+feature.description+'</p>');
  }
}).addTo(map);

