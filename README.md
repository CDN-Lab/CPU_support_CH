# Getting started with Python

Here is a step-by-step guide on how to prepare your computer for running Python scripts including the batch processing, found in our snazzy CDN-Lab Github : https://github.com/CDN-Lab/ 

After completing these four steps, you will have a working Conda environment where you can run many python scripts that depend on some common Python libraries: matplotlib, ipython, pandas, numpy, and scipy.  

*Important* if you are doing this for the first time, follow steps 1-4 closely. If you have completed steps 1-4 before and just need to reactivate your conda environment, skip ahead to step 5 below 



### 1. Download miniconda files 

- Look up which chip/processor you have : [use directions here](https://support.apple.com/en-us/HT211814#:~:text=To%20open%20About%20This%20Mac,name%20of%20an%20Intel%20processor.)

- Go to our Sharepoint [miniconda](https://nih.sharepoint.com/:f:/r/sites/NIMH-CDNlab/Shared%20Documents/Code/miniconda?csf=1&web=1&e=L5gLrH) and download the Miniconda3 installer file appropriate for your chip/processor: 
> (M1 chip) : Miniconda3-py39_22.11.1-1-MacOSX-arm64.sh  
> (Intel) : Miniconda3-py39_22.11.1-1-MacOSX-x86_64.sh  

If you cannot access our Sharepoint you should be able to find the installer in the [Conda website](https://docs.conda.io/en/latest/miniconda.html). 

- Please track the location in your computer where the file is downloaded. We *will* need this specific path in step 4:

> /path_to_file/Miniconda3-py39_22.11.1-1-MacOSX-***64.sh 


### 2. Prepare directories 

- Introduction to using a Terminal : [short tutorial here](https://www.youtube.com/watch?v=aKRYQsKR46I). We will use a `$` to denote that we are running a function from the terminal. 

- Open Terminal, and in your home directory, make a directory called "IDM_project"  

    `$ mkdir IDM_project`
    
    `$ cd IDM_project`


### 3. Git clone CPU_support 

- To start using the code in this repository, you have to create a copy of everything here on your own computer. To do this you can simply open a command window on your computer and run the following code. Inside the IDM_project directory, clone the CPU_support repository:

    `$ git clone https://github.com/CDN-Lab/CPU_support`

    `$ cd CPU_support`

If your computer does not have `git` you can download from [their website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).



### 4. Execute python script setup_conda.py 

- Run python scripts with python3. You can check python version with: 

    `$ python –-version`

    `$ python3 --version`

- [ optional ] Run the help command to familiarize yourself with the script 

    `$ python3 setup_conda.py --help`

- Use setup_conda.py to install Conda: 

    `$ python3 setup_conda.py -ip ~/Downloads/Miniconda3-py39_22.11.1-1-MacOSX-***64.sh -dp /path_to_conda`

* NOTE: * You can omit the –dp field, in which case, miniconda will be installed in your home directory: /Users/username/opt/ 

- Source the miniconda environment: 

    `$ source /path_to_conda/miniconda/bin/activate`

- Use setup_conda.py again to create conda environment: 

    `$ python3 setup_conda.py --create_environment`

* NOTE: * If this step does not work, you may need to copy the .condarc file to the home directory 

- Activate the conda_environment, now you can run the batch processing script 

    `$ conda activate idm_env`




### 5. Conda already set up? 

If you have already gone through steps 1-4 and just need to activate your conda environment, do the following: 

- Source the miniconda environment: 

    `$ source /path_to_conda/miniconda/bin/activate`

- Activate the conda_environment, now you can run the batch processing script 

    `$ conda activate idm_env`

