from collections import OrderedDict

from flask import render_template

from tib import app


@app.route('/team')
def team() -> str:
    team_ = OrderedDict([
        ('Peter Fraundorfer', {
            'id': '1',
            'email': 'Peter.Fraundorfer@oeaw.ac.at',
            'function': 'Forschung',
            'text': """Schon in meinem Bachelorstudium hat mich vor allem die Kirchengeschichte 
            interessiert. Im Masterstudium am Institut für österreichische Geschichtsforschung 
            konnte ich dieses Interesse in meiner Masterarbeit über die hoch- und 
            spätmittelalterlichen Viten des heiligen Rupert ausleben. Es freut mich sehr durch die 
            Mitarbeit an diesem Projekt meinen forschenden Blick nun auch auf die 
            griechisch-orthodoxe Seite der europäischen Kirchengeschichte werfen zu dürfen.
            """,
            'img': 'peter.jpg',
        }),
        ('Verena Demel ', {
            'id': '2',
            'email': 'ena.demel@gmail.com',
            'function': 'Forschung',
            'text': """Während meines Lehramtsstudiums für Geschichte, Sozialkunde und Politische
             Bildung beschäftigte ich mich besonders mit Theorien des historischen Denkens und 
             Lernens sowie der Analyse historischer und musealer Erzählungen.
             Ich interessiere mich für sozial- und kulturgeschichtliche Themenfelder
             und freue mich, Teil dieses Projekts zu sein, dessen Forschungsgegenstand
             der Flucht und Vertreibung aufgrund der leider immer währenden Aktualität
             besonders spannend ist.""",
            'img': 'verena.jpg',
        }),
        ('Rainer Simon', {
            'id': '3',
            'email': 'Rainer.Simon@ait.ac.at',
            'function': 'App Deveolpment',
            'text': """Ich bin Senior Scientist in der Forschungsgruppe 'Data Science and Artificial
             Intelligence' am <a href="https://www.ait.ac.at" target="_blank">Austrian Institute of Technology</a>. In meiner
              Arbeit beschäftige ich mich vorwiegend mit dem Einsatz von Web- und <a href="https://en.wikipedia.org/wiki/Linked_data" target="_blank">Linked Data</a>-Technologien im Kultur- und
               Bibliotheksbereich, sowie in der geisteswissenschaftlichen Forschung. Meine besondere
                Leidenschaft gilt alten Landkarten, und in vielen meiner Projekte habe ich mich mit
                 geographischen oder kartographischen Daten beschäftigt. Als leidenschaftlicher
                  Softwarenentwickler arbeite ich mit verschiedensten Werkzeugen und
                   Programmiersprachen, in letzter Zeit vorwiegend JavaScript, Python und Scala.
            """,
            'img': 'rainer.jpg',
        }),
        ('Bernhard Koschicek', {
            'id': '4',
            'email': 'bernhard.koschicek@oeaw.ac.at',
            'function': 'Backend Development (ehrenamtlich)',
            'text': "",
            'img': 'bernhard.png',
        }),
        ('Sandra Wabnitz', {
            'id': '5',
            'email': 'Sandra.Wabnitz@oeaw.ac.at',
            'function': 'Forschung (ehrenamtlich)',
            'text': """Im Bachelorstudium Geschichte an der Uni Wien galt mein Interesse vor allem
             der Zeitgeschichte. Das Masterstudium am Institut für Österreichische
              Geschichtsforschung habe ich im Schwerpunkt Mittelalter mit einer Masterarbeit über
               die Integration der Barbaren in die lateinische und chinesische Historiographie des
                Frühmittelalters abgeschlossen. Ich freue mich Teil dieses Projektes zu sein, da ich
                 so meine Fähigkeiten, die ich im Masterstudium erworben habe, für ein
                  zeitgeschichtlichtes Thema einsetzen kann.""",
            'img': 'sandra.jpg',
        }),
        ('Mihailo Popović ', {
            'id': '6',
            'email': 'mihailop@hotmail.com',
            'function': 'Projektleiter',
            'text': """Seit meinem Studium der Byzantinistik und Neogräzistik sowie 
            südosteuropäischen Geschichte an der Universität Wien interessiere ich mich für die 
            mittelalterlichen und neuzeitlichen politischen, geistlichen und kulturellen Beziehungen
             zwischen unserem Land und Südosteuropa. Ich möchte mit meiner wissenschaftlichen Arbeit
              das gegenseitige Verständnis und Kennenlernen fördern sowie Brücken zwischen Menschen
               und Ländern bauen. In einem sich vereinenden Europa ist meiner Meinung nach ein
                solcher Dialog unerläßlich.""",
            'img': 'mihailo.jpg',
        }),

    ])
    return render_template('team.html', team=team_)
