import argparse
import os,sys
import subprocess


def install_conda(installer_path,destination_path):
	if not destination_path:
		home_dir = os.path.expanduser('~')
		destination_path = os.path.join(home_dir,'opt')
		print('No destination_path was specified, so we will use: {}'.format(destination_path))
		if not os.path.exists(destination_path):
		    os.makedirs(destination_path)

	if not os.path.exists(installer_path):
	    print('The path for the miniconda does not exist : {}'.format(installer_path))
	    raise SystemExit(1)
	else:
		miniconda_path = os.path.join(destination_path,'miniconda')
		if os.path.exists(miniconda_path):
			print('It seems miniconda is already installed in : {}'.format(miniconda_path))
			raise SystemExit(1)
		command = 'bash {} -b -p {}'.format(installer_path,miniconda_path)
		print('Executing {}'.format(command))
		args = command.split()
		subprocess.run(args,check=True)
		print('Huzzah! First part has completed, now we will create a virtual environment')
		print('Please copy paste and execute the following command:')
		command = 'source {}'.format(os.path.join(miniconda_path,'bin/activate'))
		print('\n >>> {} <<<\n'.format(command))

def create_conda_env():
	command = 'conda create -n idm_env python=3.9 matplotlib ipython pandas numpy scipy'
	print('Executing {}'.format(command))
	args = command.split()
	subprocess.run(args,check=True)

	print('Now you can activate and deactivate using the commands above')



def main():

	parser = argparse.ArgumentParser(description="Set up miniconda in your local computer")
	parser.add_argument("-ip","--installer_path", 
		help="1a. Location of Miniconda installer: /path_to_miniconda/Miniconda3-py39_22.11.1-1-MacOSX-x86_64.sh")
	parser.add_argument("-dp","--destination_path", 
		help="1b. [optional] Destination to install Miniconda: default to /home_dir/opt", nargs='?', const='')
	parser.add_argument("-ce","--create_environment", 
		help="2. Create conda environment, after running part 1",action="store_true")
	args = parser.parse_args()
	installer_path = args.installer_path
	destination_path = args.destination_path
	create_environment = args.create_environment

	if installer_path or destination_path:
		install_conda(installer_path,destination_path)
	elif create_environment:
		create_conda_env()
	else:
		parser.print_help()
		raise SystemExit(1)

	# conda env remove --yes -n new_env    # remove the environment new_env if it exists (optional)


if __name__ == "__main__":
    main()



