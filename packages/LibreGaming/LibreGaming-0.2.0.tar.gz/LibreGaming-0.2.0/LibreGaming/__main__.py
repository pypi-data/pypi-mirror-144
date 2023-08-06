from .LibreGaming import LibreGaming
import os, argparse

#Parse commandline arguments
def parse_arguments():
    parser = argparse.ArgumentParser(usage="%(prog)s <arguments>", description="Install Gaming Packages with ease",
                                     epilog="GPLv3 - Repo : https://github.com/Ahmed-Al-Balochi/LibreGaming.git")
    parser.add_argument('-g', '--gaming', action='store_true', help='Install all the Gaming Packages(Steam,Wine-Staging,Gamemode,Lutris,Heroic,MangoHud & Goverlay)')
    parser.add_argument('-b', '--basic', action='store_true', help='Install Basic Gaming Packages(Steam,Wine-Staging,Gamemode)')
    parser.add_argument('-ath', '--athenaeum', action='store_true', help='Install Athenaeum Launcher')
    parser.add_argument('-o', '--overlays', action='store_true', help='Install Mangohud & Goverlay')
    parser.add_argument('-p', '--proton', action='store_true', help='Install/Update ProtonGE(You must run Steam once before installing ProtonGE)')
    parser.add_argument('-l', '--list', action='store_true', help='List installed ProtonGE Releases')
    parser.add_argument('-t', '--tag', action='store',type=str, default=None, help='Install a specific ProtonGE Release')
    parser.add_argument('-r', '--rem', action='store', type=str, default=None, metavar='TAG', help='remove a specific ProtonGE Release')
    parser.add_argument('--releases', action='store_true', help='List ProtonGE Releases')
    parser.add_argument('--tui', action='store_true', help='use a Terminal User Interface to install Packages ')
    parser.add_argument('--heroic', action='store_true', help='Install Heroic Launcher')
    parser.add_argument('--lutris', action='store_true', help='Install Lutris Launcher')
    parser.add_argument('--itch', action='store_true', help='Install itch.io Launcher')
    parser.add_argument('--stl', action='store_true', help='Install Steam Tinker Launch(For Arch Linux only)')
    return parser.parse_args()

# Main execution
def main():
    LibreGaming_Object = LibreGaming()
    args = parse_arguments()
    if args.tui:
        dir = os.path.dirname(__file__)
        # Gets the path to the TUI.py file
        tui = os.path.join(dir, 'TUI.py')
        os.system("python3 "+tui)
    if args.proton:
        LibreGaming_Object.protonup_Install_Latest()
    if args.releases:
        LibreGaming_Object.protonup_Show_Releases()
    if args.list:
        LibreGaming_Object.protonup_List()
    if args.tag:
        LibreGaming_Object.protonup_Install_Specific()
    if args.rem:
        LibreGaming_Object.protonup_Remove()
    if args.gaming:
        LibreGaming_Object.installAllPkgs()
    if args.basic:
        LibreGaming_Object.BasicPkgs()
    if args.overlays:
        LibreGaming_Object.Overlays()
    if args.lutris:
        LibreGaming_Object.Lutris()
    if args.heroic:
        LibreGaming_Object.Heroic()
    if args.itch:
        LibreGaming_Object.Common_Pkgs_Object.itch()
    if args.stl:
        LibreGaming_Object.STL()
    if args.athenaeum:
        LibreGaming_Object.Common_Pkgs_Object.Athenaeum()

if __name__ == "__main__":
    main()
