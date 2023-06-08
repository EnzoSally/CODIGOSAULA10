import cx_Freeze
#pip install cx_Freeze

executables = [
    cx_Freeze.Executable(script="mainbkp.py", icon="flappy.ico")
]

cx_Freeze.setup(
        name = "Flappy",
        options = {
            "build_exe":{
                "packages": ["pygame"],
                "include_files":[
                    "FUNDOSONIC.jpg",
                    "flappy.png"
            ]
        }
    } , executables = executables
)

#python nome do arquivo build