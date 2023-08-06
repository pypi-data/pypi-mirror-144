from typing import Set, Tuple, Dict, Collection

from bauh.api.abstract.handler import ProcessWatcher
from bauh.api.abstract.view import MultipleSelectComponent, InputOption, FormComponent, SingleSelectComponent, \
    SelectViewType
from bauh.commons import resource
from bauh.commons.html import bold
from bauh.commons.view_utils import get_human_size_str
from bauh.gems.arch import ROOT_DIR, get_repo_icon_path, get_icon_path, pacman
from bauh.view.util.translation import I18n


def _get_repo_icon(repository: str):
    return resource.get_path('img/{}.svg'.format('arch' if repository == 'aur' else 'repo'), ROOT_DIR)


def request_optional_deps(pkgname: str, pkg_repos: dict, watcher: ProcessWatcher, i18n: I18n) -> Set[str]:
    opts = []

    repo_deps = [p for p, data in pkg_repos.items() if data['repository'] != 'aur']
    sizes = pacman.map_update_sizes(repo_deps) if repo_deps else {}

    for p, d in pkg_repos.items():
        size = sizes.get(p)
        op = InputOption('{}{} ({}: {}) - {}: {}'.format(p, ': ' + d['desc'] if d['desc'] else '',
                                                         i18n['repository'],
                                                         d['repository'].lower(),
                                                         i18n['size'].capitalize(),
                                                         get_human_size_str(size) if size is not None else '?'), p)
        op.icon_path = _get_repo_icon(d['repository'])
        opts.append(op)

    view_opts = MultipleSelectComponent(label='',
                                        options=opts,
                                        default_options=set(opts))

    install = watcher.request_confirmation(title=i18n['arch.install.optdeps.request.title'],
                                           body='<p>{}.</p><p>{}:</p>'.format(i18n['arch.install.optdeps.request.body'].format(bold(pkgname)), i18n['arch.install.optdeps.request.help']),
                                           components=[view_opts],
                                           confirmation_label=i18n['install'].capitalize(),
                                           deny_label=i18n['do_not.install'].capitalize())

    if install:
        return {o.value for o in view_opts.values}


def request_install_missing_deps(deps: Collection[Tuple[str, str]], watcher: ProcessWatcher, i18n: I18n) -> bool:
    msg = f"<p>{i18n['arch.missing_deps.body'].format(deps=bold(str(len(deps))))}:</p>"

    opts = []

    repo_deps = [d[0] for d in deps if d[1] != 'aur']
    sizes = pacman.map_update_sizes(repo_deps) if repo_deps else {}

    for dep in deps:
        size = sizes.get(dep[0])
        op = InputOption('{} ({}: {}) - {}: {}'.format(dep[0],
                                                       i18n['repository'],
                                                       dep[1].lower(),
                                                       i18n['size'].capitalize(),
                                                       get_human_size_str(size) if size is not None else '?'), dep[0])
        op.read_only = True
        op.icon_path = _get_repo_icon(dep[1])
        opts.append(op)

    comp = MultipleSelectComponent(label='', options=opts, default_options=set(opts))
    return watcher.request_confirmation(i18n['arch.missing_deps.title'], msg, [comp], confirmation_label=i18n['continue'].capitalize(), deny_label=i18n['cancel'].capitalize(),
                                        min_width=600)


def request_providers(providers_map: Dict[str, Set[str]], repo_map: Dict[str, str], watcher: ProcessWatcher, i18n: I18n) -> Set[str]:
    msg = "<p>{}.</p><p>{}.</p>".format(i18n['arch.dialog.providers.line1'],
                                        i18n['arch.dialog.providers.line2'])

    repo_icon_path = get_repo_icon_path()
    aur_icon_path = get_icon_path()

    form = FormComponent([], label='')

    for dep, providers in providers_map.items():
        opts = []

        repo_providers, aur_providers = {}, {}

        for p in providers:
            repo = repo_map.get(p, 'aur')

            if repo == 'aur':
                aur_providers[p] = repo
            else:
                repo_providers[p] = repo

        for current_providers in (repo_providers, aur_providers):
            for pname, repo in sorted(current_providers.items()):
                opts.append(InputOption(label=pname,
                                        value=pname,
                                        icon_path=aur_icon_path if repo == 'aur' else repo_icon_path,
                                        tooltip='{}: {}'.format(i18n['repository'].capitalize(), repo)))

        form.components.append(SingleSelectComponent(label=bold(dep.lower()),
                                                     options=opts,
                                                     default_option=opts[0],
                                                     type_=SelectViewType.COMBO,
                                                     max_per_line=1))

    if watcher.request_confirmation(title=i18n['arch.providers'].capitalize(),
                                    body=msg,
                                    components=[form],
                                    confirmation_label=i18n['proceed'].capitalize(),
                                    deny_label=i18n['cancel'].capitalize()):

        return {s.get_selected() for s in form.components if isinstance(s, SingleSelectComponent)}
