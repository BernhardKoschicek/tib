from tib.data.image_descriptions import project_icons

descriptions = {
    'tib11': """
    <p>Der Band TIB 11 „Makedonien, südlicher Teil“ umfasst den südlichen Teil 
    der historischen Landschaft Makedonien. Das Bearbeitungsgebiet entspricht 
    etwa der römischen Provinz <i>Macedonia Prima</i> und ist zugleich die 
    Region Makedonia des jetzigen Nord-Griechenland, die von Epirus im Westen 
    bis Thrakien im Osten reicht und an die im Süden Thessalien anschließt. Im 
    Osten bildet die Nordküste der Ägäis die Südgrenze des Bearbeitungsgebiets. 
    Das Gebiet von TIB 11 hat eine Fläche von knapp 33.000 km² und grenzt im 
    Norden an Albanien, Nordmazedonien und Bulgarien, d. h. an Gebiete, die 
    fast zur Gänze Thema des Bandes <a href="TIB_16">TIB 16 „Makedonien, 
    nördlicher Teil sind.</a></p><p> Im 
    Bearbeitungsgebiet liegen Thessaloniki, über Jahrhunderte die 
    zweitwichtigste Stadt des Byzantinischen Reiches, und der Heilige Berg 
    Athos, seit dem 10. Jahrhundert ein Zentrum des orthodoxen Mönchtums. Die 
    Zuwanderung der Slawen im 6. und 7. Jahrhundert hat die mittelalterlichen 
    Ortsnamen (Toponymie) und Siedlungsgeschichte des Landes entscheidend 
    mitgeprägt, und Makedonien war fortan im Mittelalter Kontaktzone zwischen 
    Griechen und Slawen. Gegen Ende des 14. Jahrhunderts und in der ersten 
    Hälfte des 15. Jahrhunderts fiel die Region an das Osmanische Reich, 
    dessen frühe Steuerregister (Defter) teilweise auch die mittelalterliche 
    Toponymie wiedergeben.</p>
    <p>Der Katalogteil von TIB 11 (Lemmata) wird 2022 veröffentlicht werden.</p>
    """,

    'tib16': """
    <p>Der Band TIB 16 mit dem Titel „Makedonien, nördlicher Teil“ umfaßt die 
    spätrömischen bzw. frühbyzantinischen Provinzen <i>Macedonia Secunda</i> 
    und Teile der Provinzen <i>Macedonia Prima, Dardania, Epirus Nova, 
    Praevalitana</i> und <i>Dacia Mediterranea</i>. Er steht in engem 
    Zusammenhang mit <a href="TIB_11">TIB 11 „Makedonien, südlicher Teil“</a>. 
    Da sich Makedonien 
    als historischer Raum auf die modernen Staaten Griechenland, Nordmazedonien 
    und Bulgarien verteilt, werden im Band „Makedonien, nördlicher Teil“ das 
    gesamte Staatsgebiet Nordmazedoniens und zwei Bezirke Bulgariens 
    (Kjustendil und Blagoevgrad) bearbeitet. Somit wird die Lücke zwischen den 
    Bänden TIB 6 „Thrakien“ und TIB 11 „Makedonien, südlicher Teil“ 
    geschlossen.
    </p><p> 
    Als Basis der wissenschaftlichen Aufarbeitung dienen, neben regelmäßigen 
    Bereisungen, die schriftlichen historischen Quellen (hier vor allem die 
    griechischen, lateinischen, altslawischen und osmanischen), die Denkmäler, 
    der archäologische Befund und die mannigfaltigen Toponyme sowie eine 
    überaus reiche Sekundärliteratur, die im wesentlichen in den südslawischen 
    Sprachen verfaßt ist. Des weiteren fließen in diesen Band neue Methoden 
    der historischen Geographie ein, im konkreten verschiedenartige 
    Siedlungstheorien (z. B. die modifizierte Central Place Theory) sowie 
    Anwendungen aus dem Bereich der Geoinformatik (Historical Geographic 
    Information Systems / HGIS), die in den Teilprojekten der TIB Balkan 
    erarbeitet wurden und in der 
    <a href="https://oeaw.academia.edu/MapsofPower">„Maps of Power: 
    Historical Atlas of Places, 
    Borderzones and Migration Dynamics in Byzantium“  Initiative</a> der TIB 
    Balkan erfolgreich eingesetzt werden.</p>
    """,

    'tib17': """
    <p>Der Band "Nea Epeiros und Praevalis" (TIB 17; Mihailo St. Popović) 
    umfaßt die frühbyzantinischen Provinzen desselben Namens bzw. das gesamte 
    Staatsgebiet Montenegros, den Nordteil Albaniens und die Region Raška 
    (Novi Pazar) in Serbien. Dieser Band schließt die Lücke zwischen 
    <a href="TIB_16">"Makedonien, nördlicher Teil" (TIB 16; Mihailo St. 
    Popović)</a> und "Nikopolis und Kephallenia" (TIB 3).
    </p><p>
    Als Basis der wissenschaftlichen Aufarbeitung dienen, neben regelmäßigen 
    Bereisungen vor Ort, die schriftlichen historischen Quellen (hier vor 
    allem die griechischen, lateinischen, altslawischen und osmanischen), die 
    Denkmäler, der archäologische Befund und die mannigfaltigen Toponyme sowie 
    eine überaus reiche Sekundärliteratur, die im wesentlichen in den 
    südslawischen Sprachen verfaßt ist. Ein besonderes Augenmerk wird auf das 
    Kulturerbe im Bearbeitungsgebiet gelegt, das auch auf der Basis von 
    unveröffentlichtem österreichisch-ungarischen Archivmaterial im 
    Österreichischen Staatsarchiv erschlossen und erforscht wird.
    </p>
    """,
}

tib_volumen_dict = {
    'TIB_11': {
        'title': 'Makedonien, südlicher Teil',
        'author': 'Peter Soustal',
        'icon_description': project_icons['tib11'],
        'icon': 'images/boxes_background/tib11_icon.jpg',
        'description': descriptions['tib11'],
        'subprojects': [],
        'images': 'tib11'
    },
    'TIB_16': {
        'title': 'Makedonien, nördlicher Teil',
        'author': 'Mihailo Popović',
        'icon_description': project_icons['tib16'],
        'icon': 'images/boxes_background/tib16_icon.jpg',
        'description': descriptions['tib16'],
        'subprojects': [],
        'images': 'tib16'
    },
    'TIB_17': {
        'title': 'Nea Epeiros und Praevalis',
        'author': 'Mihailo Popović',
        'icon_description': project_icons['tib17'],
        'icon': 'images/boxes_background/tib17_icon.jpg',
        'description': descriptions['tib17'],
        'subprojects': [],
        'images': 'tib17'
    }
}
