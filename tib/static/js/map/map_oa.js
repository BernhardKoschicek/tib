map = L.map("map", {maxZoom: mapMaxZoom, fullscreenControl: true});
map.createPane('pointsPane');
map.createPane('linesPane');
map.createPane('polygonsPane');
L.control.scale().addTo(map);
// Icons
const newIcon = L.icon({
    iconUrl: "/static/images/map/marker-icon_new.png",
    iconAnchor: [12, 41],
    popupAnchor: [0, -34],
});
const editIcon = L.icon({
    iconUrl: "/static/images/map/marker-icon_edit.png",
    iconAnchor: [12, 41],
    popupAnchor: [0, -34],
});
const editedIcon = L.icon({
    iconUrl: "/static/images/map/marker-icon_edited.png",
    iconAnchor: [12, 41],
    popupAnchor: [0, -34],
});
const grayMarker = L.icon({
    iconUrl: "/static/images/map/marker-icon-gray.png",
    iconAnchor: [12, 41],
    popupAnchor: [0, -34],
});
const superMarker = L.icon({
    iconUrl: "/static/images/map/marker-icon-orange.png",
    iconAnchor: [12, 41],
    popupAnchor: [0, -34],
});
const subsMarker = L.icon({
    iconUrl: "/static/images/map/marker-icon-green.png",
    iconAnchor: [12, 41],
    popupAnchor: [0, -34],
});
const siblingsMarker = L.icon({
    iconUrl: "/static/images/map/marker-icon-gray.png",
    iconAnchor: [12, 41],
    popupAnchor: [0, -34],
});

const myCircleStyle = {
    color: "#000000",
    weight: 1,
    fillOpacity: 0.8,
    fillColor: "#007bd9",
    radius: 10,
};

const getWeight = (feature) =>
    feature?.properties?.shapeType === "area" ? 0 : 2;
const selectedPolygonStyle = (feature) => {
    return {
        weight: getWeight(feature),
    };
};
const polygonStyle = (feature) => {
    return {
        color: "#9A9A9A",
        weight: getWeight(feature),
        fillOpacity: .5
    };
};
const siblingStyle = (feature) => {
    return {
        color: "rgb(111,111,111)",
        weight: getWeight(feature),
    };
};

const superStyle = (feature) => {
    return {
        color: "rgb(255,231,191)",
        weight: getWeight(feature),
    };
};

const subStyle = (feature) => {
    return {
        color: "rgb(39,207,59)",
        weight: getWeight(feature),
    };
};

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

// Filter to get different types from the geojson
const pointFilter = (feature) => feature?.geometry?.type === "Point";
const polygonFilter = (feature) => feature?.geometry?.type === "Polygon";
const lineFilter = (feature) => feature?.geometry?.type === "LineString";


const gisAll = [...gisPointAll, ...gisPolygonAll, ...gisLineAll];

//take selected from hidden fields if exist
const hiddenFieldPoints = $("#gis_points")?.val(),
    hiddenFieldsLines = $("#gis_lines")?.val(),
    hiddenFieldsPolygons = $("#gis_polygons")?.val();
const gisSelected = [
    ...(!hiddenFieldPoints || hiddenFieldPoints === "[]" ? gisPointSelected : JSON.parse(hiddenFieldPoints)),
    ...(!hiddenFieldsLines || hiddenFieldsLines === "[]" ? gisLineSelected : JSON.parse(hiddenFieldsLines)),
    ...(!hiddenFieldsPolygons || hiddenFieldsPolygons === "[]" ? gisPolygonSelected : JSON.parse(hiddenFieldsPolygons)),
];

const pointLayer = new L.GeoJSON(gisAll, {
    filter: pointFilter,
    onEachFeature: setPopup(false),
    pointToLayer: function (feature, latlng) {
        return L.circleMarker(latlng, myCircleStyle);
    },
});
const polygonLayer = new L.GeoJSON(gisAll, {
    onEachFeature: setPopup(false),
    style: polygonStyle,
    filter: polygonFilter,
});
const linestringLayer = new L.GeoJSON(gisAll, {
    onEachFeature: setPopup(false),
    style: {color: "#9A9A9A"},
    filter: lineFilter,
});
let selectedLayer = L.geoJson(gisSelected, {
    onEachFeature: setPopup(true),
    style: selectedPolygonStyle,
}).addTo(map);

