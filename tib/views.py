from flask import render_template

from tib import app
from tib.data.digital import objects3d
from tib.data.image_descriptions import home_images
from tib.data.index import front_menu
from tib.data.oa_access import get_entity_from_oa, \
    get_oa_by_view_class, view_classes
from tib.data.subprojects import subprojects_dict
from tib.data.team import team_members
from tib.data.tib_volumes import tib_volumes_dict


@app.route('/')
def home() -> str:
    return render_template(
        'home/home.html',
        front_menu=front_menu,
        img_description=home_images,
        tib_volumes=tib_volumes_dict,
        subprojects=subprojects_dict,
        team=team_members)


@app.route('/team')
def team() -> str:
    return render_template(
        'team/team.html',
        team=team_members)


@app.route('/tib-volumes')
@app.route('/tib-volumes/<volume>')
def tib_volumes(volume: str = None) -> str:
    if volume:
        return render_template(
            f'tib_volumes/volume.html',
            tib_volume=tib_volumes_dict[volume])
    else:
        return render_template(
            'tib_volumes/tib_volumes.html')


@app.route('/subprojects')
@app.route('/subprojects/<project>')
def subprojects(project: str = None) -> str:
    if project:
        return render_template(
            f'subprojects/subproject.html',
            subproject=subprojects_dict[project])
    else:
        return render_template(
            'subprojects/subproject_overview.html')


@app.route('/öffentlichskeitsarbeit')
def outreach() -> str:
    return render_template('outreach/outreach.html')


@app.route('/entity/<id_>')
def entity_view(id_: int = None) -> str:
    return render_template(
        'digital/entity_view.html',
        entity=get_entity_from_oa(id_))


@app.route('/digital/')
def digital() -> str:
    return render_template(
        'digital/digital.html',
        objects3d=objects3d,
        subprojects_dict=subprojects_dict,
        view_classes=view_classes)


@app.route('/digital/<project>/<view>')
def digital_oa_access(project: str, view: str) -> str:
    return render_template(
        'digital/entity_table.html',
        data=get_oa_by_view_class(view, subprojects_dict[project]['oaID']),
        project=subprojects_dict[project],
        view_classes=view_classes[view])





# @app.route('/subprojects')
# @app.route('/subprojects/<project>')
# def subprojects(project=None):
#     if project:
#         project = next((item for item in
#                         Subprojects.get_subprojects(app.config['PROJECTS_ID'])
#                         if
#                         item.project[0] == project), None)
#         sidebar = render_template(
#             'projects/sidebar.html',
#             projects=project,
#             team=project.project_team,
#             sponsors=Sponsors.get_sponsors(app.config['FINANCIER_ID']))
#         return render_template(
#             'projects/project_details.html',
#             projects=project,
#             sidebar=sidebar)
#     else:
#         return render_template(
#             'projects/subprojects.html',
#             projects=Subprojects.get_subprojects(app.config['PROJECTS_ID']))


@app.route('/longterm')
def longterm():
    return render_template('longterm/longterm.html')


@app.route('/tib')
def tib():
    return render_template('longterm/longterm.html')


@app.route('/publications')
def publications():
    return render_template('longterm/longterm.html')


@app.route('/youth')
def youth():
    return render_template('longterm/longterm.html')


@app.route('/digtib')
def catalouge():
    return render_template('longterm/longterm.html')


@app.route('/dig-tib')
def dig_tib():
    return render_template('longterm/longterm.html')


@app.route('/maps')
def maps():
    return render_template('longterm/longterm.html')


@app.route('/relief')
def relief():
    return render_template('longterm/longterm.html')


@app.route('/model')
def model():
    return render_template('longterm/longterm.html')


@app.errorhandler(404)
def page_not_found(e: Exception) -> tuple:
    return render_template('404.html', e=e), 404
