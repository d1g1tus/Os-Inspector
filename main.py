from bin.variables import gui as g
from bin.variables import main_vars as mv
from bin.commands import commands as cm

cm.clear("s")

while True:
    opt = str(input(f"{mv.lcyan}///// {mv.lgreen}-> {mv.yellow}")).split()
    try:
        if opt[0] == "help":
            if len(opt) == 1:
                print(f"{g.commands_help[opt[0]]}")
            elif opt[1] == "*":
                g.commands_help["*"]()
            else:
                print(f"{g.commands_help[opt[1]]}")
        if opt[0] == "list":
            print(mv.command_list)
        if opt[0] == "elist":
            print(g.command_list)
        else:
            try:
                getattr(cm, f"{opt[0]}")(opt)
            except IndexError:
                pass
            except AttributeError:
                pass
    except KeyError:
        pass
    except IndexError:
        pass