//supers
const pointLayerSupers = new L.GeoJSON(gisPointSupers, {
    filter: pointFilter,
    onEachFeature: setPopup(false),
    pointToLayer: function (feature, latlng) {
        return L.marker(latlng, {icon: superMarker});
    },
});
const polygonLayerSupers = new L.GeoJSON(gisPointSupers, {
    filter: polygonFilter,
    style: superStyle,
    onEachFeature: setPopup(false),
});
const linestringLayerSupers = new L.GeoJSON(gisPointSupers, {
    filter: lineFilter,
    style: superStyle,
    onEachFeature: setPopup(false),
});
//siblings
const pointLayerSiblings = new L.GeoJSON(gisPointSibling, {
    filter: pointFilter,
    onEachFeature: setPopup(false),
    pointToLayer: function (feature, latlng) {
        return L.marker(latlng, {icon: siblingsMarker});
    },
});
const polygonLayerSiblings = new L.GeoJSON(gisPointSibling, {
    filter: polygonFilter,
    style: siblingStyle,
    onEachFeature: setPopup(false),
});
map.addLayer(polygonLayerSiblings);
const linestringLayerSiblings = new L.GeoJSON(gisPointSibling, {
    filter: lineFilter,
    style: siblingStyle,
    onEachFeature: setPopup(false),
});
//subs
const pointLayerSubs = new L.GeoJSON(gisPointSubs, {
    filter: pointFilter,
    onEachFeature: setPopup(false),
    pointToLayer: function (feature, latlng) {
        return L.marker(latlng, {icon: subsMarker});
    },
});
const polygonLayerSubs = new L.GeoJSON(gisPointSubs, {
    filter: polygonFilter,
    style: subStyle,
    onEachFeature: setPopup(false),
});
const linestringLayerSubs = new L.GeoJSON(gisPointSubs, {
    filter: lineFilter,
    style: subStyle,
    onEachFeature: setPopup(false),
});

//clustering
const cluster = L.markerClusterGroup({
    showCoverageOnHover: false,
    maxClusterRadius: maxClusterRadius,
    disableClusteringAtZoom: disableClusteringAtZoom,
});
cluster.addLayer(pointLayer);
map.addLayer(cluster);

baseMaps.Landscape.addTo(map);

const allSelectedLayer = [
    selectedLayer,
    pointLayerSupers,
    pointLayerSiblings,
    pointLayerSubs,
];
const allSelected = [
    ...gisSelected,
    ...gisPointSupers,
    ...gisPointSibling,
    ...gisPointSubs,
];
if (allSelected?.length > 0)
    map.fitBounds(L.featureGroup(allSelectedLayer).getBounds(), {
        maxZoom: mapDefaultZoom,
    });
else if (Object.keys(pointLayer?.getBounds()).length !== 0)
    map.fitBounds(pointLayer.getBounds(), {maxZoom: mapDefaultZoom});
else map.setView([30, 0], 2);

// Overlay maps
let overlayMapsControl = {};
overlays.forEach((o) => {
    if (!o?.boundingBox.length === 2 && !o?.boundingBox.length === 3) return;

    const imageOverlay =
        o?.boundingBox.length === 2
            ? L.imageOverlay("/display/" + o.image, o.boundingBox)
            : L.imageOverlay.rotated(
                "/display/" + o.image,
                L.latLng(o.boundingBox[0]),
                L.latLng(o.boundingBox[1]),
                L.latLng(o.boundingBox[2])
            );
    imageOverlay.addTo(map);
    overlayMapsControl[o.name] = imageOverlay;
});

//controll grouped layers
const groupedOverlays = {
    Places: {
        Cluster: cluster,
        Markers: pointLayer,
    },
    General: {
        Polygons: polygonLayer,
        Linestrings: linestringLayer,
    },
    Subunits: {
        ...(pointLayerSupers?.getLayers().length > 0 && {
            SuperPoints: pointLayerSupers,
        }),
        ...(polygonLayerSupers?.getLayers().length > 0 && {
            SuperPolygons: polygonLayerSupers,
        }),
        ...(linestringLayerSupers?.getLayers().length > 0 && {
            SuperLines: linestringLayerSupers,
        }),
        ...(pointLayerSiblings?.getLayers().length > 0 && {
            SiblingPoints: pointLayerSiblings,
        }),
        ...(polygonLayerSiblings?.getLayers().length > 0 && {
            SiblingPolygons: polygonLayerSiblings,
        }),
        ...(linestringLayerSiblings?.getLayers().length > 0 && {
            SiblingLines: linestringLayerSiblings,
        }),
        ...(pointLayerSubs?.getLayers().length > 0 && {
            SubPoints: pointLayerSubs,
        }),
        ...(polygonLayerSubs?.getLayers().length > 0 && {
            SubPolygons: polygonLayerSubs,
        }),
        ...(linestringLayerSubs?.getLayers().length > 0 && {
            SubLines: linestringLayerSubs,
        }),
        ...overlayMapsControl,
    },
};
const GroupOptions = {
    exclusiveGroups: ["Places"],
    groupCheckboxes: true,
};
L.Control.GroupedLayers.include({
    getActiveOverlays: function () {
        const active = this._layers
            .filter(x => x.name.includes("Polygons"))
            .flatMap(x => map.hasLayer(x.layer) ? Object.values(x.layer._layers) : [])
        return L.layerGroup(active);
    }
});
const control = L.control.groupedLayers(baseMaps, groupedOverlays, GroupOptions).addTo(map);

