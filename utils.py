import subprocess
import i3

def run_dmenu(menu, *args):
    """ Run dmenu
        args : args passed to dmenu
        menu: list of possible choices
    returns the selected choice


    """
    process = subprocess.Popen(["dmenu"] + list(args),
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE)
    process.stdin.write("\n".join(menu)+"\n")
    out = process.communicate()[0]
    return out.strip()

def get_workspace_names():
    """ Get the list of workspace names

    """
    workspaces = i3.get_workspaces()
    return [x['name'] for x in workspaces]

def insert_new_workspace(workspaces, name):
    new_index = 1
    for workspace in workspaces:
        (w_index, w_name) = int(workspace[0]), workspace[3:]
        if w_name < name:
            new_index = w_index + 1
        else:
            new_name = "%i: %s" % (w_index+1, w_name)
            i3.command('rename workspace "%s" to "%s"' % (workspace, new_name))
    new_name = "%i: %s" % (new_index, name)
    return new_name


def sort_workspaces():
    names = get_workspace_names()
    names = names.sort(key=lambda x: x[3:])
    for i, name in enumerate(get_workspace_names()):
        if name[0].isdigit():
          w_name = name[3:]
          new_name = "%i: %s"  % (i+1, w_name)
        else:
          new_name = name; 
        print 'rename workspace "%s" to "%s"' % (name, new_name)
        if new_name != name:
            cmd = 'rename workspace "%s" to "%s"' % (name, new_name)
            i3.command(cmd)
