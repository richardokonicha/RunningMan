from cx_Freeze import setup, Executable

# Include the name of all folder or files in your project folder that are nessesary for the project excluding your main flask file.
# If there are multiple files, you can add them into a folder and then specify the folder name.

includefiles = ['.env']
includes = ['catcher', 'runner', 'config']
excludes = []

setup(
    name='Running Man',
    version='0.1',
    description='Running Man',
    options={'build_exe':   {'excludes': excludes,
                             'include_files': includefiles, 'includes': includes}},
    executables=[Executable('runningman.py')]
)

# In place of main.py file add your main flask file name