const geoSearchControl = L.control.geonames({
    username: geoNamesUsername, // Geonames account username.  Must be provided.
    maxresults: 8, // Maximum number of results to display per search.
    zoomLevel: 12, // Max zoom level to zoom to for location. If null, will use the map's max zoom level.
    featureClasses: ["A", "H", "L", "P", "R", "T", "U", "V", "S"], // Feature classes to search against.  See: http://www.geonames.org/export/codes.html.
    showMarker: false, // Show a marker at the location the selected location.
    showPopup: true, // Show a tooltip at the selected location.
    enablePostalCodes: true, // If true, use postalCodesRegex to test user provided string for a postal code.  If matches, then search against postal codes API instead.
    postalCodesRegex:
        /^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$/, // Regex used for testing user provided string for a postal code.  If this test fails, the default geonames API is used instead.
    title: translate["map_geonames_title"], // Search input title value.
    placeholder: translate["map_geonames_placeholder"], // Search input placeholder text.
});
geoSearchControl.on("select", function (e) {
    if (geoNamesModule) {
        const popup = `<div>
                  <a href='https://www.geonames.org/${e.geoname.geonameId}' target='_blank'>${e.geoname.name}</a><br>
                  <div id="buttonBar" style="white-space:nowrap;">
                    <p>
                        <button class="${style.button.primary}" id="ImportGeonamesID">Import ID</button>
                        <button class="${style.button.primary}" id="ImportCoordinates">Import Coordinates</button><br><br>
                        <button class="${style.button.primary}" id="ImportAll">Import ID and Coordinates</button>
                    </p>
                </div>
            </div>`;
        e.target._map.on("opengeopopup", (p) => {
            p.popup.setContent(popup);
            p.popup.update();
            $("#ImportCoordinates")
                .click(() => importNewPoint(e.geoname, p.popup, map));
            $("#ImportGeonamesID")
                .click(() => importGeonamesID(e.geoname, p.popup, map));
            $("#ImportAll").click(() => importAll(e.geoname, p.popup, map));
        });
    }
});
map.addControl(geoSearchControl);

function setPopup(selected) {
    return (feature, layer) => {
        //set panes depending on geometry type
        const panes = {
            'Polygon': "polygonsPane",
            'LineString': "linesPane",
            'Point': "pointsPane"
        }
        layer.options.pane = panes[feature.geometry.type];

        layer.bindPopup(buildPopup(feature, "view", selected));

        // Handle overlay of multiple polygons
        layer.on('click', function (e) {
            if (e.sourceTarget.feature.geometry.type === 'Point'
                || e.sourceTarget.feature.geometry.type === 'LineString') return;
            const active = control.getActiveOverlays();
            const match = [
                ...leafletPip.pointInLayer(e.latlng, selectedLayer, false),
                ...(typeof drawnItems !== 'undefined') ?
                    leafletPip.pointInLayer(e.latlng, drawnItems, false) : [],
                ...(typeof currentEditLayer !== 'undefined') ?
                    leafletPip.pointInLayer(e.latlng,
                        L.layerGroup([currentEditLayer]), false) : [],
                ...leafletPip.pointInLayer(e.latlng, active, false)];
            if (match.length > 1) {
                const content =
                    `<div id="popup" class="d-flex flex-column">
                       <strong class="mb-2">
                         ${translate["map_overlapping_places"]}
                       </strong>
                       ${match
                        .map(x => `<a
                                      role='button'
                                      class="mb-1 uc-first"
                                      onclick="dispatchPopup(${x._leaflet_id},[${e.latlng.lat},${e.latlng.lng}])">
                                               ${x.feature?.properties?.name || x.feature?.properties?.objectName || translate['polygon'] + x._leaflet_id}
                                   </a>`).join("")}
                     </div>`;
                L.popup()
                    .setLatLng(e.latlng)
                    .setContent(content)
                    .openOn(map);
            }
        });
    }
}

function dispatchPopup(id, latlng) {
    const layer = selectedLayer._layers[id]
        || control.getActiveOverlays()._layers[id]
        || drawnItems._layers[id];
    if (typeof currentEditLayer !== 'undefined'
        && currentEditLayer?._leaflet_id === id)
        currentEditLayer?.openPopup(latlng);
    layer?.openPopup(latlng);
}

function buildPopup(feature, action = "view", selected = false) {
    return `<div id="popup">
            <strong>${feature.properties.objectName || ""}</strong>
            ${feature.properties.objectType || ""}
            <strong>${feature.properties.name || ""}</strong>
            <div style="max-height:140px;overflow-y:auto"> ${
        feature.properties.description || ""
    }</div>
            <div id="buttonBar">

            ${
        selected &&
        (window.location.href.includes("update") ||
            window.location.href.includes("insert"))
            ? `<button
               id="editButton"
               class="${style.button.primary}"
               onclick="editGeometry(${feature.properties.id})">
                 ${translate["edit"]}
               </button>
               <button
               id="deleteButton"
               class="${style.button.primary}"
               onclick="deleteGeometry(${feature.properties.id})">
                 ${translate["delete"]}
               </button>`
            : `<button
               class="${style.button.primary}"
               onclick="window.location.href='/entity/${feature.properties.objectId}'">
                 ${translate["details"]}
               </button>`
    }

            </div >
        </div > `;
}

$('.leaflet-geonames-icon').click(function ($e) {
    $e.preventDefault();
});
