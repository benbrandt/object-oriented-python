import project_settings

project = project_settings.Project()

project.new_project(project.project_directory())

project.create_folders(project.PROGRAMS)